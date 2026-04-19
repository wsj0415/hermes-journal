# Defileo — Claude + Obsidian 第二大脑完整设置指南

**来源**: https://x.com/defileo/status/2042241063612502162  
**作者**: Defileo🔮 (@defileo)  
**抓取时间**: 2026-04-13 05:37 UTC  
**类型**: X 推文线程/完整教程  
**标签**: claude, obsidian, second-brain, llm-wiki, karpathy, knowledge-management, auto-ingest, auto-lint

---

## 📊 一句话总结

Defileo 分享基于 Karpathy LLM Wiki 模式的 Claude+Obsidian 第二大脑完整设置：3 层架构（Raw sources/Wiki/Schema）+3 操作（Ingest/Query/Lint）+2 特殊文件（index.md/log.md）+ 自动化脚本（晨间摘要/会议转录处理），维护成本近零，知识随每次使用复合增长。

---

## 🏷️ 话题标签

#Claude #Obsidian #第二大脑 #LLM Wiki #Karpathy #知识管理 #自动摄入 #自动维护

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:3 层架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
3-Layer LLM Wiki Architecture diagram for Claude+Obsidian Second Brain.

Layout: Vertical 3-layer stack showing knowledge flow.

Color Palette:
- Raw Sources: Blue (#3B82F6)
- Wiki: Green (#10B981)
- Schema: Purple (#8B5CF6)
- Background: Dark gradient

Layer 1 — Raw Sources 🔵:
图标：文档集合
"Your curated source documents"
"Articles / Papers / Images / Data"
"IMMUTABLE — LLM reads, never modifies"
"Source of truth"
"Obsidian Web Clipper → /raw-sources/"

Layer 2 — Wiki 🟢:
图标：互联笔记网络
"LLM-generated markdown files"
"Summaries / Entity pages / Concept pages"
"Comparisons / Overview / Synthesis"
"LLM owns this layer entirely"
"You read it; LLM writes it"
"Cross-references auto-maintained"

Layer 3 — Schema 🟣:
图标：配置文件
"CLAUDE.md / AGENTS.md"
" Tells LLM how wiki structured"
"Conventions / Workflows to follow"
"Key configuration file"
"Makes LLM disciplined maintainer"
"You and LLM co-evolve over time"

Center Operations Flow:
"1. Ingest — Drop source → LLM processes"
"   Reads → Discusses → Writes summary → Updates index"
"2. Query — Ask wiki → LLM searches → Synthesizes with citations"
"3. Lint — Health-check wiki → Find contradictions → Suggest fixes"

Bottom Special Files:
"index.md — Content catalog (each page + link + summary)"
"log.md — Chronological record (ingests/queries/lint passes)"

Style: Clean technical architecture, dark mode with layer colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 3 层 LLM Wiki 架构的内容，垂直堆叠图直接展示 Raw/Wiki/Schema 如何协同工作，比单一架构图更能传达"分层架构"的价值。

---

### 选项 2：操作流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
LLM Wiki Operations Flow infographic showing Ingest/Query/Lint cycle.

Layout: Circular 3-operation flow with special files.

Color Palette:
- Ingest: Blue (#3B82F6)
- Query: Green (#10B981)
- Lint: Orange (#F97316)
- Background: Dark gradient

Operation 1 — Ingest 🔵:
图标：文档→Wiki
"Drop new source into /raw-sources/"
"Tell LLM to process it"
"Flow:"
"LLM reads source"
"Discusses key takeaways with you"
"Writes summary page in wiki"
"Updates index.md"
"Updates relevant entity/concept pages"
"Appends entry to log.md"
"Single source touches 10-15 wiki pages"

Operation 2 — Query 🟢:
图标：问答 + 引用
"Ask questions against wiki"
"LLM searches for relevant pages"
"Reads them, synthesizes answer with citations"
"Output forms:"
"Markdown page / Comparison table"
"Slide deck (Marp) / Chart (matplotlib)"
"Key insight: Good answers filed back as new pages"
"Explorations compound in knowledge base"

Operation 3 — Lint 🟠:
图标：健康检查
"Periodically health-check wiki"
"Look for:"
"Contradictions between pages"
"Stale claims superseded by newer sources"
"Orphan pages with no inbound links"
"Concepts mentioned but no dedicated page"
"Missing cross-references"
"Data gaps fillable by web search"
"LLM suggests new questions/sources"

Center Special Files:
"index.md — Content-oriented catalog"
"log.md — Chronological append-only record"

Bottom Why It Works:
"Humans abandon wikis — maintenance burden > value"
"LLMs don't get bored, don't forget cross-references"
"Can touch 15 files in one pass"
"Maintenance cost ≈ zero"

Style: Modern operations flow, dark mode with operation colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：自动化脚本网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 5 modules showing "Claude Automation Scripts".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Various automation colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (5 Cards):

M1 — Hero:
"Claude 自动化脚本"
"设置一次，永远使用"
Icon: Claude + Automation

M2 — 晨间摘要:
"morning_digest.py"
"读 Memory.md 找今日待办"
"读过去 24h 新/raw-sources 文件"
"打印清洁简报到终端"
"Cron 每天早 7:30 运行"

M3 — 会议转录处理:
"Read /transcripts/call-today.md"
"提取每个决策/行动项 (负责人 + 截止)"
"3  bullet 摘要"
"行动→/Action-Tracker.md"
"决策→/Decision-Log.md"
"客户笔记→/clients/"

M4 — 文章摄入:
"I just added article to /raw-sources"
"Read it, extract key ideas"
"Write summary to /wiki/summaries/"
"Update index.md with link+description"
"Update connected concept pages"
"Show every file touched"

M5 — 每周 Lint:
"Read every file in /wiki/"
"Find: contradictions/orphans/missing pages/outdated claims"
"Write health report to /wiki/lint-report.md"
"Specific fixes included"
"Maintenance stops being your job"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

> **大多数人的 LLM+ 文档体验像 RAG**：上传文件集合，LLM 在查询时检索相关块，生成答案。这有效，但**LLM 每次问题都从头重新发现知识**。没有积累。

> **真正不同的想法**：不是在查询时从原始文档检索，而是**LLM 增量构建并维护持久 wiki** — 结构化互联 Markdown 文件集合，位于你和原始来源之间。

---

### 关键差异

| RAG 系统 | LLM Wiki |
|----------|----------|
| 查询时检索原始文档 | 编译一次，保持更新 |
| 每次重新拼凑相关片段 | 交叉引用已存在 |
| 无积累 | 矛盾已标记 |
| NotebookLM/ChatGPT 文件上传 | 综合反映你读过的一切 |

> **Wiki 是持久复合产物。** 每添加来源/每问问题，Wiki 变得更丰富。

---

## 三层架构

### Layer 1: Raw Sources（原始来源）

| 特征 | 说明 |
|------|------|
| **内容** | 你策划的来源文档集合（文章/论文/图像/数据文件） |
| **特性** | **不可变** — LLM 从它们读取但从不变改 |
| **作用** | 你的真相源 |

---

### Layer 2: Wiki（维基）

| 特征 | 说明 |
|------|------|
| **内容** | LLM 生成的 Markdown 文件（摘要/实体页/概念页/比较/概述/综合） |
| **特性** | **LLM 完全拥有这一层** |
| **作用** | 创建页面/新来源到达时更新/维护交叉引用/保持一致性 |
| **关系** | 你阅读它；LLM 编写它 |

---

### Layer 3: Schema（模式）

| 特征 | 说明 |
|------|------|
| **文件** | CLAUDE.md（Claude Code）或 AGENTS.md（Codex） |
| **内容** | 告诉 LLM wiki 如何结构/约定是什么/遵循什么工作流 |
| **作用** | **关键配置文件** — 让 LLM 成为纪律严明的 wiki 维护者而非通用聊天机器人 |
| **演化** | 你和 LLM 随时间共同演化它 |

---

## 三操作

### Operation 1: Ingest（摄入）

**流程**:
```
1. 将新来源放入 raw 集合
2. 告诉 LLM 处理它
3. LLM 读取来源
4. 与你讨论关键要点
5. 在 wiki 中写摘要页
6. 更新 index
7. 更新 wiki 中相关实体和概念页
8. 追加条目到 log
```

**规模**: 单个来源可能触及 10-15 个 wiki 页面

**偏好**: 作者偏好一次摄入一个来源并保持参与 — 读摘要/检查更新/指导 LLM 强调什么。但也可批量摄入多个来源监督更少。

---

### Operation 2: Query（查询）

**流程**:
```
1. 对 wiki 问问题
2. LLM 搜索相关页面
3. 阅读它们
4. 综合带引用的答案
```

**输出形式**（根据问题）:
- Markdown 页面
- 比较表
- 幻灯片（Marp）
- 图表（matplotlib）
- Canvas

**关键洞察**:
> **好答案可作为新页面归档回 wiki。** 你要求的比较/分析/发现的连接 — 这些有价值，不应消失到聊天历史中。这样你的探索在知识库中复合，就像摄入来源一样。

---

### Operation 3: Lint（健康检查）

**定期检查**:
- 页面间矛盾
- 被新来源取代的旧声明
- 无入链的孤立页面
- 被提及但缺少自己页面的重要概念
- 缺失的交叉引用
- 可通过网络搜索填充的数据空白

**LLM 擅长**: 建议新调查的问题和寻找的新来源

**作用**: 保持 wiki 随增长保持健康

---

## 两特殊文件

### index.md（内容导向）

**是什么**:
- Wiki 中一切的目录
- 每页面列出带链接/一行摘要/可选元数据（如日期/来源计数）
- 按类别组织（实体/概念/来源等）

**更新**: LLM 在每次摄入时更新它

**查询时**: LLM 先读 index 找相关页面，然后深入它们

**效果**: 在中等规模（~100 来源，~数百页面）下出奇有效，避免需要基于嵌入的 RAG 基础设施

---

### log.md（时间顺序）

**是什么**:
- 追加式记录 — 发生了什么和何时
- 摄入/查询/Lint 通过

**技巧**:
> 如果每条目以一致前缀开始（如`## [2026-04-02] ingest | Article Title`），log 可用简单 unix 工具解析 — `grep "^\[\[" log.md | tail -5` 给最后 5 条目。

**作用**: 给你 wiki 演变的时间线，帮助 LLM 理解最近做了什么

---

## 可选 CLI 工具

### qmd（推荐）

**链接**: https://github.com/tobi/qmd

**功能**:
- Markdown 文件本地搜索引擎
- 混合 BM25/向量搜索 + LLM 重排序
- 全部在设备上

**接口**:
- CLI（LLM 可 shell 调用）
- MCP 服务器（LLM 可作为原生工具使用）

**替代**: LLM 可帮助 vibe-code 简单搜索脚本按需

---

## 技巧与窍门

### Obsidian Web Clipper

**作用**: 浏览器扩展，将网页文章转为 Markdown  
**价值**: 快速将来源放入 raw 集合

---

### 本地下载图像

**设置**:
1. Obsidian 设置 → Files and links
2. 设置"Attachment folder path"到固定目录（如 `raw/assets/`）
3. 设置 → Hotkeys
4. 搜索"Download"找到"Download attachments for current file"
5. 绑定到热键（如 Ctrl+Shift+D）

**使用**: 剪贴文章后按热键，所有图像下载到本地磁盘

**价值**: 让 LLM 直接查看和引用图像，而非依赖可能断裂的 URL

**注意**: LLM 不能原生读取带内联图像的 Markdown 一次通过 — 权宜之计是让 LLM 先读文本，然后单独查看一些或所有引用图像获取额外上下文。有点笨拙但足够有效。

---

### Obsidian Graph View

**作用**: 看 wiki 形状的最佳方式 — 什么连接什么/哪些页面是枢纽/哪些是孤立

---

### Marp

**作用**: 基于 Markdown 的幻灯片格式  
**插件**: Obsidian 有插件  
**价值**: 直接从 wiki 内容生成演示

---

### Dataview

**作用**: Obsidian 插件，在页面 frontmatter 上运行查询  
**用法**: 如果 LLM 添加 YAML frontmatter 到 wiki 页面（标签/日期/来源计数），Dataview 可生成动态表格和列表

---

### Git 版本控制

> **Wiki 只是 Markdown 文件的 git 仓库。** 你免费获得版本历史/分支/协作。

---

## 为什么这有效

> **维护知识库的枯燥部分不是阅读或思考 — 是记账。**

**人类放弃 Wiki 的原因**: 维护负担增长快于价值

**LLM 的优势**:
- 不无聊
- 不忘更新交叉引用
- 可一次触及 15 个文件

> **Wiki 保持维护因为维护成本接近零。**

**分工**:
| 人类的工作 | LLM 的工作 |
|-----------|-----------|
| 策划来源 | 总结 |
| 指导分析 | 交叉引用 |
| 问好问题 | 归档 |
| 思考意味着什么 | 记账 |

---

## 与 Memex 的关系

> **这想法精神上相关于 Vannevar Bush 的 Memex (1945)** — 个人策划的知识存储，文档间有关联轨迹。

**Bush 的愿景**:
- 私人的
- 积极策划的
- 文档间连接与文档本身一样有价值

**Bush 无法解决的部分**: 谁做维护

**解决方案**: **LLM 处理那个。**

---

## 实际实现命令

### 文章摄入

```bash
claude -p "I just added an article to /raw-sources. 
Read it, extract the key ideas, write a summary page to /wiki/summaries/, 
update index.md with a link and one-line description, and update any 
existing concept pages that this article connects to. 
Show me every file you touched." --allowedTools Bash,Write,Read
```

**效果**: 一篇文章 — Claude 链接 10-15 个 wiki 页面，浮现意外连接，标记矛盾，准确记录改变什么。

---

### 查询 Wiki

```bash
# Ask the wiki
claude -p "Query the wiki about [TOPIC]"

# LLM scans index, pulls right pages, answers with citations
# Then saves best outputs back into wiki:
# - Comparisons
# - Analyses  
# - New connections
# So insights don't vanish in chat and knowledge base compounds
```

---

### 每周 Lint

```bash
claude -p "Read every file in /wiki/. Find: contradictions between pages, 
orphan pages with no inbound links, concepts mentioned repeatedly but 
with no dedicated page, and claims that seem outdated based on newer files 
in /raw-sources/. Write a health report to /wiki/lint-report.md with 
specific fixes." --allowedTools Bash,Write,Read
```

**效果**: 知识库自动保持健康，维护停止成为你的工作。

---

### 晨间摘要自动化

```bash
claude -p "Write a Python script called morning_digest.py that:
1) reads Memory.md and surfaces any open actions due today
2) reads any new files added to /raw-sources in the last 24 hours
3) prints a clean briefing to the terminal.
Then schedule it as a cron job every morning at 7:30am." --allowedTools Bash,Write
```

**效果**: 设置一次，每天早上运行无需你碰任何东西。

---

### 会议转录处理

```bash
claude -p "Read the transcript in /transcripts/call-today.md.
Extract every decision made, every action item with owner and deadline,
and a 3-bullet summary. Add actions to /Action-Tracker.md, log decisions 
to /Decision-Log.md, and create a client note in /clients/ linking back 
to this transcript." --allowedTools Bash,Write,Read
```

**效果**: 每个归档的决策，每个追踪的行动，再也不会丢失到聊天历史中。

---

## 为什么第二大脑项目失败

> **大多数第二大脑项目以同样方式死亡。**

**死亡循环**:
```
1. 开始有组织
2. 维护堆积（更新标签/保持交叉引用最新/结构演变时重组）
3. 那是全职外额外工作 → 你跳过它
4. 系统退化 → 你回到分散笔记
5. 6 个月后尝试重建 → 循环重复
```

---

### Claude 如何打破循环

> **Claude 永久打破那循环。维护只是一个命令。**

| 任务 | 传统方式 | Claude 方式 |
|------|----------|------------|
| 重组整个 vault | 手动数小时 | 一个提示词 |
| 从 Notion 迁移 | 手动复制 | 一个命令处理每个导出文件 |
| 更新交叉引用 | 手动追踪 | 自动维护 |
| 健康检查 | 手动审查 | 每周 lint 命令 |

---

## 从零开始

### 没有现有材料？

> **打开 Claude 聊天聊 20 分钟**：你的工作/你的目标/你在构建什么/你在弄清什么。

**保存那对话为你的 Memory 文件** — 那足够让你的第一次会话感觉像 Claude 实际认识你。

> **Vault 不需要完整才有用。它只需要真实。**

---

## 核心哲学

> **人类的工作是策划来源/问好问题/思考意味着什么。**

> **Claude 的工作是其他一切** — 总结/交叉引用/归档/记账，使知识库随时间实际有用。

> **Vannevar Bush 在 1945 年描述了类似东西** — 个人策划的知识存储，文档间连接与文档本身一样有价值。他称之为 Memex。**他无法解决的部分是谁做维护。**

> **现在你知道谁做了：构建一次 → 永远使用，它每天你添加时变得更好。**

> **这就是为什么它应该是非法的。** — Leo

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 架构层数 | 3 |
| 核心操作 | 3 (Ingest/Query/Lint) |
| 特殊文件 | 2 (index.md/log.md) |
| 单来源触及页面 | 10-15 |
| 中等规模 | ~100 来源/~数百页面 |
| 维护成本 | ≈ 零 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Wiki 是持久复合产物" | 核心价值 |
| "你读它；LLM 写它" | 分工 |
| "维护成本≈零" | LLM 优势 |
| "好答案归档为新页面" | 复合机制 |
| "构建一次→永远使用" | 长期价值 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **3 层架构** — Raw/Wiki/Schema 清晰分离
2. **3 操作循环** — Ingest/Query/Lint 完整生命周期
3. **index.md + log.md** — 内容目录 + 时间日志
4. **自动化脚本** — 晨间摘要/会议处理
5. **维护近零成本** — LLM 处理记账
6. **复合知识** — 每次使用变得更好

### 可实施
- 为内容创作采用 3 层架构
- 实现 Ingest/Query/Lint 操作循环
- 创建 index.md 追踪所有内容
- 创建 log.md 记录所有操作
- 自动化晨间摘要和会议处理
- 用 LLM 处理内容归档和交叉引用

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Defileo 原文 | https://x.com/defileo/status/2042241063612502162 |
| Karpathy LLM Wiki | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| qmd | https://github.com/tobi/qmd |
| Obsidian | https://obsidian.md |
| Marp | https://marp.app |

---

*原始来源：https://x.com/defileo/status/2042241063612502162*
