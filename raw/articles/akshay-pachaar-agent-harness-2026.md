# Agent Harness 解剖：The Anatomy of an Agent Harness

> 原文作者：**Akshay 🚀** (@akshay_pachaar)
> 翻译时间：2026-04-18
> 原文数据：38 回复 | 259 转发 | 1.5K 点赞 | 3.8K 收藏 | 628K 浏览
> 推文链接：https://x.com/akshay_pachaar/status/2041146899319971922?s=52

---

一句话总结：真正决定 Agent 在生产环境中是否可靠的，往往不是模型本身，而是包裹模型的 agent harness——也就是负责编排循环、工具、记忆、上下文、状态、安全和验证的整套运行系统。

---

## 全文翻译

### A deep dive into what Anthropic, OpenAI, Perplexity and LangChain are actually building.

深入拆解 Anthropic、OpenAI、Perplexity 和 LangChain 实际上在构建什么：编排循环、工具、记忆、上下文管理，以及所有那些把一个“无状态 LLM”变成“可工作的智能体”的系统部件。

你已经做出了一个聊天机器人。
也许你还接上了一个带几个工具的 ReAct loop。
做 demo 的时候一切都能跑。

但一旦你尝试构建真正能用于生产环境的系统，问题就来了：模型会忘记三步之前做过什么，工具调用会静默失败，上下文窗口会被一堆垃圾信息塞满。

问题不在于你的模型。
问题在于模型之外的整套系统。

LangChain 已经证明了这一点：他们只改变了包裹 LLM 的那层基础设施——模型没变、权重没变——就在 TerminalBench 2.0 上从前 30 名之外直接跃升到第 5 名。
另一个研究项目则让 LLM 去优化这层基础设施本身，最终拿到了 76.4% 的通过率，超过了人工设计的系统。

现在，这套基础设施终于有了一个名字：agent harness。

## What Is the Agent Harness?

“Agent Harness” 这个术语是在 2026 年初被正式明确下来的，但它描述的概念早就存在了。

Harness 指的是包裹在 LLM 外面的整套软件基础设施，包括：
- 编排循环（orchestration loop）
- 工具（tools）
- 记忆（memory）
- 上下文管理（context management）
- 状态持久化（state persistence）
- 错误处理（error handling）
- 安全护栏（guardrails）

Anthropic 的 Claude Code 文档说得很直接：这个 SDK 就是“驱动 Claude Code 的 agent harness”。
OpenAI 的 Codex 团队也使用了同样的表述，明确把“agent”和“harness”这两个词用来指代让 LLM 变得实用的那套非模型基础设施。

我特别喜欢 LangChain 的 Vivek Trivedy 提出的那句定义：

“If you're not the model, you're the harness.”

这里有一个很容易让人混淆的点：
“Agent” 指的是用户所看到的那个具备目标导向、能调用工具、会自我纠错的行为体；
“Harness” 则是生成这种行为的机械系统。

所以当一个人说“我做了一个 agent”，更准确地说，其实是：
他做了一套 harness，然后把它接到了一个模型上。

Beren Millidge 在 2023 年的文章《Scaffolded LLMs as Natural Language Computers》中给出了一个非常精准的类比：
一个原始 LLM 就像一颗没有 RAM、没有硬盘、没有 I/O 的 CPU。

- 上下文窗口就像 RAM：速度快，但容量有限
- 外部数据库就像磁盘：容量大，但访问慢
- 工具集成就像设备驱动
- Harness 则像操作系统

正如 Millidge 所说：“我们重新发明了冯·诺依曼架构”，因为这对任何计算系统来说都是一种自然抽象。

## Three Levels of Engineering

围绕模型，有三个同心层次的工程工作：

- Prompt engineering：设计模型收到的指令
- Context engineering：管理模型在什么时候看到什么内容
- Harness engineering：不仅包含前两者，还包括完整的应用基础设施——工具编排、状态持久化、错误恢复、验证循环、安全执行和生命周期管理

Harness 不是一个 prompt 外壳。
它是让自主智能体行为成为可能的完整系统。

