# Harrison Chase — Your Harness, Your Memory

**来源**: https://x.com/hwchase17/status/2042978500567609738  
**作者**: Harrison Chase (@hwchase17) — LangChain 创始人  
**抓取时间**: 2026-04-12 18:12 UTC  
**类型**: X 推文线程/深度分析  
**标签**: agent-harness, agent-memory, open-source, vendor-lockin, langchain, deep-agents, mcp, context-engineering, memory-ownership, stateful-agents

---

## 📊 一句话总结

Harrison Chase 深度分析 Agent Harness 与 Memory 的紧密关系，警告使用封闭 Harness（尤其是专有 API 后）会将 Agent 记忆控制权让渡给第三方造成锁定，主张 Harness 和 Memory 应该开放可自托管，对比 OpenAI Responses API/Anthropic 服务器端压缩/Codex 加密压缩摘要等锁定风险，推出 Deep Agents 平台实现开源/模型无关/开放标准/可自托管。

---

## 🏷️ 话题标签

#AgentHarness #AgentMemory #开源 #供应商锁定 #LangChain #DeepAgents #MCP #上下文工程 #记忆所有权 #有状态 Agent

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：封闭 vs 开放 Harness 对比图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Technical comparison diagram for "Closed Harness vs Open Harness — Memory Ownership".

Layout: Side-by-side comparison showing memory flow and ownership.

