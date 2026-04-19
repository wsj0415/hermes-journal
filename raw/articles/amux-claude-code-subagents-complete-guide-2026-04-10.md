# Claude Code Subagents — 完整指南

**来源**: https://amux.io/guides/claude-code-subagents/  
**抓取时间**: 2026-04-10 05:42 UTC  
**类型**: 技术指南  
**标签**: claude-code, subagents, ai-agents, context-isolation, parallel-execution, code-review, amux, prompt-engineering, multi-agent-systems, developer-tools

---

## 📊 一句话总结

这篇指南详细解释了 Claude Code Subagents 是什么（一次性无记忆同事）、何时使用（上下文隔离/专业化工作）、何时避免（单文件读取/多写入冲突）、如何编写（YAML frontmatter + 精简系统提示）、5 个生产就绪示例、并行运行方法，以及与 amux 多会话的区别和组合使用策略。

---

## 🏷️ 话题标签

#ClaudeCode #Subagents #AI 代理 #上下文隔离 #并行执行 #代码审查 #amux #提示工程 #多代理系统 #开发者工具

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Subagent 架构对比图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a clean technical architecture infographic for "Claude Code Subagents — Complete Guide".

Title: "Claude Code Subagents"
Subtitle: "一次性无记忆同事"

Layout: Vertical flow showing parent → subagent delegation with context isolation.