## The 12 Components of a Production Harness

综合 Anthropic、OpenAI、LangChain 以及更广泛实践社区的做法，一个生产级的 agent harness 至少包含 12 个不同组件。下面逐一来看。

### 1. The Orchestration Loop

这是心跳。
它实现的是 Thought-Action-Observation（TAO）循环，也叫 ReAct loop。

循环通常长这样：
- 组装 prompt
- 调用 LLM
- 解析输出
- 执行任何工具调用
- 把结果回填给模型
- 重复，直到任务结束

从机械实现上说，它往往只是一个 while 循环。
复杂性不在循环本身，而在循环管理的所有东西上。
Anthropic 把自己的运行时称作“一个愚蠢的循环（dumb loop）”，因为真正的智能都在模型里，harness 只是负责管理回合。

### 2. Tools

工具是 agent 的手。

工具会以 schema 的形式被定义出来：名字、描述、参数类型，然后注入到 LLM 的上下文中，让模型知道自己能做什么。
工具层负责：
- 工具注册
- schema 校验
- 参数提取
- 沙箱执行
- 结果捕获
- 将结果格式化回 LLM 可读的 observation

Claude Code 提供六大类工具：
- 文件操作
- 搜索
- 执行
- Web 访问
- 代码智能
- 子智能体调用

OpenAI Agents SDK 则支持：
- function tools（通过 @function_tool）
- hosted tools（WebSearch、CodeInterpreter、FileSearch）
- MCP server tools

### 3. Memory

记忆在多个时间尺度上工作。

- 短期记忆：一个会话内的对话历史
- 长期记忆：跨会话持久化的信息

Anthropic 用项目级的 CLAUDE.md 和自动生成的 MEMORY.md 文件；
LangGraph 用按 namespace 组织的 JSON Store；
OpenAI 则支持由 SQLite 或 Redis 支撑的 Sessions。

Claude Code 实现了一个三层结构：
- 轻量索引（每条大约 150 个字符，始终加载）
- 按需拉取的详细主题文件
- 只通过搜索访问的原始 transcript

这里有一个关键设计原则：
Agent 对自己的记忆应当把它当作“提示（hint）”，而不是直接当真；真正行动前，要去验证当前真实状态。

### 4. Context Management

这是很多 agent 悄悄失败的地方。

核心问题是 context rot：当关键信息落在长上下文的中间位置时，模型表现会下降 30% 以上。Chroma 的研究和 Stanford 的 “Lost in the Middle” 都证明了这一点。
即使是百万 token 的上下文窗口，随着长度上升，指令遵循能力依然会退化。

生产环境中的常见策略包括：

- Compaction：接近上下文上限时做摘要压缩。Claude Code 会保留架构决策和未解决 bug，丢弃冗余工具输出。
- Observation masking：JetBrains 的 Junie 会隐藏旧的工具输出，但保留工具调用本身。
- Just-in-time retrieval：维护轻量标识符，动态加载真正需要的数据。Claude Code 更倾向于 grep、glob、head、tail，而不是一上来读整文件。
- Sub-agent delegation：子智能体可以做大量探索，但只返回 1000 到 2000 token 的压缩总结。

Anthropic 的 context engineering 指南对目标的表述非常精确：
找到“最小的一组高信号 token”，用来最大化得到目标结果的概率。

### 5. Prompt Construction

这一步负责组装模型每一轮真正看到的内容。
它是分层的：
- system prompt
- tool definitions
- memory files
- conversation history
- 当前用户消息

OpenAI 的 Codex 使用一个严格的优先级栈：
- 服务器控制的 system message（最高优先级）
- tool definitions
- developer instructions
- user instructions（包括层层叠加的 AGENTS.md 文件，最多 32 KiB）
- conversation history

### 6. Output Parsing

现代 harness 越来越依赖原生 tool calling，也就是模型直接返回结构化的 tool_calls 对象，而不是输出自由文本再由系统解析。

Harness 要检查的是：
- 有没有 tool calls？有的话就执行工具并继续循环
- 没有 tool calls？那就是最终答案