Color Palette:
- Closed Harness: Red (#EF4444)
- Open Harness: Green (#10B981)
- Memory: Purple (#8B5CF6)
- Background: Dark gradient

Left — Closed Harness (Red):
图标：API 锁
"Memory behind API"
"You don't own memory"
"Cannot swap models + resume threads"
"Non-transferrable between harnesses"

Examples:
- OpenAI Responses API
- Anthropic server-side compaction
- Claude Agent SDK (closed source)
- Codex encrypted compaction summary

Risk Levels:
🟡 Mildly Bad: Stateful API stores state on their server
🟠 Bad: Closed harness, memory shape unknown
🔴 Worst: Whole harness + long-term memory behind API

Right — Open Harness (Green):
图标：开放数据库
"You own your memory"
"Swap models freely"
"Transfer between harnesses"
"Build proprietary dataset"

Examples:
- Deep Agents (open source)
- Model agnostic
- Open standards (MCP)
- Self-hostable
- Bring your own database (Postgres/Redis)

Bottom — Key Insight:
"Memory = proprietary dataset of user interactions"
"Without memory: agents easily replicable"
"With memory: differentiated + sticky experience"
"Model providers incentivized to lock in via memory"

Badge:
"Harness = Memory" | "Open Standards" | "Own Your Data"

Style: Clean technical comparison, dark mode with red/green contrast
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于封闭 vs 开放 Harness 对比的内容，并排对比图直接展示记忆所有权差异和锁定风险等级，比单一架构图更精准传达"为什么需要开放 Harness"的核心论点。

---

### 选项 2：Harness 演进时间线

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Agent Harness Evolution timeline showing 3 years of change.

Layout: Horizontal timeline from 2023 to 2026.

Color Palette:
- 2023: Blue (#3B82F6)
- 2024: Purple (#8B5CF6)
- 2025: Green (#10B981)
- 2026: Orange (#F97316)
- Background: Dark gradient

2023 — Simple RAG Chains:
"ChatGPT came out"
"All you could do: simple RAG"
"Models: basic capability"

2024 — Complex Flows:
"Models got a little better"
"Could create more complex flows"
"More scaffolding needed"

2025 — Agent Harnesses:
"Models got a lot better"
"New scaffolding type: harnesses"
"Examples: LangChain, Letta, OpenClaw..."

2026 — Memory + Harness Tied:
"Harnesses not going away"
"Memory = core harness capability"
"Open vs Closed battle"

Center Insight:
"Scaffolding needed in 2023 no longer needed"
"Replaced by other types of scaffolding"
"Even best model makers investing heavily in harnesses"

Bottom — Evidence:
"Claude Code source code leaked → harness code revealed"
"Web search in APIs = lightweight harness behind API"
"Memory isn't a plugin, it's the harness"

Badge:
"3 Years Evolution" | "Harnesses Here to Stay"

Style: Modern timeline infographic, dark mode with gradient timeline
Aspect ratio: 9:16 portrait
```

---

### 选项 3：记忆锁定风险金字塔

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Memory Lock-in Risk Pyramid showing 3 levels of risk.

Layout: Vertical 3-tier pyramid from mild to worst.

Color Palette:
- Tier 1: Yellow (#FBBF24)
- Tier 2: Orange (#F97316)
- Tier 3: Red (#EF4444)
- Background: Dark gradient

Tier 1 (Top) — Mildly Bad:
"Stateful API"
"Stores state on their server"
"Cannot swap models + resume threads"

Examples:
- OpenAI Responses API
- Anthropic server-side compaction

Tier 2 (Middle) — Bad:
"Closed harness"
"Memory shape unknown"
"Non-transferrable between harnesses"

Examples:
- Claude Agent SDK (closed source)
- Client-side artifacts shape unknown

Tier 3 (Bottom) — Worst:
"Whole harness + long-term memory behind API"
"Zero ownership or visibility"
"No control over what's exposed"

Examples:
- Full API-locked platforms
- Encrypted compaction summaries

Center Badge:
"Memory = proprietary dataset"
"Without memory: easily replicable"
"With memory: differentiated + sticky"

Bottom — Solution:
"Open Harness" | "Own Your Memory" | "Model Agnostic"
"Deep Agents: Open source + MCP + Self-hostable"

Style: Technical pyramid diagram, dark mode with tier colors
Aspect ratio: 9:16 portrait
```

---

## 核心论点

### Harness 不会消失

** sentiment**: 有时有人认为模型会吸收越来越多 scaffolding，Harness 将消失。

**现实**: 
- 2023 年需要的 scaffolding 不再需要
- 但被其他类型 scaffolding 替代
- Agent 定义 = LLM 与工具/数据源交互
- 总会有系统围绕 LLM 促进这种交互

**证据**:
> Claude Code 源代码泄露时，有 harness 代码。即使是世界最佳模型制造者也在大量投资 harnesses。

**Web Search 例子**:
- 内置于 OpenAI/Anthropic API 的 Web Search
- 不是"模型一部分"
- 是轻量级 harness 在 API 后编排模型与 Web Search API（仅通过工具调用）

---

### Memory = Harness 核心能力

引用 Sarah Wooders 文章《Why memory isn't a plugin (it's the harness)》:

> 要求把 memory 插入 agent harness 就像要求把驾驶插入汽车。管理上下文，因此 memory，是 agent harness 的核心能力和责任。

**Harness 如何管理 Memory**:
| 问题 | 示例 |
|------|------|
| 系统提示加载 | `.clauderc` / `.agents.md` 如何加载到上下文？ |
| 技能元数据展示 | 在系统提示中？在系统消息中？ |
| 自修改指令 | agent 能否修改自己系统指令？ |
| 压缩生存 | 什么在压缩后生存，什么丢失？ |
| 交互存储 | 交互是否存储并可查询？ |
| 记忆元数据 | 如何呈现给 agent？ |
| 工作目录 | 当前工作目录如何表示？ |
| 文件系统信息 | 多少暴露给 agent？ |

---

### Memory 现状

**Memory 处于婴儿期**:
- 长期记忆通常不是 MVP 部分
- 先让 agent 一般工作，然后担心个性化
- 仍在 figuring out memory
- 没有知名或通用的 memory 抽象

**Sarah Wooders**:
> "Ultimately, how the harness manages context and state in general is the foundation for agent memory."

---

## 锁定风险等级

### 🟡 Mildly Bad: Stateful API

**问题**: 使用有状态 API（如 OpenAI Responses API 或 Anthropic 服务器端压缩）

**后果**:
- 状态存储在他们服务器上
- 如果想切换模型并恢复先前线程 → 不再可行

---

### 🟠 Bad: Closed Harness

**问题**: 使用封闭 Harness（如 Claude Agent SDK，底层用 Claude Code，不开源）

**后果**:
- Harness 以未知方式与记忆交互
- 可能创建一些客户端工件
- 但这些工件形状是什么？Harness 应如何使用？
- 未知，因此不可转移

---

### 🔴 Worst: Full API Lock-in

**问题**: 整个 Harness（包括长期记忆）在 API 后

**后果**:
- 零所有权或可见性
- 不知道 Harness（因此不知道如何使用记忆）
- 甚至不拥有记忆！
- 可能部分通过 API 暴露，可能完全不 — 无控制权

**含义**:
> 当人们说"模型会吸收越来越多 harness" — 这就是他们真正意思。他们指这些记忆相关部分将进入模型供应商提供的 API 后。

---

## 为什么供应商要锁定

### 激励机制

**模型供应商强烈激励这样做**:
- Memory 重要，创造他们从模型得不到的锁定
- 已经开始行动

**例子**:
| 供应商 | 锁定机制 |
|--------|----------|
| **Anthropic** | 推出全 API 锁定平台 |
| **OpenAI** | Codex 开源但生成加密压缩摘要（不可在 OpenAI 生态外使用） |

---

### Memory 的价值

**为什么 Memory 创造锁定**:
- 允许 agent 在用户交互时变好
- 允许构建数据飞轮
- 允许 agent 个性化到每个用户
- 构建适应用户欲望和使用模式的 agent 体验

**关键洞察**:
> 没有 memory，你的 agent 容易被任何有相同工具访问的人复制。
> 
> 有 memory，你构建专有数据集 — 用户交互和偏好数据集。这专有数据集允许你提供差异化且越来越智能的体验。

---

### 切换成本对比

| 场景 | 切换难度 | 原因 |
|------|----------|------|
| **无状态模型** | 容易 | 相似/相同 API，只需微调提示 |
| **有状态（带 Memory）** | 困难 | 记忆重要，切换就失去访问权 |

---

## Harrison 的个人故事

### 被删除的 Email Assistant

**背景**:
- 内部 email assistant
- 基于 Deep Agents 模板构建
- 平台内置 memory

**过程**:
- 几个月交互 → agent 建立记忆
- 几周前，agent 被意外删除
- 尝试从相同模板创建新 agent

**结果**:
> 体验如此更差。必须重新教它所有偏好、语气、一切。

**洞察**:
> 这件事让我意识到 memory 可以多么强大和粘性。

---

## 解决方案：Deep Agents

### 核心特性

| 特性 | 说明 |
|------|------|
| **开源** | 代码完全开放 |
| **模型无关** | 可切换任何模型供应商 |
| **开放标准** | 使用 MCP 等开放标准 |
| **插件支持** | Postgres/Redis 等记忆存储插件 |
| **可部署** | Docker 自托管/任何云/自带数据库 |

### 为什么 Deep Agents

> 为了拥有你的记忆，你需要使用开放 Harness。

**核心主张**:
- Memory（因此 Harness）应与模型供应商分离
- 应该想要尝试任何最适合用例的模型的选择权
- 模型供应商被激励通过记忆创造锁定

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Harness 演进年数 | 3 年（2023-2026） |
| 锁定风险等级 | 3 级（Mildly Bad/Bad/Worst） |
| Deep Agents 特性 | 5 个（开源/模型无关/开放标准/插件/可部署） |
| 支持数据库 | Postgres/Redis/其他 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Harnesses are not going away" | Harness 永久存在 |
| "Memory isn't a plugin, it's the harness" | Memory 是 Harness 核心 |
| "If you use closed harness, you don't own your memory" | 锁定警告 |
| "Without memory, agents easily replicable" | Memory 差异化价值 |
| "Memory needs to be opened, owned by you" | 核心主张 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Harness-Memory 绑定** — 记忆是 Harness 核心能力非插件
2. **开放标准优先** — 使用 MCP 等开放标准避免锁定
3. **可自托管** — 完全控制记忆存储和格式
4. **模型无关** — 可自由切换最佳模型
5. **专有数据集价值** — 用户交互和偏好创造差异化
6. **记忆所有权** — 确保完全拥有和控制记忆

### 可实施
- 确保记忆文件格式开放可读
- 使用开放标准（如 MCP）集成工具
- 支持自托管部署选项
- 保持模型供应商可切换性
- 追踪用户交互和偏好建立专有数据集
- 定期备份记忆防止意外丢失

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Harrison Chase 原文 | https://x.com/hwchase17/status/2042978500567609738 |
| Sarah Wooders 文章 | Why memory isn't a plugin (it's the harness) |
| Deep Agents | 文中提及（Harrison 的公司） |
| Letta | @Letta_AI（Sarah Wooders 的公司） |
| LangChain | https://github.com/langchain-ai/langchain |

---

*原始来源：https://x.com/hwchase17/status/2042978500567609738*
