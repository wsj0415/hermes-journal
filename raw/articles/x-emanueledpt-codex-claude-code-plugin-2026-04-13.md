# Emanuele Di Pietro — 如何在 Claude Code 中使用 Codex

**来源**: https://x.com/emanueledpt/status/2038719718379700617  
**作者**: Emanuele Di Pietro (@emanueledpt)  
**抓取时间**: 2026-04-13 05:16 UTC  
**类型**: X 推文线程/插件教程  
**标签**: codex, claude-code, openai-plugin, code-review, adversarial-review, subagent, background-jobs, code-delegation

---

## 📊 一句话总结

OpenAI 发布官方 Codex 插件 for Claude Code，通过/codex:*斜杠命令调用 Codex 作为后台子 agent 进行代码审查/对抗性审查/完整编码任务委托，支持背景运行让你继续工作，6 个核心命令（review/adversarial-review/rescue/status/result/cancel）+ 审查门可选功能 + 配置指南。

---

## 🏷️ 话题标签

#Codex #ClaudeCode #OpenAI 插件 #代码审查 #对抗性审查 #子 Agent #后台任务 #代码委托

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Codex 插件命令全景图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Codex Plugin for Claude Command infographic showing 6 core commands.

Layout: 6 command cards with usage examples.

Color Palette:
- Review: Blue (#3B82F6)
- Adversarial: Red (#EF4444)
- Rescue: Green (#10B981)
- Status: Yellow (#FBBF24)
- Result: Purple (#8B5CF6)
- Cancel: Orange (#F97316)
- Background: Dark gradient

Command 1 — /codex:review 🔵:
"Read-only code review"
"Uncommitted changes"
"Severity: critical/high/medium/low"
"File paths + line numbers + confidence"
"--wait / --background / --base main"

Command 2 — /codex:adversarial-review 🔴:
"Design critique, harder"
"Questions design decisions"
"Tradeoffs? Assumptions? Production failures?"
"Accepts focus text after flags"
"--background look for race conditions"

Command 3 — /codex:rescue 🟢:
"Most powerful command"
"Delegate full coding task"
"Investigation/debugging/implementation"
"--model gpt-5.4-mini --effort medium"
"--background for multi-step"

Command 4 — /codex:status 🟡:
"Monitor background jobs"
"List all current/recent jobs"
"<job-id> full output"
"<job-id> --wait for completion"
"Shows: ID/kind/status/phase/time/summary"

Command 5 — /codex:result 🟣:
"Get completed job output"
"Verdict + summary + findings"
"File paths + line numbers + next steps"
"Includes Codex session ID for resume"

Command 6 — /codex:cancel 🟠:
"Cancel active background job"
"<job-id> optional"
"Stop long-running tasks"

Center Badge:
"Background subagent"
"Keep working while Codex does its thing"
"Uses local Codex CLI + existing limits"

Bottom Setup:
"1. /plugin marketplace add openai/codex-plugin-cc"
"2. /plugin install codex@openai-codex"
"3. /reload-plugins"
"4. /codex:setup"

Style: Modern command grid, dark mode with command colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Codex 插件 6 个核心命令的教程，命令网格图直接展示每个命令的用途和参数，比单一架构图更能传达"命令参考"的价值。

---

### 选项 2：工作流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Codex Plugin Workflow diagram showing Claude Code + Codex interaction.

Layout: Horizontal flow showing main workflow + subagent delegation.

Color Palette:
- Claude Code: Blue (#3B82F6)
- Codex Subagent: Green (#10B981)
- Background Jobs: Purple (#8B5CF6)
- Output: Yellow (#FBBF24)
- Background: Dark gradient

Left — Claude Code Main Workflow:
图标：终端窗口
"Handles main workflow"
"Your primary interface"
"Receives slash commands"
"/codex:review"
"/codex:rescue"
"/codex:adversarial-review"

Center — Plugin Bridge:
图标：桥梁
"Codex Plugin = Bridge"
"6 slash commands"
"Background subagent"
"Uses local Codex CLI"
"Counts toward existing limits"

Right — Codex Subagent:
图标：Codex Logo
"Runs in background"
"Code review (read-only)"
"Adversarial design critique"
"Full task delegation"
"Returns findings + session ID"

Bottom — Job Monitoring:
"/codex:status — List jobs"
"/codex:result — Get output"
"/codex:cancel — Stop job"
"Job ID / Kind / Status / Phase / Time / Summary"

Optional Feature — Review Gate:
"Auto-run Codex after every edit"
"Blocks Claude from finishing if issues found"
"Warning: Can create long loops, drain limits"
"Only enable when actively monitoring"

Style: Clean workflow diagram, dark mode with flow colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：安装与配置指南风格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "Codex Plugin Setup & Usage".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various feature colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Codex Plugin for Claude Code"
"OpenAI 官方插件"
Icon: Codex + Claude bridge

M2 — Prerequisites:
"Node.js 18.18.0+"
"ChatGPT account (Free/Paid)"
"或 OpenAI API key"
"2 min setup"

M3 — 4 Step Install:
"1. marketplace add openai/codex-plugin-cc"
"2. install codex@openai-codex"
"3. reload-plugins"
"4. codex:setup"

M4 — 6 Commands:
"review — Read-only review"
"adversarial-review — Design critique"
"rescue — Full task delegation"
"status/result/cancel — Job mgmt"

M5 — Config:
"~/.codex/config.toml (user)"
".codex/config.toml (project)"
"model = gpt-5.4-mini"
"reasoning_effort = low/medium/high/xhigh"

M6 — Best Practices:
"One task per run"
"Explicit success criteria"
"Specify output format"
"Avoid 'more reasoning' requests"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 什么是 Codex 插件

> **OpenAI 刚刚为 Claude Code 发布了官方 Codex 插件。**

**核心功能**:
- 运行代码审查
- 对抗性审查
- 委托完整编码任务给 Codex
- **无需离开终端**
- **一切作为后台子 agent 运行** — 你可以继续工作而 Codex 做它的事

---

### 插件架构

> **Codex 插件是两工具之间的桥梁。**

| 组件 | 职责 |
|------|------|
| **Claude Code** | 处理你的主工作流 |
| **Codex 插件** | 添加/codex:*斜杠命令集 |
| **Codex 子 Agent** | 后台运行代码审查/任务委托/设计审查 |

**技术细节**:
- 使用你本地 Codex CLI
- 计入现有 Codex 限制
- 适用于 ChatGPT Free/任何付费订阅/OpenAI API key

---

## 安装指南

### 前置条件

| 要求 | 说明 |
|------|------|
| **Node.js** | 18.18.0 或更高 |
| **认证** | ChatGPT 账户（Free 或付费）或 OpenAI API key |

---

### 四步安装

**Step 1: 添加市场源**
```bash
/plugin marketplace add openai/codex-plugin-cc
```

**Step 2: 安装插件**
```bash
/plugin install codex@openai-codex
```

**Step 3: 重载插件**
```bash
/reload-plugins
```

**Step 4: 运行设置**
```bash
/codex:setup
```

**设置检查**:
- Codex 是否安装和认证
- 如果 Codex 缺失且 npm 可用，自动提供安装
- 如果 Codex 已安装但未登录，提示`codex login`

---

### 手动安装 Codex（可选）

```bash
npm install -g @openai/codex
codex login
```

---

### 配置读取

插件从以下位置读取现有配置：

| 配置文件 | 作用域 |
|----------|--------|
| `~/.codex/config.toml` | 用户级 |
| `.codex/config.toml` | 项目级（仅当项目受信任时加载） |

**无需额外配置**（如果你已在使用 Codex）

---

## 6 个核心命令

### /codex:review — 代码审查

**功能**: 标准只读代码审查你的未提交更改

**作用域检查**: 插件先检查工作树估计范围，多文件更改建议在后台运行

**选项**:
```bash
/codex:review                    # 默认
/codex:review --wait             # 强制前台
/codex:review --background       # 强制后台
/codex:review --base main        # 与分支比较
```

**输出**:
- 严重性级别（critical / high / medium / low）
- 确切文件路径
- 行号
- 置信度分数

**特点**: **只读，不做任何更改**

---

### /codex:adversarial-review — 对抗性审查

**功能**: 与 review 相同，但可 steering 且更严格

**区别**:
| /codex:review | /codex:adversarial-review |
|--------------|--------------------------|
| 寻找缺陷 | 质疑设计决策 |
| 找 bug | 问：这是正确方法吗？ |
| | 问：错过了什么权衡？ |
| | 问：什么假设在生产中可能失败？ |

**选项**:
```bash
/codex:adversarial-review
/codex:adversarial-review --base main challenge whether this was 
  the right caching and retry design
/codex:adversarial-review --background look for race conditions 
  and question the chosen approach
```

**接受额外焦点文本**在标志后

**用途**: 当你想要设计审查而非仅缺陷审计

**特点**: **只读，不修复代码**

---

### /codex:rescue — 完整任务委托 ⭐ 最强大

**功能**: 委托完整编码任务给 Codex 作为后台子 agent

**适用**: 调查/调试/实现 — 任何多步骤你通常会花大量时间自己做的事

**示例**:
```bash
/codex:rescue investigate why the tests started failing
/codex:rescue fix the failing test with the smallest safe patch
/codex:rescue --resume apply the top fix from the last run
/codex:rescue --model gpt-5.4-mini --effort medium 
  investigate the flaky integration test
/codex:rescue --model spark fix the issue quickly
/codex:rescue --background investigate the regression
```

**自然语言也可**:
```
"Ask Codex to redesign the database connection to be more resilient."
```

**注意**:
- 不传`--model`或`--effort`，Codex 选自己默认
- `spark` 自动映射到`gpt-5.3-codex-spark`
- 开始前检查是否有上一会话的可恢复线程
- **小/有界请求用`--wait`**
- **多步骤用`--background`**

---

### /codex:status — 监控后台任务

**功能**: 监控你的后台作业

**选项**:
```bash
/codex:status                      # 列出所有当前和最近作业
/codex:status <job-id>             # 特定作业完整输出
/codex:status <job-id> --wait      # 等待作业完成
```

**输出显示**:
- Job ID
- Kind
- Status
- Phase
- Elapsed time
- Summary

---

### /codex:result — 获取完成作业输出

**功能**: 获取已完成作业的完整输出

**选项**:
```bash
/codex:result                      # 最近作业
/codex:result <job-id>             # 特定作业
```

**返回完整结果**:
- Verdict（判决）
- Summary（摘要）
- All findings with file paths and line numbers（所有发现带文件路径和行号）
- Next steps（下一步）
- **Codex session ID** — 可直接在 Codex 内用`codex resume <session-id>`恢复该运行

---

### /codex:cancel — 取消作业

**功能**: 取消活跃的后台作业

**选项**:
```bash
/codex:cancel                      # 取消当前作业
/codex:cancel <job-id>             # 取消特定作业
```

---

## 可选功能：审查门（Review Gate）

> **在每次 Claude Code 编辑后自动运行 Codex，在工作被视为完成前。**

**行为**:
- 如果 Codex 发现问题，不阻塞响应
- **但阻塞 Claude 完成，强制它先继续工作修复问题**

**启用/禁用**:
```bash
/codex:setup --enable-review-gate   # 启用
/codex:setup --disable-review-gate  # 禁用
```

---

### ⚠️ 警告

> **审查门可能创建长运行 Claude/Codex 循环，可能快速耗尽你的使用限制。仅当你计划主动监控会话时启用。**

---

## 配置指南

### 设置默认模型和推理努力

在`.codex/config.toml`中添加：

```toml
model = "gpt-5.4-mini"
model_reasoning_effort = "xhigh"
```

**推理努力选项**: `low` / `medium` / `high` / `xhigh`

---

### 配置文件位置

| 路径 | 作用域 | 说明 |
|------|--------|------|
| `~/.codex/config.toml` | 用户级 | 全局默认 |
| `.codex/config.toml` | 项目级 | 仅当项目受信任时加载 |

---

## 最佳实践

### 内部提示词指南关键原则

| 原则 | 说明 |
|------|------|
| **One task per run** | 将不相关请求拆分为独立调用 |
| **Define explicit success criteria** | 模糊请求得到模糊结果 |
| **Specify your output format** | 告诉它确切想要什么形状返回 |
| **Avoid asking for "more reasoning"** | 写更好合约而非要求更多推理 |

---

### 避免的反模式

| 反模式 | 问题 |
|--------|------|
| `"Let me know what you think"` | 太模糊 |
| **无输出合约** | Codex 不知道返回什么格式 |
| **混合多个不相关任务** | 在一个提示词中 |
| **要求猜测** | 当上下文缺失时 |

---

## 快速参考

### 发货前快速审查
```bash
/codex:review
```

###  handing 问题给 Codex
```bash
/codex:rescue investigate why the build is failing in CI
```

### 启动长运行任务
```bash
/codex:adversarial-review --background
/codex:rescue --background investigate the flaky test
```

### 然后检查
```bash
/codex:status
/codex:result
```

---

## 命令速查表

| 命令 | 功能 | 只读 |
|------|------|------|
| `/codex:review` | 未提交更改的只读审查 | ✅ |
| `/codex:adversarial-review` | 可 steering 设计审查和假设分析 | ✅ |
| `/codex:rescue` | 委托完整编码任务给 Codex | ❌ |
| `/codex:status` | 监控后台作业 | N/A |
| `/codex:result` | 获取已完成作业的完整输出 | N/A |
| `/codex:cancel` | 取消活跃作业 | N/A |

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Node.js 最低版本 | 18.18.0 |
| 核心命令数 | 6 |
| 推理努力选项 | 4 (low/medium/high/xhigh) |
| 审查门 | 可选功能 |
| 许可证 | Apache 2.0 |
| 仓库 | https://github.com/openai/codex-plugin-cc |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Background subagent" | 后台运行不阻塞 |
| "Keep working while Codex does its thing" | 并行工作流 |
| "One task per run" | 最佳实践 #1 |
| "Explicit success criteria" | 避免模糊请求 |
| "Review gate can create long loops" | 审查门警告 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **子 Agent 架构** — 后台运行不阻塞主工作流
2. **命令化接口** — 斜杠命令清晰分工
3. **作业监控** — status/result/cancel 完整生命周期管理
4. **审查门机制** — 自动质量控制（谨慎使用）
5. **配置分层** — 用户级 + 项目级配置
6. **自然语言 + 标志混合** — 灵活调用方式

### 可实施
- 为内容创作任务设计子 agent 委托机制
- 实现后台任务监控命令
- 添加内容质量审查门（可选）
- 支持用户级 + 项目级配置
- 提供自然语言 + 结构化参数混合调用

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Emanuele 原文 | https://x.com/emanueledpt/status/2038719718379700617 |
| GitHub 仓库 | https://github.com/openai/codex-plugin-cc |
| Codex 文档 | https://code.claude.com/docs |
| OpenAI Codex | https://openai.com/codex |

---

*原始来源：https://x.com/emanueledpt/status/2038719718379700617*