对于结构化输出，OpenAI 和 LangChain 都支持通过 Pydantic 等 schema 约束输出。
早期那种 RetryWithErrorOutputParser 的办法依然存在：把原始 prompt、失败的 completion 和 parsing error 一起喂回模型，让模型重试修正。

### 7. State Management

LangGraph 把状态建模成沿着图节点流动的 typed dictionary，并通过 reducer 合并更新。
在 super-step 边界做 checkpoint，因此支持中断恢复和时间旅行调试。

OpenAI 提供四种互斥的状态策略：
- application memory
- SDK sessions
- 服务端 Conversations API
- 更轻量的 previous_response_id 链接

Claude Code 则走另一条路：
- 用 Git commit 作为 checkpoint
- 用 progress files 作为结构化 scratchpad

### 8. Error Handling

为什么这件事重要？
因为一个 10 步流程，如果每一步成功率是 99%，最终端到端成功率也只有约 90.4%。
错误会非常快地复利。

LangGraph 把错误分成四类：
- transient：临时性错误，应该指数退避重试
- LLM-recoverable：把错误作为 ToolMessage 返回，让模型自己调整
- user-fixable：需要用户提供输入，因此应该中断并等待人类
- unexpected：超出预期的系统错误，直接上抛便于调试

Anthropic 的做法是在工具 handler 内部捕获失败，并把错误以 error result 的形式返回，确保整个循环继续运行。
Stripe 的生产 harness 则把重试次数限制在两次。

### 9. Guardrails and Safety

OpenAI 的 SDK 实现了三层 guardrails：
- input guardrails：针对最初输入
- output guardrails：针对最终输出
- tool guardrails：针对每一次工具调用

其中还有一个“tripwire”机制，一旦触发，agent 会被立刻停止。

Anthropic 则在架构上把“权限执行”和“模型推理”分开：
- 模型决定它想尝试做什么
- 工具系统决定它是否被允许做

Claude Code 可以独立控制约 40 种不同的工具能力，并分三阶段执行：
1. 项目加载时建立信任
2. 每次工具调用前做权限检查
3. 对高风险操作要求用户显式确认

### 10. Verification Loops

这是真正把 toy demo 和 production agent 拉开差距的地方。

Anthropic 推荐三种验证方式：
- 规则型反馈：测试、linters、type checkers
- 视觉反馈：例如 UI 任务用 Playwright 截图验证
- LLM-as-judge：让另一个子智能体来评估输出质量

Claude Code 的创建者 Boris Cherny 曾说：
只要给模型一个验证自己工作的办法，整体质量就会提高 2 到 3 倍。

### 11. Subagent Orchestration

Claude Code 支持三种子智能体执行模式：
- Fork：父上下文的字节级拷贝
- Teammate：独立终端 pane，通过文件邮箱通信
- Worktree：独立 git worktree + 独立分支

OpenAI SDK 也支持两种：
- agents-as-tools：专家 agent 处理一个有边界的子任务
- handoffs：把控制权完整交给另一个专家 agent

LangGraph 则把子智能体实现成嵌套的状态图。

## The Loop in Motion: A Step-by-Step Walkthrough

现在你已经知道这些组件是什么了，我们来走一遍一个循环是怎么工作的。

### Step 1: Prompt Assembly
Harness 先构建完整输入：
- system prompt
- tool schemas
- memory files
- conversation history
- 当前用户消息

重要的信息会尽量放在 prompt 的开头和结尾，以避免 “Lost in the Middle”。

### Step 2: LLM Inference
把拼好的 prompt 发给模型 API。
模型输出 token：可能是文本、tool call 请求，或者两者都有。

### Step 3: Output Classification
- 如果模型只生成文本且没有 tool calls，循环结束。
- 如果它请求了 tool calls，就进入工具执行。
- 如果它请求 handoff，就切换当前 agent 并重新开始。

### Step 4: Tool Execution
对每一个 tool call：
- 校验参数
- 检查权限
- 在沙箱环境里执行
- 捕获结果

只读操作可以并行执行；有副作用的操作应该串行执行。

