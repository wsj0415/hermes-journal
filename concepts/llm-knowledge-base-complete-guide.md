---
title: LLM 知识库完整教程 - 从初学者到构建者
created: 2026-04-15
updated: 2026-04-15
type: summary
tags: [knowledge-base, workflow, best-practice]
sources: [raw/articles/llm-knowledge-base-complete-guide.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

LLM 知识库是一个外部大脑系统，通过 5 步循环让知识每次触摸变得更聪明：收集原材料 → AI 编译 wiki → 问问题 → 归档答案 → 健康检查。教程提供 3 个级别（初学者/舒适用户/构建者），核心工具是 Obsidian + Claude。

**核心理念**：
```
大多数人使用 AI 的方式：
问问题 → 得答案 → 关闭标签页
  ↓
第二天从零开始
  ↓
无积累。无复合。
  ↓
燃烧 token 反复重新发现相同上下文

Karpathy 的系统完全翻转这个：
1. 收集原材料（文章/论文/YouTube 转录/PDF 等）
  ↓
2. AI 阅读一切并写结构化 wiki
  ↓
3. 你对 wiki 问问题
  ↓
4. 每个答案归档回 wiki
  ↓
5. AI 定期健康检查 wiki
```

**结果**：
> 个人知识库每次触摸变得更聪明。一个月后，你拥有深度互联的资源，无 Google 搜索可复制。

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 hoeem (@hooeem) 推文

---

## 三个教程版本

| 版本 | 要求 | 阅读范围 |
|------|------|----------|
| **版本 1** | 零技能（能安装应用、复制粘贴） | 基础设置 |
| **版本 2** | 对 AI 工具舒适，愿意学习自动化 | 读到"自动化"部分 |
| **版本 3** | 技术舒适，愿意构建完整系统 | 完整教程 |

---

## 版本 1：你的第一个知识库

### 步骤 1：创建 vault（2 分钟）

1. 打开 Obsidian
2. 点击"Create new vault"
3. 命名（如"crypto-research"或"health-knowledge"）
4. 选择保存位置
5. 点击"Create"

---

### 步骤 2：创建两个文件夹（1 分钟）

```
右键 → New folder

创建：
- raw（源材料：文章/笔记/收集的任何东西）
- wiki（AI 构建编译知识库的地方）
```

---

### 步骤 3：添加第一个原始源（5 分钟）

**对每篇文章**：
1. 右键 raw 文件夹 → New note
2. 给描述性名称
3. 复制粘贴文章文本
4. 在顶部添加：`Source: [URL]`

**关键**：
> 不要过度思考格式。不要担心结构。只需把原始文本放进去。

**快速获胜**：安装 Obsidian Web Clipper 浏览器扩展，一键保存网页为格式化 markdown 笔记。

---

### 步骤 4：让 AI 编译你的 wiki（5 分钟）

**提示词**：
```
I have a knowledge base with raw sources in a raw/ folder.
Please read all sources and compile a structured wiki with:

1. Individual summaries for each source (100-150 words each)
2. Concept explanation articles for key ideas mentioned across sources
3. Entity pages for people, organizations, and tools mentioned
4. A master index file that lists all pages with wikilinks between them
5. Cross-references showing how concepts connect

Format everything as markdown with YAML frontmatter including:
- title, created_date, source_count, tags, summary (50 words)

Use kebab-case for all filenames. Create wikilinks for all concept references.
```

**保存输出到 wiki 文件夹**。

---

### 步骤 5：见证魔法

**打开 Obsidian 的 Graph View**（Ctrl/Cmd+G）：
- 笔记作为点
- 由 AI 创建的 wikilinks 连接
- 你的知识库可视化为连接思想的网络

**点击任何 linked concept**：
- 如页面存在 → Obsidian 打开它
- 如不存在 → Obsidian 提供创建它

**这就是 wiki 如何有机增长**。

---

## 增长你的知识库（日常习惯）

### 添加新源

**每当你读到值得保留的东西**：
1. 剪贴或粘贴到 raw 文件夹
2. 告诉 AI：
```
I added a new source to raw/[filename].md.
Please:
1. Create a summary (100-150 words)
2. Identify 3-5 key concepts and create/update concept pages
3. Identify entities (people, orgs, tools) and create/update entity pages
4. Update the master index with new pages and summaries
5. Create wikilinks from existing pages to new content
```
3. 保存输出到 wiki 文件夹

---

### 问问题

**一旦有 10+ 编译文章**：
```
Based on my knowledge base wiki, please answer:

[Your question here]

Please:
1. Read the index first to identify relevant pages
2. Load and read those specific pages
3. Synthesise an answer with citations to specific wiki pages
4. Format as markdown with sections and bullet points
```

**关键习惯**：
> 总是将答案归档回 wiki。这是复合循环。每个问题丰富知识库供未来问题使用。

---

### 每周健康检查

**每周一次**：
```
Please health-check my wiki index. Look for:

1. Contradictions between different pages
2. Gaps where concepts are mentioned but not explained
3. Broken wikilinks pointing to non-existent pages
4. Stale content that newer sources have superseded
5. Missing cross-references between related concepts

For each issue found, suggest a specific fix.
```

**每周三次互动**：
- 一两次源添加
- 偶尔问问题
- 一次健康检查

---

## 版本 2&3：完整系统

### 三层设计

| 层 | 文件夹 | 说明 |
|----|--------|------|
| **1** | raw/ | 原始源（你的单一真相源）。AI 从这里读取但永不修改。 |
| **2** | wiki/ | AI 生成和 AI 维护。摘要/概念文章/实体页面/交叉链接/索引/查询输出。 |
| **3** | CLAUDE.md | 配置文档告诉 AI wiki 如何结构化。这是控制 AI 行为的程序。 |

---

### 四个操作循环

| 循环 | 说明 |
|------|------|
| **Ingest** | 你添加原始源。AI 读取它们并创建摘要/概念页面/连接。 |
| **Compile** | AI 构建和更新 wiki 页面，维护索引，将新信息编织到现有结构中。 |
| **Query** | 你问问题。AI 研究整个 wiki 并产生引用答案，归档回去。 |
| **Lint** | AI 健康检查矛盾/空白/断裂链接/过时内容/缺失页面。 |

---

### 完整文件夹结构

```
your-vault/
├── CLAUDE.md                 # 模式（AI 指令）
├── raw/                      # 原始源
│   ├── articles/             # 网页文章
│   ├── papers/               # 研究论文
│   ├── transcripts/          # YouTube/播客转录
│   ├── pdfs/                 # PDF 文档
│   └── assets/               # 图像/媒体
├── wiki/                     # 编译的 wiki
│   ├── index.md              # 主索引
│   ├── log.md                # 操作日志
│   ├── concepts/             # 概念文章
│   ├── entities/             # 实体页面（人/组织/工具）
│   ├── summaries/            # 源摘要
│   └── outputs/              # 查询答案
└── _index/                   # 分类索引（可选）
```

---

### 命名文件

**对所有文件名使用 kebab-case**：
```
active-inference.md ✓
Active Inference.md ✗
active_inference.md ✗
```

**源摘要**：`author-year-short-title.md`（如 `friston-2010-free-energy.md`）

**概念**：直接用概念名（如 `transformer-architecture.md`）

**为什么重要**：
> kebab-case 跨每个操作系统工作，URL 友好，AI 一致引用。

---

## 设置 AI 环境

### 选项 A：Claude Chat（最简单）

**设置**：
1. 去 claude.ai 登录（推荐 Pro 订阅$20/月）
2. 创建 Project
3. 在 Project instructions 粘贴 CLAUDE.md 内容
4. 上传原始源和现有 wiki 文件

**工作流**：
- 粘贴新源 → Claude 生成 wiki 页面 → 你复制回 Obsidian
- 问问题 → Claude 产生引用答案 → 你保存为笔记
- 请求健康检查 → Claude 识别问题 → 你应用修复

---

### 选项 B：Claude Code（最强大）

**Claude Code 是 Anthropic 的命令行工具，有完整文件系统访问**。

**要求**：
- 基本终端舒适
- 最低 Pro 订阅$20/月
- 无免费层

**设置**：
```bash
cd ~/path/to/your-vault
claude
```

**为什么强大**：
> Claude Code 可读所有文件、创建新 wiki 页面、编辑现有、运行搜索工具、执行脚本。单个提示如"process all new files in raw/"自动触发整个 ingest-compile 循环。

---

## 编写 CLAUDE.md：控制一切的模式

**CLAUDE.md 是你系统中单一最重要文件**。

**模板**：
```markdown
# Knowledge Base Schema

## Purpose
This wiki compiles knowledge about [YOUR TOPIC] from raw sources.

## Folder Structure
- raw/ — immutable source material
- wiki/ — AI-generated knowledge base
  - index.md — master index with summaries
  - concepts/ — concept explanation articles
  - entities/ — people/orgs/tools pages
  - summaries/ — source summaries
  - outputs/ — query answers
  - log.md — operation audit trail

## Naming Conventions
- All filenames: kebab-case (lowercase, hyphens)
- Source summaries: author-year-short-title.md
- Concepts: concept-name.md
- Entities: entity-name.md

## Page Format
Every wiki page has YAML frontmatter:
```yaml
---
title: "Page Title"
created_date: YYYY-MM-DD
updated_date: YYYY-MM-DD
source_count: N
tags: [tag1, tag2, tag3]
summary: "50-word summary"
---
```

## Operations
1. Ingest: Read new sources in raw/, create summaries and concept pages
2. Compile: Update wiki pages and index with new information
3. Query: Research across wiki, produce cited answers, file back to outputs/
4. Lint: Health-check for contradictions, gaps, broken links, stale content

## Rules
- Never modify raw/ sources
- Preserve existing wikilinks when updating pages
- Only make connections explicitly supported by source material
- Append new info to existing sections, don't rewrite unchanged content
- Check for duplicate concepts under different names and merge
```

**保持简洁。每行吃掉 AI 上下文窗口预算**。

---

## 用 Web Clipper 超级充电数据收集

**安装**：从浏览器扩展商店安装免费开源扩展（Chrome/Firefox/Safari/Edge）。

**配置**：
- **General → Vault**：准确输入 vault 名称
- **Templates → Default template → Note location**：设为 `raw/articles/`
- **Templates → Default template → Properties**：添加 `title`, `source_url`, `clipped_date`
- **Templates → Default template → Note content**：设为 `{{content}}`

**工作流**：
```
读到值得保存的文章
  ↓
点击浏览器工具栏 Obsidian 图标
  ↓
确认模板
  ↓
点击"Add to Obsidian"
  ↓
完成
```

---

## 对比：传统 AI 使用 vs 知识库方式

| 维度 | 传统方式 | 知识库方式 |
|------|----------|------------|
| **积累** | 无 | 每次使用更丰富 |
| **复合** | 无 | 每个问题使下一个更好 |
| **上下文** | 每次都从零开始 | 深度互联的知识网络 |
| **成本** | 燃烧 token 重复发现 | 一次编译，多次复用 |
| **输出** | 通用答案 | 基于你收集的材料 |

---

## 相关链接

- [[second-brain-karpathy-style]] - Karpathy 风格第二大脑
- [[ai-knowledge-layer-two-tier]] - AI Knowledge Layer 两层系统
- [[agent-memory-architecture]] - Agent Memory 架构演进
- [原文推文](https://x.com/hooeem/status/2041196025906418094)
