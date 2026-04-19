# 如何创建你的 LLM 知识库 — 完整教程

> **原文作者：** hoeem (@hooeem)  
> **翻译时间：** 2026-04-07  
> **灵感来源：** Andrej Karpathy 的 LLM 知识库模式  
> **推文链接：** https://x.com/hooeem/status/2041196025906418094  
> **点赞数：** 520 | **转发：** 53 | **浏览：** 77,574 | **书签：** 1,190

---

## 📊 文章信息

| 指标 | 数值 |
|------|------|
| **原文作者** | hoeem (@hooeem) |
| **灵感来源** | Andrej Karpathy |
| **核心概念** | LLM 知识库 = 外部大脑 |
| **教程版本** | 3 个级别（初学者/舒适用户/构建者） |
| **核心工具** | Obsidian + Claude |

---

## 🎯 核心理念

**大多数人使用 AI 的方式：**
```
问问题 → 得答案 → 关闭标签页
  ↓
第二天从零开始
  ↓
无积累。无复合。
  ↓
燃烧 token 反复重新发现相同上下文
```

**Karpathy 的系统完全翻转这个：**
```
1. 收集原材料（文章/论文/YouTube 转录/PDF 等）
  ↓
2. AI 阅读一切并写结构化 wiki（摘要/概念解释/连接/主索引）
  ↓
3. 你对 wiki 问问题（它研究自己编译的知识并给出引用综合答案）
  ↓
4. 每个答案归档回 wiki（所以下个问题受益于之前所有工作）
  ↓
5. AI 定期健康检查 wiki（找矛盾/空白/过时信息并修复）
```

**结果：**
> 个人知识库每次触摸变得更聪明。

**一个月后：**
> 你拥有深度互联的资源，无 Google 搜索可复制。因为它被综合，而非仅索引。

**适用任何主题：**
- 加密货币市场
- 医学研究
- 法律案例法
- 竞争情报
- 学术研究
- 哲学

---

## 📚 三个教程版本

### 版本 1：完全初学者

**要求：** 零技能（零 tekkerzzz）

**如果你能：**
- ✅ 安装应用
- ✅ 复制粘贴文本

**你就可以现在做这个。**

---

### 版本 2：舒适使用 AI 工具

**要求：**
- ✅ 对 AI 工具舒适
- ✅ 愿意学习自动化

**阅读到"自动化"部分。**

---

### 版本 3：构建者/开发者

**要求：**
- ✅ 技术舒适
- ✅ 愿意构建完整系统

**阅读完整教程包括所有自动化级别。**

---

## 📁 版本 1：你的第一个知识库

### 步骤 1：创建 vault（2 分钟）

**打开 Obsidian：**
1. 点击"Create new vault"
2. 命名描述性名称（如"crypto-research"或"health-knowledge"）
3. 选择保存位置（Documents 文件夹即可）
4. 点击"Create"

**你现在有空 vault。** Obsidian 监视这个文件夹。任何 markdown 文件放入会自动显示为笔记。

---

### 步骤 2：创建两个文件夹（1 分钟）

**在 Obsidian 左侧边栏：**
```
右键 → New folder

创建：
- raw（源材料：文章/笔记/收集的任何东西）
- wiki（AI 构建编译知识库的地方）
```

**这就是你的完整起始结构。**

---

### 步骤 3：添加第一个原始源（5 分钟）

**选择一个你真正感兴趣的主题。找 3-5 篇好文章。**

**对每篇：**
1. 右键 raw 文件夹 → New note
2. 给描述性名称（如"bitcoin-halving-2024-explainer"）
3. 复制粘贴文章文本到笔记
4. 在顶部添加：`Source: [粘贴 URL]`

**关键：**
> 不要过度思考格式。不要担心结构。只需把原始文本放进去。

**快速获胜：** 安装 Obsidian Web Clipper 浏览器扩展（免费，Chrome/Firefox/Safari/Edge）。一键保存网页为格式化 markdown 笔记。

---

### 步骤 4：让 AI 编译你的 wiki（5 分钟）

**打开 Claude（或你首选的 AI）。复制粘贴这个提示：**