Color Palette:
- Parent: Blue (#3B82F6)
- Subagent: Purple (#8B5CF6)
- Context: Green (#10B981)
- Background: Dark gradient (#0F172A to #1E293B)
- Text: White

Top Section - Core Concept:

图标：大脑 + 隔离墙
"上下文隔离"
"专业化工作"
"一个总结返回"

Middle Section - Delegation Flow:

[Parent Session] 父会话
"主上下文"
"协调者"
     ↓ Task 工具
[Subagent] 子代理
"新鲜上下文"
"专业化系统提示"
"可选限制工具"
     ↓ 返回
[One Summary] 一个总结
"父上下文仅增长 200 token"
"而非 8000 token"

Bottom Section - 5 Examples:

1. Code Reviewer — "写完代码后用"
2. Explorer — "开放代码库问题"
3. Test Writer — "添加/扩展测试"
4. Migration Planner — "非平凡迁移规划"
5. Security Auditor — "安全审查只读"

Right Side - Comparison:

Subagents vs Parallel Sessions:
| 维度 | Subagents | amux 会话 |
|------|-----------|----------|
| 生命周期 | 秒 - 分钟 | 分钟 - 小时 |
| 目标 | 上下文卫生 | 吞吐量倍增 |
| 协调 | 父同步协调 | 独立无父 |
| 文件冲突 | 高风险 | 零 (隔离分支) |

Badge:
"5 个生产示例"
"并行运行"
"反模式警告"
"与 amux 组合"

Style: Modern technical architecture diagram, dark mode with neon accents
Aspect ratio: 9:16 portrait
```

---

### 选项 2:5 个示例网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules for "5 Production-Ready Subagents".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Blue (#3B82F6)
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Claude Code Subagents"
"5 个生产就绪示例"
Icon: Robot + code

M2 — Code Reviewer:
"写完代码后用"
"Bug/安全/缺失测试"
"SHIP / FIX FIRST"

M3 — Explorer:
"开放代码库问题"
"探索多文件"
"简洁总结"

M4 — Test Writer:
"添加/扩展测试"
"匹配现有风格"
"运行测试套件"

M5 — Migration Planner:
"非平凡迁移"
"逐步计划"
"非代码"

M6 — Security Auditor:
"安全审查"
"只读访问"
"严重性分级"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 什么是 Claude Code Subagent？

**定义**: Claude Code subagent 是你定义为带 YAML frontmatter 的 markdown 文件的专业 AI 助手。父 Claude 会话可通过 `Task` 工具委托工作给它，subagent 在独立的新鲜上下文窗口中运行，有自己的系统提示和（可选）限制工具集，返回单个文本回复给父会话。

**核心价值**: 不是添加更多智能（subagents 使用与父会话相同的底层模型），而是**上下文隔离**：保持父会话专注，移交嘈杂或专业化工作，获得干净总结，继续工作。

### 上下文不对称

```
父会话                    Subagent
─────────                    ────────
"找到所有使用             ↓
 旧 auth helper 的地方"  ──>  [新鲜上下文]
                              Grep, Read, Read, Read...
                              (15 个工具调用，8KB 输出)
                              ↓
"在 4 个文件中找到 12 个  <──  [返回一个消息]
 调用点：..."
[父上下文增长 200           [subagent 上下文丢弃]
 token，而非 8000]
```

**这种不对称性** — 多内部步骤进，一个总结消息出 — 是整个价值主张。

---

## 心智模型：一次性无记忆同事

新手最常见的错误是将 subagents 视为有状态的长期助手。**它们不是**。每次调用：

- 从空上下文窗口开始
- 只看到系统提示 + 父会话传递的提示
- 无法读取先前对话、其他 subagents 输出或父会话之前做的事
- 返回一个最终消息并立即终止
- 跨调用无持久记忆

**把 subagent 想象成你拍肩膀的同事**："嘿，查一下 X 告诉我找到什么。"他们走开，做工作，带着答案回来，忘记整个互动。下次拍他们，是新人。

---

## Subagent 文件结构

Subagents 存在于两个位置之一：

- `.claude/agents/<name>.md` — 项目级，检入 git，团队共享
- `~/.claude/agents/<name>.md` — 用户级，个人，所有项目可用

**项目级在命名冲突上胜出**。两者都是带 YAML frontmatter 的纯 markdown：

```markdown
---
name: code-reviewer
description: 写完或修改代码后主动使用，捕获 bug、安全问题和风格问题。专注于防御性审查，提供具体修复建议。
tools: Read, Grep, Glob, Bash
model: sonnet
---

你是有二十年经验的高级代码审查员。

你的工作是审查父 agent 刚生成的 diff 并报告：

1. Bug 或逻辑错误（带 file:line 引用）
2. 安全问题（注入、auth 绕过、secret 泄露）
3. 风格和一致性问题
4. 新分支缺失的测试
5. 任何会阻止发布的内容

简洁。以严重性开头。跳过赞美。如果代码干净，用一句话说。
以结论结束：SHIP / FIX FIRST / NEEDS DISCUSSION。
```

### Frontmatter 字段

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | 是 | 小写，kebab-case。如何从 Task 工具调用它。 |
| `description` | 是 | **最重要字段**。Claude 读这个决定是否自动委托。具体说明_何时_使用它。 |
| `tools` | 否 | 逗号分隔列表。省略继承所有父工具。限制以保证安全（如研究者只获 Read+Grep）。 |
| `model` | 否 | 覆盖模型。用 `haiku` 做便宜查找，`opus` 做困难推理，或省略继承。 |

**frontmatter 下方的正文是系统提示**。它每次运行时加载到 subagent 上下文中，所以保持精简 — 这里的每个 token 每次调用都要付费。

---

## 委托如何工作

有两种方式调用 subagent：

### 1. 自动委托（父会话决定）

当你要求父 Claude 做某事时，它扫描可用 subagents 的 `description` 字段并决定是否匹配。如果 description 以"Use proactively when..."或"Use whenever..."开头，Claude 更可能在不被告知时主动使用它。**这就是为什么 description 是文件中最重要的字段** — 它字面上是路由信号。

### 2. 显式调用（你决定）

你可以告诉父会话："用 code-reviewer subagent 检查这个 diff"或"Spawn 三个 explorer subagents 并行映射代码库"。父会话然后发出命名 subagent 的 `Task` 工具调用。

```markdown
# 在你对父会话的提示中
"用 code-reviewer subagent 检查我刚做的更改"

# 父会话内部做什么
Task(subagent_type="code-reviewer", prompt="审查 src/auth.py 中的 diff 并报告发现")

# 你看到什么
[code-reviewer 报告：2 个 bug，1 个风格问题，修复后 SHIP]
```

---

## 5 个生产就绪 Subagent 示例

### 1. Code Reviewer（防御性第二双眼睛）

```markdown
---
name: code-reviewer
description: 写完或修改代码后主动使用。审查 diff 查找 bug、安全问题和缺失测试，带具体 file:line 引用。
tools: Read, Grep, Glob, Bash
---

你是高级代码审查员。阅读父会话指向你的 diff 或文件。
只报告：bug、安全问题、缺失测试、破坏性更改。
跳过赞美。使用 file:line 引用。以 SHIP / FIX FIRST / NEEDS DISCUSSION 结束。
```

---

### 2. Codebase Explorer（模式搜索不污染上下文）

```markdown
---
name: explorer
description: 当用户问关于代码库的开放性问题需要探索多文件时使用。返回简洁总结而非将原始文件内容转储到父上下文。
tools: Read, Grep, Glob
---

你是代码库导航员。探索项目回答父会话的问题。
阅读文件，grep 模式，跟踪导入。
返回一个总结消息：找到什么、在哪、影响。
从不粘贴大文件内容。只用 file:line 引用和 2 行摘录。
```

---

### 3. Test Writer（父会话不需要加载的专业化提示）

```markdown
---
name: test-writer
description: 当用户要求为特定模块或函数添加/扩展测试时使用。编写匹配项目现有测试风格的惯用测试。
tools: Read, Write, Edit, Bash, Grep
---

你编写匹配项目现有约定的测试。
写之前：阅读 2-3 个现有测试文件学习风格。
覆盖快乐路径、边缘情况和至少一个失败模式。
完成后运行测试套件。只返回：添加的文件、覆盖什么、通过/失败状态。
```

---

### 4. Migration Planner（重推理，单个答案）

```markdown
---
name: migration-planner
description: 当用户想规划非平凡迁移（框架升级、数据库 schema 更改、语言移植）时使用。产生逐步计划，非代码。
tools: Read, Grep, Glob
model: opus
---

你是迁移架构师。**不写代码**。产生计划。
阅读相关文件。识别风险、破坏性更改和排序约束。
输出：编号步骤列表、依赖图、每步预估风险、回滚策略。
```

---

### 5. Security Auditor（限制工具 = 安全边界）

```markdown
---
name: security-auditor
description: 当用户要求审查触碰 auth、secrets、用户输入或外部 API 的代码的安全审查时使用。只读 — 无法修改任何内容。
tools: Read, Grep, Glob
---

你是安全审计员。你故意只有**只读访问**。
查找：SQL 注入、XSS、命令注入、auth 绕过、secret 泄露、
不安全反序列化、缺失 authz 检查、IDOR、SSRF、开放重定向。
报告严重性（Critical / High / Medium / Low）带 file:line 和修复草图。
```

---

## 并行运行 Subagents

父 Claude 会话可以通过在同一响应中发出多个 `Task` 工具调用**并行**spawn 多个 subagents。它们都在各自的新鲜上下文窗口中并发执行，父会话在完成时接收所有结果。

```markdown
# 父会话一次发出三个 Task 调用：
Task(subagent_type="explorer", prompt="映射 auth 子系统")
Task(subagent_type="explorer", prompt="映射 billing 子系统")
Task(subagent_type="explorer", prompt="映射 notifications 子系统")

# 三个同时运行。父接收三个总结。
# 总墙钟时间：~最慢的一个，非总和。
```

**这是如何 30 秒而非 2 分钟扫描大代码库的方法** — 父上下文仅增长三个总结，而非每个 subagent 阅读的每个文件。

这是_一个 Claude Code 会话内_的并行。它不同于并发运行多个顶层 Claude Code 会话（下一节）。

---

## Subagents vs 并行 Claude Code 会话

最常见的困惑："如果我可以并行运行 subagents，为什么需要 amux 或多个 Claude Code 会话？"

**因为它们解决根本不同的问题**。

| 维度 | Subagents（一个会话内） | 并行会话（amux） |
|------|------------------------|-----------------|
| 生命周期 | 秒到几分钟 | 几分钟到小时，可过夜运行 |
| 目标 | 上下文卫生、专业化 | 墙钟吞吐量倍增 |
| 协调 | 父同步协调 | 独立会话，无父 |
| 文件系统 | 与父相同工作目录 | 每个会话独立 git worktree |
| 冲突风险 | 高如果多个 subagents 写入 | 零 — 隔离分支 |
| 可观察性 | 活在父转录中 | Web 仪表板 + 移动 PWA |
| 自愈 | 父死 subagents 死 | Watchdog 自动重启崩溃会话 |
| 输出 | 每个一个文本回复 | 完整 PRs、commits、branches |
| 最佳用途 | 查找、审查、规划 | 并行发布 10 个 ticket |

**经验法则**: 如果子任务短、 mostly 读取、反馈回父推理，用 subagent。如果子任务是自包含 ticket 以 commit 或 PR 结束，在它自己的 Claude Code 会话中运行。两者互补，非竞争。

---

## 浪费 Token 的反模式

### 1. 单行查找用 Subagents

如果只需读单个文件，父可一个工具调用完成。Spin up subagent 花费系统提示开销加委托往返。糟糕交易。

### 2. 多个 Subagents 写入相同文件

Subagents 共享父的工作目录。两个 subagents 同时编辑 `src/auth.py` 会互相覆盖 — 无 git worktree 隔离。如果两个工作单元触碰重叠文件，运行它们为独立 amux 会话在独立 worktrees，非并行 subagents。

### 3. 模糊描述

如果 description 是"helps with code"，父永远不会自动委托。让它命令式和具体："写完 Python 测试后主动使用验证它们实际运行并断言有意义的东西。" **Descriptions 是路由层**。

### 4. 臃肿系统提示

subagent 文件正文中的每个 token 每次调用都加载。3KB 系统提示调用 20 次是 60KB 上下文开销。**无情修剪**。

### 5. Subagents 试图成为父

如果 subagent 最终做 30 个工具调用、规划多步重构、要求澄清 — 它应该只是主会话，非 subagent。**Subagents 应专注：一个工作，一个返回值**。

### 6. 忽略"无记忆"规则

试图让 subagent"记住"先前调用发生的事会静默失败。在提示中传递任何需要的上下文，或使用真实持久层（board、notes、磁盘文件）。

---

## 编写实际被选中的 Subagent Descriptions

Description 字段是父和 subagent 之间的整个接口。Claude 读它，决定相关性，然后委托或不委托。**三条规则**：

### 以触发条件开头

以_何时_使用 subagent 开头，非_它是什么_。

```markdown
# 糟糕
description: 一个找 bug 和风格问题的代码审查员。

# 好
description: 用户写完或修改代码后主动使用。审查 diff 查找 bug、安全问题和缺失测试。
```

### 使用"use proactively"或"use whenever"这些词

这些短语偏置父向自动委托。没有它们，父通常等被问。

### 窄而非宽

做"通用代码事情"的 subagent 会随机被选。做"触碰 auth、secrets 或用户输入代码的安全审查"的 subagent 会在确切相关时被选。

---

## 结合 Subagents 与 amux 获得真实吞吐量

**最强设置使用两层**：

- **amux 在外层**: 10 个 Claude Code 会话在 10 个 git worktrees 并行运行，每个拥有 kanban board 的独立 ticket
- **Subagents 在内层**: 每个会话用 `code-reviewer` subagent 在 commit 前，`explorer` subagent 用于代码库问题，`test-writer` subagent 用于覆盖

**外层倍增墙钟吞吐量** — 你在一个时间内发布 10 个东西。**内层保持每个会话上下文干净和专业化**所以质量保持高。Subagents 防止每个会话淹没在自己的中间输出中；amux 防止你在顺序工作中淹没。

```bash
# 1. 定义可复用 code-reviewer subagent（检入 repo）
echo '---
name: code-reviewer
description: Commit 前主动使用。审查 diff 查找 bug 和缺失测试。
tools: Read, Grep, Bash
---
你是高级代码审查员。简洁。以严重性开头。以 SHIP / FIX FIRST 结束。
' > .claude/agents/code-reviewer.md

# 2. 推送 10 个 ticket 到 amux board
amux board add "为 auth/login.py 添加测试"
amux board add "迁移 api/users.py 到 async"
amux board add "修复 bug #423 — 重复通知"
# ...等

# 3. Spin up 10 个 amux 会话，每个在自己的 worktree
for i in $(seq 1 10); do
  amux register worker-$i --dir ../myproject --worktree --yolo
  amux start worker-$i
done

# 4. 每个 worker claim 一个 ticket，commit 前调用 code-reviewer subagent，
#    发布干净 PR — 全部并行。
```

---

## FAQ

### Subagents 与运行多个并行 Claude Code 会话如何不同？

Subagents 活在_一个_Claude Code 会话_内_。它们共享相同终端、相同工作目录，在一个父的协调下运行。多个并行 Claude Code 会话（amux 模型）是独立进程，有自己的 git worktrees、自己的仪表板， ability 运行数小时无父。**Subagents 最适合上下文卫生；并行会话最适合真实吞吐量倍增**。

### 何时应该用 subagent 而非直接做工作？

用 subagent 当 (1) 任务生成大量中间输出你不想要污染主上下文，(2) 它受益于专业化系统提示你不想要加载在主会话，或 (3) 你想并发运行多个查找。**不要为 trivial 读取用 subagent** — 委托开销超过收益。

### Subagents 可以调用其他 subagents 吗？

在当前版本，**不** — subagents 无法访问 Task 工具。视父为唯一协调者。如果发现想要嵌套委托，工作可能属于独立顶层 Claude Code 会话通过 amux 而非。

### Subagents 与父共享记忆吗？

**不**。每次调用从新鲜上下文窗口开始，仅由系统提示和父传入的提示播种。Subagents 无法看到先前工具结果、其他 subagents 输出或对话历史。

### Subagents 可以用什么工具？

你在 YAML frontmatter 的 `tools` 下列出的任何内容。**省略字段继承父的完整工具集**，或限制以保证安全（如研究 subagent 只获 `Read` 和 `Grep` — 它物理上无法修改文件）。

### 我在哪保存 subagent 文件？

项目级在 repo 的 `.claude/agents/`（检入 git，团队共享）或用户级在 `~/.claude/agents/`（个人，所有项目可用）。**项目级在命名冲突上胜出**。

### 应该用 subagents 还是 amux 做并行编码？

**两者**。会话内 subagents 用于上下文效率和并发查找。amux 会话外用于跨隔离 git worktrees 的真实并行吞吐量，带自愈、监控和每会话 token 追踪。**它们组合；它们不竞争**。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 生产示例 | 5 个 |
| Frontmatter 字段 | 4 个（name/description/tools/model） |
| 反模式 | 6 个 |
| Description 规则 | 3 条 |
| 并行 subagents | 支持 |
| 与 amux 组合 | 推荐 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "一次性无记忆同事" | 核心心智模型 |
| "上下文隔离" | 核心价值主张 |
| "Description 是路由层" | 最重要字段 |
| "两者组合；它们不竞争" | Subagents + amux |
| "无情修剪" | 系统提示建议 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **上下文隔离** — 专业化任务独立上下文
2. **Description 设计** — 触发条件开头 + "use proactively"
3. **工具限制** — 安全边界通过限制工具
4. **并行执行** — 多个子任务并发
5. **反模式避免** — 单行查找/多写入/臃肿提示

### 可实施
- 为内容创作任务定义 subagents（研究/审查/优化）
- 用 description 规则优化任务路由
- 限制敏感操作的工具访问
- 并行运行独立内容分析任务
- 避免反模式（精简系统提示）

---

## 相关资源

| 资源 | 链接 |
|------|------|
| amux GitHub | https://github.com/mixpeek/amux |
| Agentmaxxing 指南 | https://amux.io/guides/agentmaxxing/ |
| Scaling to 50 Agents | https://amux.io/guides/scaling-to-50-agents/ |

---

*原始来源：https://amux.io/guides/claude-code-subagents/*
