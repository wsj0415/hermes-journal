---
title: 为 AI 代理和人类设计 CLI — 7 个设计模式
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [cli, agent-design, best-practice, ux]
sources: [raw/articles/cli-design-for-agents-and-humans.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

在 AI 代理时代，CLI 设计需要同时服务人类和代理。核心洞察：**"今年构建的每个 CLI 在某个时候都会被代理调用。大多数还没准备好。"** 问题：交互式提示、彩色输出、终端 UI 在自动化代理尝试解析结果的瞬间就崩溃了。解决方案：设计同时服务于两者的 CLI，无需维护两个独立代码库。推文数据：690👍 | 127🔁 | 117K👁️ | 1,142🔖（收藏率 165%）。

**来源**：Google Cloud Tech (@GoogleCloudTech)

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Google Cloud Tech 推文

---

## 核心哲学：数据与表现分离

```
┌─────────────────────────────────────────┐
│              CLI 引擎                    │
│    (内部逻辑，发射数据)                   │
└─────────────────┬───────────────────────┘
                  │
         ┌────────┴────────┐
         ↓                 ↓
   ┌──────────┐      ┌──────────┐
   │  人类     │      │   代理    │
   │  TUI     │      │  JSON    │
   │  可读格式  │      │  结构化   │
   └──────────┘      └──────────┘
```

**同一个 `watch` 命令应该**：
- 给人类：实时更新的 TUI
- 给代理：NDJSON 事件流

**你可以在不维护两个独立代码库的情况下实现这种无缝的双受众体验。**

---

## 7 个设计模式

### 1️⃣ 结构化可发现性

**入口点应该清晰映射功能。**

#### --help 优化

**分组命令** — 按功能分组，而非字母顺序：

```
❌ 字母顺序：
  add, config, delete, get, list, remove, update

✅ 功能分组：
  Task Management: add, delete, list
  Information: get, show
  Configuration: config, init
```

**明确标记入口点：**
```
Commands:
  init (start here)          Initialize a new project
  list (typical first step)  List all tasks
  get                        Get task details
```

#### 每个命令填充三个字段

| 字段 | 说明 | 示例 |
|------|------|------|
| **Short** | 一行摘要，5-10 词，以动词开头 | "List all tasks in current project" |
| **Long** | 详细说明：做什么、为什么用、与类似命令的区别 | "Lists all tasks with their current status. Use this to get an overview before drilling into specific tasks. Differs from 'show' which shows details of a single task." |
| **Example** | 3-5 个具体可复制粘贴的示例 | `cli list --status=pending`<br>`cli list --assignee=me`<br>`cli list --limit=10` |

**示例比描述更重要。** 开发者会在阅读前复制粘贴。代理会解析示例来推断标志模式。

#### 外部化代理指令

**可发现性超越 `--help`。**

**不要假设 LLM 原生知道如何使用你的工具 — 明确教它。**

**在仓库根目录发布 `AGENTS.md` 文件**：
- 定义参与规则
- 默认工作流
- 架构标准

**对于复杂命令，包含 `skills/` 目录**：
- 包含专用提示文件
- 外部代理可直接摄取

---

### 2️⃣ 代理优先互操作性

**CLI 必须是可解析和可预测的。**

#### --json 支持所有命令

**每个产生数据的命令都应该支持 `--json` 或 `--no-tui` 标志。**

```bash
# 人类使用
$ cli watch

# 代理使用
$ cli watch --json
# 或
$ cli watch --no-tui
```

**输出应该是有效的 JSON 或 NDJSON。**

**如果代理无法解析你的输出，你的 CLI 在代理世界中不存在。**

#### 自动检测受众

**智能检测何时输出 JSON 而非 TUI**：

```javascript
// 检测是否在 CI/代理环境
if (process.env.CI || process.env.AGENT_MODE) {
  outputJSON();
} else {
  outputTUI();
}
```

**或者显式标志**：
```bash
$ cli watch --json  # 代理
$ cli watch         # 人类
```

---

### 3️⃣ 错误处理

**错误应该是可解析的和可操作的。**

#### 结构化错误输出

```json
{
  "error": {
    "code": "TASK_NOT_FOUND",
    "message": "Task '123' not found",
    "suggestion": "Run 'cli list' to see available tasks",
    "exitCode": 1
  }
}
```

**人类可读**：
```
❌ Task '123' not found
   Run 'cli list' to see available tasks
```

**代理可读**：
- 错误码可编程处理
- 建议可自动执行

---

### 4️⃣ 进度和状态

**长时间运行命令需要报告进度。**

#### 人类：进度条

```
Building project...
[████████░░] 80% (4/5 tasks)
```

#### 代理：事件流

```json
{"type": "progress", "current": 4, "total": 5}
{"type": "complete", "success": true}
```

#### 实现模式

```javascript
// 内部发射事件
for (const task of tasks) {
  emit('progress', { current, total });
  await execute(task);
}

// 根据受众渲染
if (jsonMode) {
  outputNDJSON(events);
} else {
  renderTUI(events);
}
```

---

### 5️⃣ 配置管理

**配置应该易于人类编辑和代理读取。**

#### 推荐格式

| 格式 | 人类友好 | 代理友好 | 推荐 |
|------|----------|----------|------|
| JSON | ❌ 严格语法 | ✅ 原生 | ⭐⭐ |
| YAML | ✅ 可读 | ✅ 可解析 | ⭐⭐⭐ |
| TOML | ✅ 可读 | ✅ 可解析 | ⭐⭐⭐ |
| INI | ✅ 简单 | ⚠️ 有限 | ⭐ |

#### 配置示例

```yaml
# ~/.config/mycli/config.yaml

# 默认设置
defaults:
  project: my-project
  output: table

# 代理设置
agent:
  enabled: true
  jsonOutput: true
```

---

### 6️⃣ 认证和权限

**认证流程应该对人类简单，对代理可自动化。**

#### 人类：交互式登录

```bash
$ cli login
Opening browser...
✓ Logged in as user@example.com
```

#### 代理：环境变量/API Key

```bash
$ export MYCLI_API_KEY=sk-xxx
$ cli deploy  # 无需交互
```

#### 最佳实践

- **支持多种认证方式**
- **环境变量优先于交互式**
- **清晰的错误消息**

---

### 7️⃣ 文档和示例

**文档应该服务人类和代理。**

#### 人类：README.md

- 安装指南
- 快速开始
- 常见用例
- 故障排除

#### 代理：AGENTS.md

```markdown
# Agent Instructions

## How to use this CLI

1. Authenticate: `export MYCLI_API_KEY=sk-xxx`
2. List tasks: `cli list`
3. Get details: `cli get <id>`
4. Create task: `cli add --title "..."`

## Common patterns

- Always check `cli list` before creating
- Use `--json` for programmatic access
- Errors include suggestions for next steps
```

#### 示例库

```
examples/
├── basic-usage.sh
├── automation.sh
├── ci-cd.sh
└── agent-workflow.sh
```

---

## 实施检查清单

### 基础（必须）

- [ ] `--json` 标志支持所有命令
- [ ] 结构化错误输出
- [ ] `--help` 包含示例
- [ ] AGENTS.md 文件

### 进阶（推荐）

- [ ] 自动检测代理环境
- [ ] NDJSON 事件流
- [ ] 配置管理
- [ ] 多种认证方式

### 高级（可选）

- [ ] 技能/提示文件
- [ ] 示例库
- [ ] 自动补全
- [ ] 交互式教程

---

## 关键洞察

1. **不要选择受众** — 设计同时服务人类和代理
2. **数据与表现分离** — 同一引擎，不同输出
3. **示例比描述重要** — 人类复制粘贴，代理解析模式
4. **错误应该是可操作的** — 结构化错误码 + 建议
5. **文档分层** — README 给人类，AGENTS.md 给代理

---

## 相关链接

- [[12-agentic-harness-patterns]] - 12 个 Agentic Harness 模式
- [[most-capable-agent-system-prompt]] - Most Capable Agent System Prompt
- [Google Cloud Tech 推文](https://x.com/googlecloudtech/status/2038778093104779537)