```
I have a knowledge base with raw sources in a raw/ folder.
Please read all sources and compile a structured wiki with:

1. Individual summaries for each source (100-150 words each)
2. Concept explanation articles for key ideas mentioned across sources
3. Entity pages for people, organizations, and tools mentioned
4. A master index file that lists all pages with [[wikilinks]] between them
5. Cross-references showing how concepts connect

Format everything as markdown with YAML frontmatter including:
- title
- created_date
- source_count
- tags
- summary (50 words)

Use kebab-case for all filenames. Create [[wikilinks]] for all concept references.
```

**AI 产生结构化输出。复制每个部分到 wiki 文件夹的新笔记：**
- 保存摘要为独立笔记（如 `wiki/summary-bitcoin-halving.md`）
- 保存主索引为 `wiki/index.md`
- 保存概念文章到 wiki/ 带描述性名称

---

### 步骤 5：见证魔法

**打开 Obsidian 的 Graph View（点击左侧边栏图图标或按 Ctrl/Cmd+G）。**

**你将看到：**
- 笔记作为点
- 由 AI 创建的 [[wikilinks]] 连接
- 你的知识库可视化为连接思想的网络

**点击任何 [[linked concept]]：**
- 如页面存在 → Obsidian 打开它
- 如不存在 → Obsidian 提供创建它

**这就是 wiki 如何有机增长。**

**你现在有工作知识库。从这里开始都是让它更大、更快、更强大。**

---

## 🌱 增长你的知识库（日常习惯）

### 添加新源

**每当你读到值得保留的东西：**
1. 剪贴或粘贴到 raw 文件夹
2. 打开 Claude 粘贴：
```
I added a new source to raw/[filename].md.
Please:
1. Create a summary (100-150 words)
2. Identify 3-5 key concepts and create/update concept pages
3. Identify entities (people, orgs, tools) and create/update entity pages
4. Update the master index with new pages and summaries
5. Create [[wikilinks]] from existing pages to new content
```
3. 保存输出到 wiki 文件夹，用更新的索引替换旧索引

---

### 问问题

**一旦有 10+ 编译文章：**
```
Based on my knowledge base wiki, please answer:

[Your question here]

Please:
1. Read the index first to identify relevant pages
2. Load and read those specific pages
3. Synthesise an answer with citations to specific wiki pages
4. Format as markdown with sections and bullet points
```

**关键习惯：**
> 总是将答案归档回 wiki。保存到 wiki 文件夹。这是复合循环。每个问题丰富知识库供未来问题使用。

---

### 每周健康检查

**每周一次，粘贴完整索引到 Claude：**
```
Please health-check my wiki index. Look for:

1. Contradictions between different pages
2. Gaps where concepts are mentioned but not explained
3. Broken [[wikilinks]] pointing to non-existent pages
4. Stale content that newer sources have superseded
5. Missing cross-references between related concepts

For each issue found, suggest a specific fix.
```

**每周三次互动：**
- 一两次源添加
- 偶尔问问题
- 一次健康检查

**这就是知识库稳定增长所需的全部。**

---

## 🏗️ 版本 2&3：完整系统

### 三层设计

| 层 | 文件夹 | 说明 |
|----|--------|------|
| **1** | raw/ | 原始源（你的单一真相源）。AI 从这里读取但永不修改。文章/论文/仓库/数据集/图像都放这里。想象为图书馆的 intake 架。 |
| **2** | wiki/ | AI 生成和 AI 维护。摘要/概念文章/实体页面（人/组织/工具）/交叉链接/索引/查询输出都放这里。你很少直接编辑。AI 做写作。 |
| **3** | CLAUDE.md | 配置文档告诉 AI wiki 如何结构化、遵循什么命名约定、可执行什么操作。这是控制 AI 行为的程序。放在 vault 根文件夹。 |

---

### 四个操作循环

**这些持续重复，复合 wiki 价值：**

| 循环 | 说明 |
|------|------|
| **Ingest** | 你添加原始源。AI 读取它们并创建摘要/概念页面/连接。 |
| **Compile** | AI 构建和更新 wiki 页面，维护索引，将新信息编织到现有结构中。 |
| **Query** | 你问问题。AI 研究整个 wiki 并产生引用答案，归档回去。 |
| **Lint** | AI 健康检查矛盾/空白/断裂链接/过时内容/缺失页面。修复能修复的，标记不能修复的。 |

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
    ├── concepts_index.md
    ├── entities_index.md
    └── summaries_index.md