### Step 5: Result Packaging
工具结果会被格式化成模型可读消息。
错误不会让循环直接崩掉，而是作为 error result 返回给模型，供它自我修正。

### Step 6: Context Update
结果被追加到对话历史中。
如果快接近上下文窗口上限，就触发 compaction。

### Step 7: Loop
回到 Step 1，继续。
直到满足终止条件。

常见终止条件包括：
- 模型输出了无工具调用的最终答案
- 超过最大回合数
- token 预算耗尽
- guardrail tripwire 触发
- 用户主动中断
- 出现安全拒绝

一个简单问题也许只要 1 到 2 轮。
一个复杂重构任务则可能要经历几十轮、跨越大量工具调用。

对于跨多个上下文窗口的长任务，Anthropic 发展出一种两阶段的 “Ralph Loop” 模式：
- Initializer Agent：负责初始化环境（启动脚本、进度文件、功能列表、初始 Git commit）
- Coding Agent：后续每一轮新会话都先读取 git log 和 progress files 来恢复上下文，然后选择最高优先级的未完成功能，继续工作、提交并写总结

这里，文件系统承担了跨上下文窗口的连续性。

## How Real Frameworks Implement the Pattern

### Anthropic / Claude Agent SDK
Anthropic 的 Claude Agent SDK 通过一个 query() 函数暴露 harness：它会创建 agentic loop，并返回一个可流式迭代消息的异步迭代器。
运行时本质上就是一个“dumb loop”，智能都放在模型里。

Claude Code 的工作模式可概括为：
Gather → Act → Verify
即：
- 收集上下文（搜索文件、读代码）
- 执行动作（改文件、跑命令）
- 验证结果（跑测试、检查输出）
- 再重复

### OpenAI / Agents SDK
OpenAI Agents SDK 通过 Runner 类实现 harness，支持 async、sync 和 streamed 三种模式。
这个 SDK 是“code-first”的：工作流逻辑用原生 Python 写，而不是图 DSL。

Codex harness 在此基础上进一步扩展出三层结构：
- Codex Core（agent code + runtime）
- App Server（双向 JSON-RPC API）
- Client surfaces（CLI、VS Code、Web App）

由于所有表面都共享同一套 harness，所以 “Codex 模型在 Codex 自家表面上比在一个通用聊天窗口里表现更好”。

### LangGraph
LangGraph 把 harness 显式建模成状态图。
最核心的是两个节点：
- llm_call
- tool_node

二者之间由条件边连接：
- 如果存在 tool calls，则流向 tool_node
- 如果没有，则直接 END

LangGraph 是从 LangChain 的 AgentExecutor 演化而来。后者在 v0.2 被废弃，因为难以扩展，也不适合多智能体。

LangChain 的 Deep Agents 则明确使用了 “agent harness” 这个词：
内置工具、planning（如 write_todos 工具）、文件系统上下文管理、子智能体和持久记忆，全都属于 harness 的一部分。

### CrewAI
CrewAI 实现了一种基于角色的多智能体架构：
- Agent：包裹 LLM 的 harness，由 role、goal、backstory 和 tools 定义
- Task：工作单元
- Crew：agent 集合

CrewAI 的 Flows 层则提供“确定性骨架 + 智能生长点”：
路由、验证和流程控制由 Flows 管；自主协作由 Crew 负责。

### AutoGen / Microsoft Agent Framework
AutoGen（后来演变为 Microsoft Agent Framework）开创了“对话驱动编排”的范式。
它的三层结构（Core、AgentChat、Extensions）支持五种编排模式：
- sequential
- concurrent（fan-out / fan-in）
- group chat
- handoff
- magentic（由 manager agent 维护动态任务账本并协调专家）

## The Scaffolding Metaphor

“脚手架”这个比喻不是装饰性的，它非常准确。

建筑工地上的脚手架，是让工人能够触达高处、完成本来碰不到的部分的临时基础设施。
它本身不负责施工。
但没有它，工人就够不到高层。

关键洞察在于：
楼建成后，脚手架应该被拆掉。

