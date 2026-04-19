# Akshay Pachaar — Agent Harness 解剖指南

**来源**: https://x.com/akshay_pachaar/status/2041146899319971922  
**作者**: Akshay 🚀 (@akshay_pachaar)  
**抓取时间**: 2026-04-15 00:05 UTC  
**类型**: X 推文线程/深度技术文章  
**标签**: agent-harness, harness-engineering, context-engineering, agent-architecture, llm-infrastructure, production-agents, agent-components, verification-loops

---

## 📊 一句话总结

深度解析 Agent Harness 的 12 个核心组件（编排循环/工具/记忆/上下文管理/状态持久化/错误处理/防护栏等），对比 Anthropic/OpenAI/LangChain 实现，揭示从状态less LLM 到生产级 agent 的完整基础设施，证明改变仅 harness 可提升 20+ 排名位置。

---

## 🏷️ 话题标签

#AgentHarness #HarnessEngineering #ContextEngineering #Agent 架构 #LLM 基础设施 #生产 Agent #Agent 组件 #验证循环

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:12 组件全景图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
12 Agent Harness Components infographic showing complete architecture.

Layout: Circular 12-component diagram around central LLM.

Color Palette:
- Components: Rainbow gradient
- Center LLM: Purple (#8B5CF6)
- Background: Dark gradient

Center — LLM Model 🟣:
图标：大脑
"Raw LLM"
"CPU with no RAM/disk/I/O"
"Context window = RAM"
"External DB = Disk"
"Tools = Device drivers"

12 Components (clockwise):

1. Orchestration Loop 🔴:
"TAO/ReAct cycle"
"Assemble→Call→Parse→Execute→Feed back"
"Dumb loop, intelligence in model"

2. Tools 🟠:
"Agent's hands"
"Schemas injected into context"
"Registration/validation/execution"

3. Memory 🟡:
"Short-term: conversation history"
"Long-term: across sessions"
"Three-tier hierarchy"

4. Context Management 🟢:
"Combat context rot"
"Compaction/Masking/JIT retrieval"
"Smallest high-signal token set"

5. Prompt Assembly 🔵:
"System+Tools+Memory+History+Message"
"Hierarchical priority stack"

6. Output Classification 🟣:
"Text vs Tool calls vs Handoff"
"Native tool calling"

7. State Persistence 🟤:
"Typed dictionaries through graph"
"Checkpointing at boundaries"
"Resume after interruptions"

8. Error Handling ⚫:
"4 error types"
"Transient/LLM-recoverable/User-fixable/Unexpected"
"Retry with backoff"

9. Guardrails ⚪:
"Input/Output/Tool guardrails"
"Tripwire mechanism"
"Permission enforcement"

10. Verification 🟤:
"Rules-based feedback"
"Visual feedback"
"LLM-as-judge"
"2-3x quality improvement"

11. Subagents 🟡:
"Fork/Teammate/Worktree"
"Agents-as-tools/Handoffs"
"Nested state graphs"

12. Termination 🟢:
"Layered conditions"
"Max turns/Token budget/User interrupt"

Bottom Insight:
"Change only harness → 20+ ranking positions"
"10-step 99% per-step = 90.4% end-to-end"
"Harness = OS for LLM"

Style: Modern component diagram, dark mode with rainbow components
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 12 个 Harness 组件的内容，环形图直接展示所有组件围绕 LLM 的架构，比单一架构图更能传达"完整系统"的价值。

---

### 选项 2：7 个架构选择对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
7 Harness Architecture Choices comparison diagram.

Layout: 7 horizontal choice cards with tradeoffs.

Color Palette:
- Choice headers: Blue gradient
- Options: Green vs Red contrast
- Background: Dark gradient

Choice 1 — Single vs Multi-Agent 🔵:
"Maximize single agent first"
"Split when: >10 overlapping tools or separate domains"
"Multi-agent adds: routing overhead, context loss"

Choice 2 — ReAct vs Plan-and-Execute 🟠:
"ReAct: Reason+Action interleaved (flexible, higher cost)"
"Plan-and-execute: Separate planning from execution"
"LLMCompiler: 3.6x speedup over sequential ReAct"

Choice 3 — Context Management 🟡:
"5 approaches: Time-based/Summarization/Masking/Note-taking/Delegation"
"ACON: 26-54% token reduction, 95%+ accuracy"
"Prioritize reasoning traces over raw outputs"

Choice 4 — Verification Loop 🟢:
"Computational: tests/linters (deterministic)"
"Inferential: LLM-as-judge (semantic, adds latency)"
"Guides (feedforward) vs Sensors (feedback)"

Choice 5 — Permission Architecture 🔴:
"Permissive: fast but risky"
"Restrictive: safe but slow"
"Depends on deployment context"

Choice 6 — Tool Scoping 🟣:
"More tools = worse performance"
"Vercel removed 80% tools → better results"
"Claude Code: 95% context reduction via lazy loading"
"Minimum tool set for current step"

Choice 7 — Harness Thickness 🟤:
"Thin: logic in model (Anthropic bet)"
"Thick: explicit control (Graph frameworks)"
"Delete planning as models internalize"

Bottom Insight:
"Identical models, different harnesses → wildly different performance"
"TerminalBench: harness change → 20+ ranking positions"
"Harness = where hard engineering lives"

Style: Clean technical choices, dark mode with choice colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：Von Neumann 架构类比

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "LLM as Von Neumann Architecture".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Various component colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"LLM = Von Neumann Architecture"
"Harness = Operating System"
Icon: CPU + OS

M2 — Raw LLM:
"CPU with no RAM"
"No disk, no I/O"
"Context window = RAM (fast but limited)"
"External DB = Disk (large but slow)"

M3 — Tools:
"Device drivers"
"Claude Code: 6 categories"
"File/Search/Execution/Web/Code/Subagent"

M4 — 3 Engineering Levels:
"Prompt Engineering: Instructions"
"Context Engineering: What model sees"
"Harness Engineering: Complete system"

M5 — 12 Components:
"Orchestration/Tools/Memory/Context"
"Prompt/Output/State/Error/Guardrails"
"Verification/Subagents/Termination"

M6 — Key Insight:
"If you're not the model, you're the harness"
"Change only harness → 20+ rankings"
"Harness = where hard engineering lives"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### Harness 定义

> **Harness 是包裹 LLM 的完整软件基础设施：编排循环/工具/记忆/上下文管理/状态持久化/错误处理/防护栏。**

**Anthropic 的 Claude Code 文档简单说**: SDK 是"为 Claude Code 提供动力的 agent harness"。

**OpenAI 的 Codex 团队用相同框架**，明确将术语"agent"和"harness"等同，指使 LLM 有用的非模型基础设施。

---

### 经典公式

> **"If you're not the model, you're the harness."** — LangChain 的 Vivek Trivedy

---

### Agent vs Harness 区别

| 概念 | 定义 |
|------|------|
| **Agent** | 涌现行为：目标导向/使用工具/自纠正实体，用户交互的 |
| **Harness** | 产生该行为的机械装置 |

> **当有人说"我建了个 agent"，他们意思是他们建了个 harness 并指向模型。**

---

### Von Neumann 架构类比

Beren Millidge 在 2023 年文章中精确化这个类比：

| 组件 | LLM 对应 |
|------|----------|
| **CPU** | Raw LLM |
| **RAM** | 上下文窗口（快但有限） |
| **Disk** | 外部数据库（大但慢） |
| **I/O** | 工具集成 |
| **OS** | Harness |

> **"我们已重新发明 Von Neumann 架构"，因为它是任何计算系统的自然抽象。**

---

## 三层工程

### Level 1: Prompt Engineering

**职责**:  crafting 模型接收的指令

---

### Level 2: Context Engineering

**职责**: 管理模型看到什么和何时看到

---

### Level 3: Harness Engineering

**职责**: 包含前两者，加完整应用基础设施：
- 工具编排
- 状态持久化
- 错误恢复
- 验证循环
- 安全执行
- 生命周期管理

> **Harness 不是 prompt 的包装器。它是使自主 agent 行为可能的完整系统。**

---

## 12 个生产 Agent Harness 组件

### Component 1: Orchestration Loop（编排循环）

**这是心跳**。它实现 Thought-Action-Observation (TAO) 循环，也称 ReAct 循环。

**循环运行**:
```
Assemble prompt → Call LLM → Parse output → Execute tool calls → Feed results back → Repeat until done
```

**机械上**: 通常只是 while 循环。复杂性存在于循环管理的一切，非循环本身。

**Anthropic 描述他们的 runtime 为"dumb loop"**，所有智能存在于模型中。Harness 只管理回合。

---

### Component 2: Tools（工具）

**工具是 agent 的手**。它们定义为 schemas（名称/描述/参数类型）注入 LLM 上下文，让模型知道可用什么。

**工具层处理**:
- 注册
- Schema 验证
- 参数提取
- 沙盒执行
- 结果捕获
- 格式化结果回 LLM 可读观察

**Claude Code 提供 6 类工具**:
1. 文件操作
2. 搜索
3. 执行
4. Web 访问
5. 代码智能
6. 子 agent 生成

**OpenAI 的 Agents SDK 支持**:
- 函数工具（通过 MCP）
- 托管工具（WebSearch/CodeInterpreter/FileSearch）
- MCP 服务器工具

---

### Component 3: Memory（记忆）

**记忆在多时间尺度操作**。

| 类型 | 说明 |
|------|------|
| **Short-term** | 单会话内的对话历史 |
| **Long-term** | 跨会话持久化 |

**实现对比**:

| 平台 | Long-term 实现 |
|------|---------------|
| **Anthropic** | Project files + 自动生成的 files |
| **LangGraph** | Namespace-organized JSON Stores |
| **OpenAI** | Sessions backed by SQLite or Redis |

**Claude Code 实现三层层级**:
1. **轻量索引**（~150 字符/条目，总是加载）
2. **详细主题文件**（按需拉取）
3. **原始转录**（仅通过搜索访问）

**关键设计原则**: agent 将自己的记忆视为"hint"，在行动前验证实际状态。

---

### Component 4: Context Management（上下文管理）

**这是许多 agent 静默失败的地方**。

**核心问题**: **Context rot** — 当关键内容落在窗口中间位置时模型性能降级 30%+（Chroma 研究，被 Stanford 的"Lost in the Middle"发现证实）。

**即使百万 token 窗口也遭受指令跟随降级随上下文增长。**

---

### 生产策略

| 策略 | 说明 |
|------|------|
| **Compaction** | 接近限制时总结对话历史（Claude Code 保留架构决策和未解决 bug，丢弃冗余工具输出） |
| **Observation masking** | JetBrains' Junie 隐藏旧工具输出同时保持工具调用可见 |
| **Just-in-time retrieval** | 维护轻量标识符并动态加载数据（Claude Code 用 grep/glob/head/tail 而非加载全文） |
| **Sub-agent delegation** | 每子 agent 广泛探索但只返回 1000-2000 token 压缩摘要 |

**Anthropic 的上下文工程指南陈述目标**: 找到最小可能的高信号 token 集，最大化期望结果的似然。

---

### Component 5: Prompt Assembly（提示组装）

**这组装模型实际每步看到的**。它是层级的：

```
System prompt → Tool definitions → Memory files → Conversation history → Current user message
```

**OpenAI 的 Codex 用严格优先级栈**:
1. 服务器控制系统消息（最高优先级）
2. 工具定义
3. 开发者指令
4. 用户指令（级联 files，32 KiB 限制）
5. 对话历史

---

### Component 6: Output Classification（输出分类）

**现代 harnesses 依赖原生工具调用**，模型返回结构化 tool_calls 对象而非必须解析的自由文本。

**Harness 检查**:
- 有工具调用？→ 执行它们并循环
- 无工具调用？→ 那是最终答案
- 有 handoff 请求？→ 更新当前 agent 并重启

**结构化输出**: OpenAI 和 LangChain 都支持通过 Pydantic 模型的 schema 约束响应。

**传统方法**: RetryWithErrorOutputParser（回馈原始 prompt/失败完成/解析错误给模型）仍可用于边缘情况。

---

### Component 7: State Persistence（状态持久化）

**为什么重要**: 10 步过程每步 99% 成功率仍只有~90.4% 端到端成功率。**错误复合快。**

**实现对比**:

| 平台 | 策略 |
|------|------|
| **LangGraph** | 状态建模为 typed dictionaries 流经 graph 节点，reducers 合并更新。Checkpointing 在 super-step 边界，支持中断后恢复和时间旅行调试 |
| **OpenAI** | 4 个互斥策略：application memory / SDK sessions / server-side Conversations API / lightweight previous_response_id chaining |
| **Claude Code** | Git commits as checkpoints + progress files as structured scratchpads |

---

### Component 8: Error Handling（错误处理）

**LangGraph 区分 4 种错误类型**:

| 类型 | 处理 |
|------|------|
| **Transient** | 带 backoff 重试 |
| **LLM-recoverable** | 返回错误为 ToolMessage 让模型调整 |
| **User-fixable** | 中断获取人工输入 |
| **Unexpected** | 冒泡上用于调试 |

**Anthropic**: 在工具处理器内捕获失败并返回为错误结果保持循环运行。

**Stripe 的生产 harness**: 上限重试 attempts 为 2。

---

### Component 9: Guardrails（防护栏）

**OpenAI 的 SDK 实现三层**:

| 层级 | 运行时机 |
|------|----------|
| **Input guardrails** | 在第一个 agent 运行 |
| **Output guardrails** | 在最终输出运行 |
| **Tool guardrails** | 在每工具调用运行 |

**"Tripwire"机制**: 触发时立即停止 agent。

**Anthropic 架构上分离权限执行和模型推理**:
- 模型决定尝试什么
- 工具系统决定允许什么

**Claude Code 门控~40 个离散工具能力独立**，三阶段：
1. 项目加载时信任建立
2. 每工具调用前权限检查
3. 高风险操作明确用户确认

---

### Component 10: Verification（验证）

**这是玩具演示和生产 agent 的分隔线**。

**Anthropic 推荐 3 种方法**:

| 方法 | 说明 |
|------|------|
| **Rules-based feedback** | 测试/linters/类型检查器 |
| **Visual feedback** | 通过 Playwright 截图用于 UI 任务 |
| **LLM-as-judge** | 单独子 agent 评估输出 |

> **Boris Cherny（Claude Code 创建者）指出，给模型验证其工作的方法提高质量 2-3x。**

---

### Component 11: Subagents（子 Agent）

**Claude Code 支持 3 种执行模型**:

| 模型 | 说明 |
|------|------|
| **Fork** | 父上下文的 byte-identical 副本 |
| **Teammate** | 单独终端面板带基于文件的邮箱通信 |
| **Worktree** | 自己 git worktree，每 agent 隔离分支 |

**OpenAI 的 SDK 支持**:
- Agents-as-tools（专家处理有界子任务）
- Handoffs（专家接管完全控制）

**LangGraph 实现子 agents 为嵌套状态图**。

---

### Component 12: Termination（终止）

**终止条件是层级的**:

| 条件 | 说明 |
|------|------|
| 模型产生无工具调用的响应 | 循环结束 |
| 最大回合限制超出 | 强制终止 |
| Token 预算耗尽 | 强制终止 |
| Guardrail tripwire 触发 | 强制终止 |
| 用户中断 | 强制终止 |
| 安全拒绝返回 | 强制终止 |

> **简单问题可能需 1-2 回合。复杂重构任务可跨数十回合链数十工具调用。**

---

## 7 个架构选择

### Choice 1: Single-agent vs Multi-agent

> **Anthropic 和 OpenAI 都说：先最大化单 agent。**

**Multi-agent 系统增加开销**:
- 额外 LLM 调用用于路由
- 交接期间上下文丢失

**仅当分裂**:
- 工具过载超过~10 个重叠工具
- 或清晰分离任务域存在

---

### Choice 2: ReAct vs Plan-and-execute

| 方法 | 说明 |
|------|------|
| **ReAct** | 每步交错推理和行动（灵活但每步成本更高） |
| **Plan-and-execute** | 分离规划和执行 |

> **LLMCompiler 报告比顺序 ReAct 快 3.6x。**

---

### Choice 3: Context Window Management

**5 种生产方法**:
1. Time-based clearing
2. Conversation summarization
3. Observation masking
4. Structured note-taking
5. Sub-agent delegation

> **ACON 研究显示 26-54% token 减少同时保持 95%+ 准确率，通过优先推理 traces 超过原始工具输出。**

---

### Choice 4: Verification Loop Design

| 类型 | 说明 |
|------|------|
| **Computational** | 测试/linters（确定性地面真相） |
| **Inferential** | LLM-as-judge（捕获语义问题但增加延迟） |

**Martin Fowler 的 Thoughtworks 团队框架为**:
- **Guides**（feedforward，行动前引导）
- **Sensors**（feedback，行动后观察）

---

### Choice 5: Permission and Safety Architecture

| 类型 | 说明 |
|------|------|
| **Permissive** | 快但有风险，自动批准大多数行动 |
| **Restrictive** | 安全但慢，每行动需批准 |

**选择取决于部署上下文。**

---

### Choice 6: Tool Scoping Strategy

> **更多工具通常意味着更差性能。**

| 案例 | 结果 |
|------|------|
| **Vercel** | 从 v0 移除 80% 工具 → 更好结果 |
| **Claude Code** | 通过 lazy loading 实现 95% 上下文减少 |

**原则**: 暴露当前步骤需要的最小工具集。

---

### Choice 7: Harness Thickness

| 类型 | 说明 |
|------|------|
| **Thin** | 逻辑在模型中（Anthropic 押注） |
| **Thick** | 显式控制（Graph 框架押注） |

> **Anthropic 随新版本内部化该能力定期从 Claude Code harness 删除规划步骤。**

---

## Harness 实现对比

### Anthropic's Claude Agent SDK

**暴露 harness 通过单一 `query()` 函数**，创建 agent 循环并返回流消息的 async iterator。

**Runtime 是"dumb loop"**。所有智能存在于模型中。

**Claude Code 用 Gather-Act-Verify 循环**:
```
Gather context (search files, read code)
→ Take action (edit files, run commands)
→ Verify results (run tests, check output)
→ Repeat
```

---

### OpenAI's Agents SDK

**通过 Runner 类实现 harness**，三模式：async / sync / streamed。

**SDK 是"code-first"**：工作流逻辑用原生 Python 表达而非 graph DSLs。

**Codex harness 扩展为三层架构**:
1. **Codex Core**（agent code + runtime）
2. **App Server**（bidirectional JSON-RPC API）
3. **Client surfaces**（CLI / VS Code / web app）

> **所有表面共享相同 harness，这就是为什么"Codex 模型在 Codex 表面上感觉比通用聊天窗口更好"。**

---

### LangGraph

**建模 harness 为显式状态图**。

**两个节点**（`llm_call` 和 `tool_node`）通过条件边连接：
- 如果有工具调用 → 路由到 `tool_node`
- 如果无 → 路由到 `END`

**LangGraph 从 LangChain 的 AgentExecutor 演化**，在 v0.2 弃用因为难扩展且缺少多 agent 支持。

**LangChain 的 Deep Agents 明确用"agent harness"术语**：内置工具/规划（`write_todos` 工具）/文件系统用于上下文管理/子 agent 生成/持久记忆。

---

### CrewAI

**实现基于角色的多 agent 架构**:

| 组件 | 说明 |
|------|------|
| **Agent** | LLM 周围的 harness，定义为 role/goal/backstory/tools |
| **Task** | 工作单元 |
| **Crew** | agent 集合 |

**CrewAI 的 Flows 层添加** "deterministic backbone with intelligence where it matters"，管理路由和验证而 Crews 处理自主协作。

---

### AutoGen (Microsoft Agent Framework)

**开创对话驱动编排**。

**三层架构**（Core / AgentChat / Extensions）支持 5 种编排模式：
1. Sequential
2. Concurrent (fan-out/fan-in)
3. Group chat
4. Handoff
5. Magentic（manager agent 维护动态任务 ledger 协调专家）

---

## Scaffolding 隐喻

> **Scaffolding 隐喻不是装饰性的。它是精确的。**

**建筑 Scaffolding 是临时基础设施**，使工人能建他们否则够不到的结构。它不做建造。但无它，工人够不到上层。

**关键洞察**: **Scaffolding 在建筑完成时移除。随模型改进，harness 复杂性应减少。**

**案例**: Manus 在 6 个月内重建 5 次，每次重写移除复杂性。复杂工具定义变为通用 shell 执行。"管理 agents"变为简单结构化 handoffs。

---

### 共同进化原则

> **模型现在用特定 harnesses 在循环中进行后训练。Claude Code 的模型学会使用它训练的具体 harness。改变工具实现可降级性能因为这种紧密耦合。**

**Harness 设计的"future-proofing test"**: 如果性能随更强大模型扩展无需增加 harness 复杂性，设计是可靠的。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Harness 组件数 | 12 |
| 架构选择数 | 7 |
| 仅 harness 改变排名提升 | 20+ 位置 |
| 10 步 99% 每步成功率 | 90.4% 端到端 |
| Context rot 性能降级 | 30%+ |
| ACON token 减少 | 26-54% |
| ACON 准确率保持 | 95%+ |
| LLMCompiler vs ReAct 加速 | 3.6x |
| 验证质量提升 | 2-3x |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "If you're not the model, you're the harness" | 核心区分 |
| "Harness = OS for LLM" | Von Neumann 类比 |
| "Context rot: 30%+ degradation" | 上下文管理重要性 |
| "Verification improves 2-3x" | 验证价值 |
| "Next time agent fails, don't blame model. Look at harness." | 核心洞察 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **12 组件架构** — 完整生产 agent 基础设施
2. **上下文管理** — 对抗 context rot 的 4 策略
3. **错误处理** — 4 类型错误分类
4. **验证循环** — 2-3x 质量提升
5. **7 架构选择** — 单 vs 多/ReAct vs Plan/上下文/验证/权限/工具/harness 厚度
6. **Scaffolding 隐喻** — 随模型改进移除复杂性
7. **共同进化** — 模型+harness 紧密耦合

### 可实施
- 实现 12 组件完整架构
- 用 compaction/masking/JIT 管理上下文
- 分类错误并适当处理
- 添加计算+推理验证循环
- 从单 agent 开始最大化
- 最小化工具集暴露
- 随模型改进删除 harness 复杂性

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Akshay Pachaar 原文 | https://x.com/akshay_pachaar/status/2041146899319971922 |
| Beren Millidge Essay | 2023 年 Von Neumann 架构文章 |
| LangChain TerminalBench | 排名从 30 外到第 5 |
| ACON Research | 26-54% token 减少 |

---

*原始来源：https://x.com/akshay_pachaar/status/2041146899319971922*