```

**你不需要每个子文件夹第一天就开始。从 raw/、wiki/、CLAUDE.md 开始。随 wiki 增长添加子文件夹。**

---

### 命名文件

**对所有文件名使用 kebab-case（小写，词用连字符分隔）：**
```
active-inference.md ✓
Active Inference.md ✗
active_inference.md ✗
```

**源摘要：** `author-year-short-title.md`（如 `friston-2010-free-energy.md`）

**概念：** 直接用概念名（如 `transformer-architecture.md`）

**为什么重要：**
> kebab-case 跨每个操作系统工作，URL 友好，AI 一致引用。相信我。当你有 200+ 文件时你会感谢自己。

---

## 🤖 设置 AI 环境

### 选项 A：Claude Chat（最简单，无需技术技能）

**大多数人应从这个开始。**

**设置：**
1. 去 claude.ai 登录（推荐 Pro 订阅$20/月）
2. 创建 Project（左侧边栏 → Projects → New Project）
3. 在 Project instructions 粘贴 CLAUDE.md 内容
4. 上传原始源和现有 wiki 文件到 Project

**每次对话在那 Project 中有持久上下文。** Claude 跨对话记住你的 wiki 结构和约定。

**工作流：**
- 粘贴新源 → Claude 生成 wiki 页面 → 你复制回 Obsidian
- 问问题 → Claude 产生引用答案 → 你保存为笔记
- 请求健康检查 → Claude 识别问题 → 你应用修复

**是的，这是手动的。但它可靠工作且无需终端知识。**

---

### 选项 B：Claude Code（最强大，需要终端舒适）

**Claude Code 是 Anthropic 的命令行工具，有完整文件系统访问。** 它直接读取/写入/创建/修改文件。适合自动化 wiki 维护。

**前选择这选项：**
- 需要基本终端舒适（导航文件夹/运行命令）
- 最低 Pro 订阅$20/月，Max 计划$100 或$200/月供更重用
- 无免费层供 Claude Code

**设置：**
```bash
# 导航到 vault 文件夹
cd ~/path/to/your-vault

# 开始会话
claude
```

**Claude Code 自动从 vault 根读取 CLAUDE.md。**

**为什么强大：**
> Claude Code 可读所有文件、创建新 wiki 页面、编辑现有、运行搜索工具、执行脚本。全部无需你复制粘贴任何东西。单个提示如"process all new files in raw/"自动触发整个 ingest-compile 循环。

---

### 选项 C：其他 AI 工具

**几个替代支持这工作流：**
- OpenAI Codex
- Gemini CLI
- 任何可读写 markdown 的 AI 工具

**核心要求相同：** 读取 markdown 文件进，产生 markdown 文件出。

---

## 📄 编写 CLAUDE.md：控制一切的模式

**CLAUDE.md 是你系统中单一最重要文件。** 它告诉 AI 你的 wiki 如何结构化、遵循什么规则、可执行什么操作。

**想象为 AI 研究图书管理员的工作描述。**

**如用 Claude Code，这文件在每次会话开始自动加载。如用 Claude Chat，粘贴到 Project instructions 或每次对话开始。**

### 模板（复制这个，自定义第一行）

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

**保持简洁。每行吃掉 AI 上下文窗口预算。告诉 AI 如何找信息而非内联包含一切。**

**模板故意低于 80 行。抵制过度指定冲动。**

---

## 🌐 用 Web Clipper 超级充电数据收集

**手动复制文章有效，但 Obsidian Web Clipper 浏览器扩展使收集戏剧性更快。** 一键将网页转为干净 markdown 笔记到你的 vault。

### 安装

**从浏览器扩展商店安装免费开源扩展（Chrome/Firefox/Safari/Edge）。** 点击浏览器工具栏 Obsidian 图标，然后点击齿轮图标配置。

### 配置

**设置这些：**
- **General → Vault：** 准确输入 vault 名称如 Obsidian 中显示
- **Templates → Default template → Note location：** 设为 `raw/articles/`
- **Templates → Default template → Properties：** 添加这些元数据字段：
  - `title`
  - `source_url`
  - `clipped_date`
- **Templates → Default template → Note content：** 设为 `{{content}}`

### 这给你什么

**读到值得保存的文章？**
```
点击浏览器工具栏 Obsidian 图标
  ↓