同样地，随着模型越来越强，harness 的复杂性应该下降。
Manus 在 6 个月里重写了 5 次，每一次重写都在减少复杂度。
复杂的工具定义逐渐变成通用 shell 执行；“管理 agent”则变成简单的结构化 handoff。

这引出了一个协同进化原则：
模型现在会带着特定 harness 一起做后训练。
Claude Code 的模型学会了使用它训练时绑定的那套特定 harness。
因此，仅仅改变工具实现方式，也可能降低模型表现，因为两者高度耦合。

一个好的 harness 设计，应该通过“面向未来的测试”：
如果模型更强了，而你不需要继续加复杂度、性能反而自然提升，那么这个 harness 的方向就是对的。

## Seven Decisions That Define Every Harness

每个 harness 架构师都要面对七个关键选择：

### 1. Single-agent vs Multi-agent
Anthropic 和 OpenAI 的建议都非常一致：
先把单智能体做到极致。

多智能体系统会带来额外开销：
- 路由需要额外 LLM 调用
- handoff 会带来上下文丢失

只有当工具数量超过约 10 个、或者任务域明显分离时，再考虑拆分。

### 2. ReAct vs Plan-and-Execute
- ReAct：每一步交替进行推理和行动，灵活，但每一步成本高
- Plan-and-Execute：先规划，再执行

LLMCompiler 报告称，相比顺序式 ReAct，它能获得 3.6 倍提速。

### 3. Context Window Management Strategy
生产环境里常见五种策略：
- 按时间清空
- 对话摘要
- observation masking
- 结构化笔记
- 子智能体委派

ACON 研究表明：通过优先保留 reasoning trace 而不是原始工具输出，可以减少 26% 到 54% 的 token，同时保持 95% 以上准确率。

### 4. Verification Loop Design
- 计算型验证：测试、lint、类型检查，给出确定性真值
- 推断型验证：LLM-as-judge，能发现语义问题，但会增加延迟

Thoughtworks 的 Martin Fowler 团队把这称为：
- guides（前馈，引导行动前的方向）
- sensors（反馈，行动后的观测）

### 5. Permission and Safety Architecture
安全架构通常在两端之间取舍：
- permissive：快，但风险高，大量自动批准
- restrictive：安全，但慢，每个动作都可能需要审批

具体选择取决于部署场景。

### 6. Tool Scoping Strategy
工具越多，不一定效果越好。

Vercel 从 v0 里删掉了 80% 的工具，结果反而更好。
Claude Code 通过 lazy loading 达成了 95% 的上下文削减。

原则是：
只暴露当前步骤真正需要的最小工具集合。

### 7. Harness Thickness
也就是：
到底要把多少逻辑放在 harness 里，多少留给模型。

Anthropic 的下注是薄 harness + 更强模型。
图工作流框架则更偏向显式控制。

Anthropic 会随着模型版本变强，持续从 Claude Code 的 harness 里删除规划步骤，因为这些能力逐渐被模型内化了。

## The Harness Is the Product

两个使用完全相同模型的产品，仅仅因为 harness 设计不同，就可能出现巨大的性能差异。
TerminalBench 的证据已经说明了这一点：
只改 harness，就足以让 agent 在榜单上前后移动 20 多个名次。

Harness 不是一个已经被解决、或者可以商品化忽略的层。
真正困难的工程问题都在这里：
- 如何把上下文当作稀缺资源来管理
- 如何设计验证循环，防止错误级联
- 如何构建既能提供连续性、又不会鼓励幻觉的记忆系统
- 如何决定该搭多少脚手架，多少交给模型自己学会

这个领域正在朝着“更薄的 harness”演化，因为模型会越来越强。
但 harness 本身不会消失。

再强的模型，也需要有人来：
- 管理上下文窗口
- 执行工具调用
- 持久化状态
- 验证工作结果

所以下次你的 agent 失败时，别先怪模型。
先看看 harness。

---

## 原文链接

- X 原帖：https://x.com/akshay_pachaar/status/2041146899319971922?s=52
- 作者主页：https://x.com/akshay_pachaar
