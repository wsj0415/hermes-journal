---
title: Visual Explainer — 终结编码代理中的 ASCII 艺术图表
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [visualization, agent-design, best-practice, html]
sources: [raw/articles/visual-explainer.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

Visual Explainer 是一个代理技能，用于生成富 HTML 页面/幻灯片，终结编码代理中的 ASCII 艺术图表。核心问题：每个编码代理默认使用 ASCII 艺术当你要求图表时，适用于简单情况（3 框流程图），但超出简单情况就变成不可读混乱。解决方案：真实排版、深色/浅色主题、交互式 Mermaid 图表（缩放 + 平移）、杂志质量幻灯片。GitHub 4.4K stars，MIT 许可证。

**来源**：Nico Bailon (@nicobailon) GitHub 项目

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 @aiwithjainam 推文

---

## 核心问题

**每个编码代理默认使用 ASCII 艺术当你要求图表时：**

```
框线字符 + 等宽对齐技巧 + 文本箭头
```

**问题**：
- ❌ 适用于简单情况（3 框流程图）
- ❌ 超出简单情况 → 变成不可读混乱
- ❌ 表格更糟：15 个需求对比计划 → 管道和破折号墙
- ❌ 数据在那里但阅读痛苦

**终端输出示例**：
```
┌─────────────┐    ┌─────────────┐
│   User      │───>│   Auth      │
└─────────────┘    └─────────────┘
      │                   │
      ▼                   ▼
┌─────────────┐    ┌─────────────┐
│   Login     │<───│   Token     │
└─────────────┘    └─────────────┘
```
（在终端中换行、断裂、不可读）

---

## 解决方案

**Visual Explainer 技能**：
- ✅ 真实排版
- ✅ 深色/浅色主题
- ✅ 交互式 Mermaid 图表（缩放 + 平移）
- ✅ 杂志质量幻灯片
- ✅ 针对真实代码事实检查
- ✅ 无需构建步骤，仅需浏览器

**输出**：
```
自包含 HTML 页面 → 在浏览器中打开
```

---

## 安装方式

### 方式 1：Claude Code（市场）

```bash
# 添加到市场
/plugin marketplace add nicobailon/visual-explainer

# 安装
/plugin install visual-explainer@visual-explainer-marketplace
```

**注意**：Claude Code 插件命名空间命令为 `/visual-explainer:command-name`

---

### 方式 2：Pi

```bash
# 一键安装
curl -fsSL https://raw.githubusercontent.com/nicobailon/visual-explainer/main/install-pi.sh | bash

# 或克隆运行
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git
cd visual-explainer && ./install-pi.sh
```

---

### 方式 3：OpenAI Codex

```bash
# 克隆到临时目录
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git /tmp/visual-explainer

# 安装技能
cp -r /tmp/visual-explainer/plugins/visual-explainer ~/.agents/skills/visual-explainer

# 可选：安装斜杠命令（已弃用但仍可用）
mkdir -p ~/.codex/prompts
cp /tmp/visual-explainer/plugins/visual-explainer/commands/*.md ~/.codex/prompts/

rm -rf /tmp/visual-explainer
```

**使用**：`$visual-explainer` 或让 Codex 隐式激活

**安装提示后**：`/prompts:diff-review`、`/prompts:plan-review` 等

---

## 可用命令

| 命令 | 功能 |
|------|------|
| **/generate-web-diagram** | 为任何主题生成 HTML 图表 |
| **/generate-visual-plan** | 为功能或扩展生成视觉实施计划 |
| **/generate-slides** | 生成杂志质量幻灯片 |
| **/diff-review** | 视觉 diff 审查 + 架构比较 + 代码审查 |
| **/plan-review** | 对比代码库中的计划 + 风险评估 |
| **/project-recap** | 心智模型快照（用于切换回项目） |
| **/fact-check** | 针对实际代码验证文档准确性 |
| **/share** | 部署 HTML 页面到 Vercel 获取实时 URL |

---

## 自动触发

**代理自动触发 HTML 渲染当**：
- 即将在终端倾倒复杂表格时
- 条件：4+ 行 或 3+ 列
- 结果：渲染 HTML 而非 ASCII

---

## 幻灯片模式

**任何产生可滚动页面的命令支持 `--slides` 生成幻灯片**：

```bash
# Diff 审查幻灯片
/visual-explainer:diff-review --slides

# 计划审查幻灯片
/visual-explainer:plan-review --slides

# 项目回顾幻灯片
/visual-explainer:project-recap --slides
```

**输出**：
- 每页一个主题
- 可导航（上一张/下一张）
- 可导出 PDF

---

## 使用场景

### 场景 1：架构审查

**问题**：需要审查复杂架构变更。

**传统方式**：
```
ASCII 图表在终端中换行，不可读
```

**Visual Explainer**：
```
1. /visual-explainer:diff-review
2. 生成 HTML 页面
3. 在浏览器中打开
4. 交互式架构图 + 代码对比
```

---

### 场景 2：项目回顾

**问题**：离开项目一段时间后需要快速回顾。

**传统方式**：
```
阅读多个文件，手动拼凑心智模型
```

**Visual Explainer**：
```
1. /visual-explainer:project-recap
2. 生成心智模型快照
3. 包含：架构图、关键决策、待办事项
```

---

### 场景 3：事实检查

**问题**：不确定文档是否准确反映代码。

**传统方式**：
```
手动对比文档和代码
```

**Visual Explainer**：
```
1. /visual-explainer:fact-check
2. 针对实际代码验证文档
3. 标记不准确之处
```

---

## 关键洞察

1. **ASCII 艺术有局限** — 简单情况可用，复杂情况不可读
2. **HTML 是更好的输出** — 真实排版、交互性、可分享
3. **自动触发是关键** — 代理应该自动选择最佳输出格式
4. **幻灯片模式有价值** — 演示和分享更方便
5. **事实检查很重要** — 文档应该反映真实代码

---

## 相关链接

- [[cli-design-for-agents-and-humans]] - 为 AI 代理和人类设计 CLI
- [[12-agentic-harness-patterns]] - 12 个 Agentic Harness 模式
- [GitHub 项目](https://github.com/nicobailon/visual-explainer)