确认模板
  ↓
点击"Add to Obsidian"
  ↓
完成
```

**文章作为格式化 markdown 笔记出现在 raw/articles/ 文件夹，准备 AI 处理。**

### 使图像离线工作

**默认 Web Clipper 保存图像为网页链接，页面离线时断裂。** 用 Local Images Plus 插件修复：

1. Obsidian：Settings → Community Plugins → Turn off Restricted Mode → Browse
2. 搜索"Local images plus"并安装
3. 在插件设置，设置下载文件夹到 `raw/assets/`
4. 剪贴会话后运行"Localise attachments"命令

**这下载所有引用图像到本地。** 一切离线工作，如用视觉能力模型 AI 可引用图像。

### 转换非网页源

**对 PDF/Word 文档等，用 MarkItDown（微软免费工具）：**
```bash
pip install markitdown
markitdown document.pdf > raw/pdfs/document.md
```

**不舒适命令行？** 打开 PDF，全选，复制，粘贴到 raw/ 中新笔记。格式不完美，但 AI 仅需文本内容。

---

## 📚 Wiki 编译：将原始源转为结构化知识

**这是核心操作。** 你收集了源。现在 AI 编译它们到活的 wiki。

### 首次编译

**如用 Claude Code，导航到 vault 在终端运行：**
```bash
claude
```

**然后输入：**
```
Please compile my wiki from raw sources.

1. Read all files in raw/
2. For each source, create a summary (100-150 words) in wiki/summaries/
3. Identify key concepts and create concept pages in wiki/concepts/
4. Identify entities (people, orgs, tools) and create pages in wiki/entities/
5. Create wiki/index.md with all pages, summaries (~50 words each), tags, and source counts
6. Add [[wikilinks]] between all related concepts
7. Log all operations in wiki/log.md
```

**如用 Claude Chat，上传原始源文件（或粘贴它们）连同 CLAUDE.md，用相同提示。你需手动复制每个生成页面到正确文件夹。**

**对 10 篇文章，预期约：**
- 10 个源摘要
- 15-30 个概念/实体页面
- 1 个综合索引

**通常一次对话带几个后续。**

---

### 增量编译（添加新源）

**初始构建后，每个新源触发增量更新而非重新处理一切：**
```
I added [N] new sources to raw/.
Please integrate them into the existing wiki:

1. Create summaries for new sources
2. Create/update concept and entity pages mentioned
3. Update the index with new pages
4. Add cross-references from existing pages to new content
5. Do NOT reprocess existing sources
```

**这是关键效率原则：** AI 将新源集成到现有结构而非从头重建。快速且 token 高效。

---

### 当事情出错（它们会）

**AI 偶尔产生不完美输出。完全正常。** 这是你会遇到的：

| 问题 | 修复 |
|------|------|
| **缺失或畸形 frontmatter** | AI 有时忘记顶部 YAML 块或格式错。修复：下次提示提醒它（"please ensure all pages have complete YAML frontmatter as specified in CLAUDE.md"） |
| **断裂 wikilinks** | AI 创建 [[link]] 到不存在的页面。修复：这实际 fine。Obsidian 中点击断裂链接提供创建页面。你也可要求 AI 在 lint 通过中为所有未链接概念创建存根页面。 |
| **幻觉连接** | AI 声称两个概念相关但源材料不支持。修复：这正是为什么你保持原始源不可变。你可总是检查声称对原件。标记可疑连接并要求 AI 用特定引用验证。 |
| **上下文窗口溢出** | 如 wiki 变大，AI 无法一次读一切。修复：总是从索引文件开始，然后仅加载需要的特定页面。 |

---

## 📑 主索引：AI 如何导航你的 Wiki

**索引文件是使整个系统工作无需复杂数据库基础设施的东西。** 它是 AI 首先读取的目录，允许它决定对任何任务加载哪个特定页面。

### 好索引示例

```markdown
# Knowledge Base Index

Last updated: 2026-04-07
Total pages: 47
Total sources: 23

## Concept Articles

- [[active-inference]] — Framework for understanding how agents act under uncertainty. Combines perception, action, and prediction into unified model. (Sources: 5) #neuroscience #ai
- [[transformer-architecture]] — Neural network architecture using self-attention. Foundation of modern LLMs. (Sources: 8) #ai #deep-learning
- ...

## Entity Pages

- [[karpathy-andrej]] — AI researcher, former Tesla AI director. Advocates for LLM knowledge bases. (Sources: 3) #researcher
- ...

## Source Summaries

- [[friston-2010-free-energy]] — Friston's free energy principle paper summary. (2010) #neuroscience
- ...
```

**每个条目有 [[wikilink]]、约 50 词摘要、关键标签、源计数。** 这格式让 AI 扫描整个 wiki 内容约 6,500 token 供 100 篇文章。与现代上下文窗口比微不足道地小。

---

### 活动日志

**wiki/log.md 是追加操作记录追踪每次操作：**
```markdown
# Wiki Activity Log

## 2026-04-07

- [10:30] Ingested 3 new sources: friston-2010.pdf, karpathy-llm-wiki.md, ...
- [10:45] Created 5 concept pages: active-inference, transformer-architecture, ...
- [10:50] Updated index with 8 new entries
- [11:00] Query: "How does active inference relate to LLMs?" → outputs/active-inference-llms.md
- [11:15] Lint pass: Fixed 2 broken links, merged duplicate concept pages

## 2026-04-06
...
```

**完整审计追踪。帮助 AI 理解最近做了什么。**

---

## ❓ 问问题：复合循环

**一旦 wiki 达到甚至 10-20 编译文章，你可开始问综合跨多源的复杂问题。**

### 查询提示

```
Based on my knowledge base wiki, please answer:

[Your question here]

Process:
1. Read wiki/index.md to identify relevant pages
2. Load and read those specific pages
3. Synthesise a comprehensive answer with citations to specific wiki pages
4. Format as markdown with sections, bullet points, and [[wikilinks]]
5. Save the answer to wiki/outputs/[question-slug].md
```

**如用 Claude Chat，你需手动粘贴索引和相关页面。**

### 关键步骤是归档答案回去

**保存到 wiki/outputs/。** 这是复合循环。每个问题丰富知识库供未来查询。

---

### 不同输出格式

**你的 wiki 不必仅产生文本：**

**幻灯片演示（用 Marp 格式）：**
```yaml
---
marp: true
theme: gaia
paginate: true
---
```

**数据可视化（如用 Claude Code 或其他有代码执行的工具）：**
```python
import matplotlib.pyplot as plt
# Generate charts from wiki data
```

**对比表/决策框架/阅读列表。wiki 是你的画布。**

---

## 🔌 Obsidian 插件

**这些免费插件将 Obsidian 从简单笔记查看器转为严肃知识库界面：**

### 如何安装插件

**Settings → Community Plugins → Turn off Restricted Mode → Browse。** 搜索插件名，点击 Install，然后 Enable。

### 必备插件

| 插件 | 用途 |
|------|------|
| **Dataview** | 最强大插件。将 vault 视为可查询数据库，自动读取所有 YAML frontmatter。在任何笔记嵌入活查询。 |
| **Templater** | 创建笔记时自动填充日期/文件名/其他变量。手动创建 wiki 页面时节省时间。 |
| **Obsidian Git** | 自动版本控制。配置每 30 分钟自动提交并推送到远程仓库。AI 犯错时每个更改可追踪可逆。你的安全网。 |
| **Tag Wrangler** | 批量重命名和合并标签跨整个 vault。一旦分类增长必不可少。 |
| **Linter** | 保存时自动格式化笔记。强制一致 YAML frontmatter/标题级别/间距。AI 写多文件时关键因格式漂移。 |
| **Marp Slides** | 渲染 markdown 文件为演示幻灯片。任何 frontmatter 有 `marp: true` 的笔记变幻灯片。导出到 PDF/HTML/PowerPoint。 |
| **Homepage** | 指定笔记为 vault 着陆页。构建带 Dataview 查询的仪表板显示最近活动和统计。 |

---

### Graph View（内置，无需插件）

**Obsidian 的 Graph View 将 wiki 可视化为交互网络。** 笔记是点。[[wikilinks]] 是连接线。高度连接概念显示为大节点。

**用途：**
- 发现相关知识点集群
- 找需要集成的孤立笔记
- 发现主题间意外连接

---

## 🏥 健康检查和质量维护

**定期健康检查防止 wiki 衰败为不连接笔记集合。** 每周运行，或每批新源后。

### Lint 提示

```
Please health-check my wiki. Look for:

1. Contradictions between different pages
2. Gaps where concepts are mentioned but not explained
3. Broken [[wikilinks]] pointing to non-existent pages
4. Stale content that newer sources have superseded
5. Missing cross-references between related concepts
6. Duplicate concepts under different names
7. Pages with no inbound links (orphans)

For each issue found:
- Describe the issue specifically
- Suggest a concrete fix
- If fix requires my input, flag it for review
```

---

### 补充自动检查

**如舒适命令行，这些免费工具捕捉 AI 可能错过的结构问题：**

```bash
# 强制一致 markdown 格式
npm install -g markdownlint-cli
markdownlint wiki/

# 验证所有超链接
npm install -g markdown-link-check
find wiki/ -name "*.md" | xargs markdown-link-check
```

**可选。AI 的语义 lint 捕捉重要的。这些捕捉格式小问题。**

---

### 两模型验证模式

**对高风险知识库（医学研究/法律分析/投资论文），用两个不同 AI 模型：**
```
一个写 wiki 页面
  ↓
第二个独立验证它们进入"活"wiki 前
```

**这防止复合幻觉。** Karpathy 原始帖子许多评论者标记的真实担忧。

**用 Claude 编译，用 GPT-4o 验证（或反之）。** 如两者同意，内容可能可靠。如不同意，调查。

---

## 📈 扩展：当 Wiki 变大

### 能放多少？

**小规模（低于约 100 文章），索引文件方法 brilliantly 工作。** AI 读取索引，选相关页面，仅加载需要的。

### 用 QMD 添加搜索

**QMD 是 Tobi Lütke（Shopify CEO）构建的免费开源本地搜索引擎。** 为 markdown 知识库构建。结合关键词搜索/语义（基于意义）搜索/AI 重排序。全部本地运行在机器上无云依赖。

**安装：**
```bash
# 从 https://github.com/tobi/qmd 安装
```

---

## 🤖 自动化整个工作流

**手动复制粘贴工作流工作。但慢。** 这系统真正力量解锁当 wiki 自建。

### 最佳和最简单方式：安装即用插件（2 分钟）

**自 Karpathy 分享他的模式，社区构建了即用 Claude Code 插件，将整个 wiki 工作流转为简单斜杠命令。** 你无需写任何配置/创建任何模板/制作任何提示。安装，输入两个命令，完成。

**最快路径是 wiki-skills 插件：**
```bash
/plugin marketplace add wiki-skills
/plugin install wiki-skills
```

**你现在有这些命令：**
- `/wiki-init` — 秒级搭建完整文件夹结构
- `/wiki-ingest` — 处理原始源到 wiki（摘要/概念/实体/wikilinks/索引更新）
- `/wiki-query` — 研究跨 wiki 的问题并归档答案回去
- `/wiki-lint` — 运行健康检查并修复能修复的

**你的工作流变：**
1. 丢文章到 raw/（通过 Web Clipper 或复制粘贴）
2. 在 Claude Code 输入 `/wiki-ingest`
3. 完成。打开 Obsidian 浏览你的 wiki。

---

### 重要：DIY 自动化

**如不想要插件，或想理解底层发生什么，这节走过 5 级 DIY 自动化。**

#### Level 1：一键编译（Claude Code CLI）

**如安装 Claude Code（最低$20/月 Pro），可用单个命令处理 raw/ 中每个新源：**
```bash
claude -p "Read CLAUDE.md. Process all new files in raw/. Compile into wiki."
```

**就这些。** Claude Code 读取原始源、写每个 markdown 文件、放它们到正确文件夹、创建所有交叉链接、更新索引。打开 Obsidian 一切在那里。

**`-p` 标志意为"prompt"。** 它非交互运行并在完成时退出。

---

#### Level 2：自定义斜杠命令（输入 /compile 并走开）

**Claude Code 支持自定义斜杠命令。** 可重用工作流保存为 markdown 文件，用 `/command-name` 调用。

**创建这文件在 `.claude/commands/wiki-compile.md`：**
```markdown
# Wiki Compile Command

Read CLAUDE.md for schema.
Process all new files in raw/.
Compile into wiki structure.
Update index.
Log all operations.
```

**现在 vault 中任何 Claude Code 会话输入：**
```
/compile
```

**Claude 读取命令文件，跟随每步，构建你的 wiki。**

**创建类似命令供其他操作：**
- `.claude/commands/wiki-lint.md` → `/wiki-lint` 供健康检查
- `.claude/commands/wiki-query.md` → `/wiki-query How do AMMs work?` 供研究

---

#### Level 3：计划任务（Wiki 每天自建）

**这是真正自主的地方。** Claude Code 支持自动运行无需你输入任何东西的计划任务。

**用 Claude Desktop（Mac/Windows）：**
```
打开任务，输入 /schedule，配置：
- What: "Read CLAUDE.md. Process all new files in raw/. Compile into wiki."
- When: 每天 9am（或任何适合你的）
- Repeat: 每天/工作日/每周
```

**每次运行启动新鲜会话，处理原始源，写 wiki 页面，退出。** 你整天剪贴文章；wiki 夜间自建。

**用 CLI：**
```bash
# 添加到 cron
crontab -e

# 添加这行（每天 9am 运行）
0 9 * * * cd ~/path/to/vault && claude -p "Read CLAUDE.md. Process raw/. Compile wiki."
```

**这在后台运行。** 你的 wiki 在你睡觉时增长。

**重要注意：**
- 每次计划运行消耗 Claude 使用配额
- Desktop 任务仅在电脑醒着和 Claude Desktop 打开时运行
- Cron 任务需要 Claude Code 安装和认证在机器上

---

#### Level 4：GitHub Actions（云自动化，电脑关闭）

**最健壮设置。** 你的电脑可关闭。编译在 GitHub 服务器发生。

1. 存储 vault 在 GitHub 仓库
2. 当你推送新文件到 raw/，GitHub Action 触发
3. Claude Code 编译 wiki
4. 更新 wiki 文件提交回仓库
5. 拉更改到本地 Obsidian vault（或用 Obsidian Git 自动同步）

**工作流文件（`.github/workflows/compile-wiki.yml`）：**
```yaml
name: Compile Wiki

on:
  push:
    paths:
      - 'raw/**'

jobs:
  compile:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Claude Code
        run: npm install -g @anthropic-ai/claude-code
      - name: Compile Wiki
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: claude -p "Read CLAUDE.md. Process new files in raw/. Compile into wiki."
      - name: Commit Changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add wiki/
          git commit -m "Auto-compile wiki" || echo "No changes"
          git push
```

**成本注意：** 这用 Claude API（按 token 付费），非你的订阅。你需 API 密钥从 console.anthropic.com。对 5-10 新源，预期每次运行低于$0.50 在 Sonnet 4.6。

---

#### Level 5：完整代理技能（自维护 Wiki）

**Claude Code 支持在它检测正确上下文时自动触发的代理技能。** 与斜杠命令（你调用）不同，技能自己激活。

**创建 `.claude/skills/wiki-maintainer/SKILL.md`：**
```markdown
# Wiki Maintainer Skill

## Triggers
- User mentions adding articles to raw/
- User asks about wiki compilation
- New files detected in raw/

## Actions
1. Read CLAUDE.md for schema
2. Process new sources in raw/
3. Create/update wiki pages
4. Update index
5. Log operations

## Response
"I've processed [N] new sources and updated your wiki with [X] new pages."
```

**有这技能到位，只说"I added three new articles to raw/"，Claude 知道精确做什么。** 无需命令。

**从 Level 1 开始。** 随舒适层加更多自动化。每级构建在前一级上。无东西破坏如你跳前。

---

## 🧪 合成数据生成（高级）

**一旦 wiki 成熟，你可用它创建训练数据供微调模型"知道"你领域在其权重中。**

**喂每个 wiki 文章到 Claude：**
```
Based on this wiki article, generate 3-5 question-answer pairs that could be used for training.

Format:
Q: [Question]
A: [Answer with citations to wiki]
```

**从 100 wiki 文章，预期 300-500 QA 对。** 足够开始通过 OpenAI API 微调较小模型（约$8 每百万训练 token）或本地用 QLoRA 在消费 GPU。

**微调教模型你领域的词汇和推理模式。** 它不擅长记忆特定事实，所以那些最好由 wiki 服务。理想设置？微调模型供行为结合 wiki 供具体细节。

---

## 🛠️ 现有工具和社区实现

**你不是从零构建。** 几个开源项目已实现这模式：

| 项目 | 说明 |
|------|------|
| **llm-wiki-compiler** | 带 `/wiki-init` 和 `/wiki-compile` 命令 |
| **sage-wiki** | 完整 CLI 带 compile/search/query/serve 命令（暴露 wiki 为 MCP 服务器） |
| **CRATE** | Python CLI 实现三层模式，OpenAI 兼容，Obsidian 友好 |
| **QMD** | markdown 本地搜索引擎带关键词/向量/混合搜索加 MCP 服务器支持 |
| **Fabric** | 140+ 策划提示模式供标准操作 |

---

## 📋 YAML Frontmatter 快速参考

**每个 wiki 页面应在顶部有元数据。** 这启用 Dataview 查询/自动维护/一致 AI 处理。

```yaml
---
title: "Page Title"
created_date: 2026-04-07
updated_date: 2026-04-07
source_count: 5
tags: [tag1, tag2, tag3]
summary: "50-word summary of this page"
---
```

---

## 🔧 故障排除常见问题

| 问题 | 修复 |
|------|------|
| **AI 持续重写页面而非更新** | 添加明确指令："Append new information to existing sections. Do not rewrite content that hasn't changed. Preserve all existing wikilinks." |
| **索引变得太长和笨重** | 分裂为分类索引。保持 wiki/index.md 为轻量概览（页标题 + 一行摘要仅）。放详细摘要在每个子文件夹的 `_index.md` 文件。 |
| **AI 幻觉不相关主题间连接** | 最常见质量问题。缓解通过总是追踪声称到特定源页面，对关键内容运行两模型验证模式，并在 CLAUDE.md 包含"only make connections explicitly supported by source material"。 |
| **在完成编译前命中 Claude 使用限制** | 处理源为小批（每次 3-5）。用增量编译而非重新处理一切。如定期命中限制，考虑 Max（$100/月）或 API 按需付费。 |
| **wiki 有不同名下重复概念** | 自然发生当 AI 跨源遇到相同想法不同措辞。添加 lint 规则到 CLAUDE.md："Check for concept pages describing same thing under different names. Merge them, keeping most common name and adding redirects." |
| **想分享 wiki 给别人** | 一切是普通 markdown 文件。推 vault 到 GitHub 仓库，通过云存储分享（Dropbox/Google Drive/iCloud），或用 MkDocs Material 部署为网站（`pip install mkdocs-material && mkdocs serve`）。 |

---

## 💡 核心洞察

### 洞察 1：归档循环是超能力

**每个查询保存回 wiki 丰富它供未来查询。** 复合回报在每次交互。无聊天界面给你这个。

---

### 洞察 2：AI 是编译器，非搜索引擎

**它综合和连接思想以 chunked 检索永不能的方式。** 它理解文档间关系，非仅相似性。

---

### 洞察 3：纯文本是永远

**你的知识库是 markdown 文件夹，任何工具可读，任何操作系统，只要电脑存在。** 无供应商锁定。无专有格式。无不透明数据库。

---

### 洞察 4：从小开始

```
选一个主题
  ↓
剪贴 5 篇文章
  ↓
运行编译
  ↓
问一个问题
  ↓
看 wiki 给你什么回
  ↓
然后继续喂它
```

**唯一问题是你用第一个 wiki 构建什么主题。**

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **原文推文** | https://x.com/hooeem/status/2041196025906418094 |
| **Karpathy 原始帖子** | 待补充 |
| **Obsidian** | https://obsidian.md |
| **Claude Code** | https://claude.ai/code |
| **QMD** | https://github.com/tobi/qmd |
| **wiki-skills 插件** | 待补充 |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-07 |
| **原文作者** | hoeem (@hooeem) |
| **灵感来源** | Andrej Karpathy |
| **翻译状态** | ✅ 完整翻译 +3 版本详解 |

---

*翻译完成时间：2026-04-07 | 版本：v1.0*
