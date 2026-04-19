# Gist 分析：Karpathy 的 LLM Wiki — 个人知识库新模式

**来源**: Andrej Karpathy (@karpathy)  
**链接**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
**类型**: GitHub Gist  
**创建时间**: 2026-04-04  
**数据**: 5000+ Stars · 2783 Forks  
**抓取时间**: 2026-04-09 11:09 UTC

---

## 📊 核心洞察

**一句话总结**: Karpathy 提出 LLM Wiki 模式 — LLM 不再只是检索原始文档（如 RAG），而是增量构建并维护一个持久的 Wiki（结构化 Markdown 文件集合），知识被编译一次并保持更新，而非每次查询时重新推导，实现知识的持续复合积累。

---

## 🎯 完整翻译

### 核心理念

大多数人与 LLM 和文档的体验是 RAG 模式：你上传一批文件，LLM 在查询时检索相关片段，然后生成答案。这有效，但**LLM 每次都在从头重新发现知识**。没有积累。问一个需要综合五份文档的微妙问题，LLM 必须每次都找到并拼凑相关片段。什么都没有被建立起来。NotebookLM、ChatGPT 文件上传和大多数 RAG 系统都这样工作。

这里的想法不同。LLM 不只是在查询时从原始文档检索，而是**增量构建并维护一个持久的 Wiki** — 一个结构化的、相互链接的 Markdown 文件集合，位于你和原始来源之间。当你添加新来源时，LLM 不只是索引它以备后用。它阅读、提取关键信息，并将其整合到现有 Wiki 中 — 更新实体页面、修订主题摘要、注意新数据与旧声明矛盾之处、加强或挑战不断演变的综合。

**知识被编译一次，然后保持更新，而不是每次查询时重新推导。**

这是关键区别：**Wiki 是一个持久的、复合的产物。** 交叉引用已经在那里。矛盾已经被标记。综合已经反映你读过的一切。Wiki 随着你添加的每个来源和问的每个问题而变得更丰富。

你从不（或很少）自己写 Wiki — **LLM 编写并维护所有内容**。你负责来源、探索和提出正确的问题。LLM 做所有苦活 — 总结、交叉引用、归档和记账，使知识库随时间真正有用。

在实践中，我一边打开 LLM agent，一边打开 Obsidian。LLM 根据我们的对话进行编辑，我实时浏览结果 — 跟随链接、检查图视图、阅读更新的页面。**Obsidian 是 IDE；LLM 是程序员；Wiki 是代码库。**

这可以应用于很多不同场景：

- **个人**: 追踪自己的目标、健康、心理学、自我提升 — 归档日记条目、文章、播客笔记，随时间建立自己的结构化图景
- **研究**: 数周或数月深入一个主题 — 阅读论文、文章、报告，增量构建一个有不断演变论文的综合 Wiki
- **读书**: 每读一章就归档，为角色、主题、情节线索建立页面及其连接。读完后你有一个丰富的伴侣 Wiki。想想粉丝 Wiki 如 [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — 数千个相互链接的页面涵盖角色、地点、事件、语言，由志愿者社区多年建立。你可以个人建立类似的东西，LLM 做所有交叉引用和维护
- **商业/团队**: LLM 维护的内部 Wiki，由 Slack 线程、会议转录、项目文档、客户电话喂养。可能有人类审查更新。Wiki 保持更新因为 LLM 做团队没人想做的维护工作
- **竞争分析、尽职调查、旅行计划、课程笔记、爱好深入** — 任何你随时间积累知识并希望组织而非分散的事情

---

## 🏗️ 架构

有三层：

### 1. Raw Sources（原始来源）
你策划的来源文档集合。文章、论文、图像、数据文件。这些是**不可变的** — LLM 从它们阅读但从不修改它们。这是你的真相源。

### 2. The Wiki（Wiki）
LLM 生成的 Markdown 文件目录。摘要、实体页面、概念页面、比较、概述、综合。**LLM 完全拥有这一层**。它创建页面、在新来源到达时更新、维护交叉引用、保持一致性。**你阅读它；LLM 编写它。**

### 3. The Schema（模式）
一个文档（如 Claude Code 的 `CLAUDE.md` 或 Codex 的 `AGENTS.md`），告诉 LLM Wiki 如何结构化、约定是什么、在摄入来源、回答问题或维护 Wiki 时遵循什么工作流。**这是关键配置文件** — 它使 LLM 成为纪律严明的 Wiki 维护者而非通用聊天机器人。你和 LLM 随时间共同演化它，找出适合你领域的方式。

---

## ⚙️ 操作

### Ingest（摄入）
你将新来源放入原始集合并告诉 LLM 处理它。示例流程：LLM 阅读来源、与你讨论关键要点、在 Wiki 中写摘要页面、更新索引、更新整个 Wiki 中的相关实体和概念页面，并追加条目到日志。**单个来源可能触及 10-15 个 Wiki 页面。**

我个人喜欢一次摄入一个来源并保持参与 — 我阅读摘要、检查更新、指导 LLM 强调什么。但你也可以批量摄入多个来源，监督更少。由你开发适合你风格的工作流，并在模式中文档化供未来会话使用。

### Query（查询）
你对 Wiki 提问。LLM 搜索相关页面、阅读它们，并综合带引用的答案。答案可以采取不同形式取决于问题 — Markdown 页面、比较表、幻灯片（Marp）、图表（matplotlib）、画布。

**重要洞察：好的答案可以作为新页面归档回 Wiki。** 你要求的比较、你发现的分析、连接 — 这些是有价值的，不应消失到聊天历史中。这样你的探索在知识库中复合，就像摄入的来源一样。

### Lint（健康检查）
定期要求 LLM 对 Wiki 进行健康检查。查找：
- 页面间的矛盾
- 被新来源取代的旧声明
- 无入链的孤立页面
- 被提及但缺少自己页面的重要概念
- 缺失的交叉引用
- 可通过网络搜索填充的数据空白

LLM 擅长建议新调查的问题和寻找的新来源。这使 Wiki 在增长时保持健康。

---

## 📇 索引和日志

两个特殊文件帮助 LLM（和你）在 Wiki 增长时导航。它们服务不同目的：

### index.md（内容导向）
是 Wiki 中一切的目录 — 每个页面列出带链接、一行摘要，和可选元数据如日期或来源计数。按类别组织（实体、概念、来源等）。LLM 在每次摄入时更新它。回答问题时，LLM 先读索引找到相关页面，然后深入它们。这在中等规模（~100 来源、~数百页面）下效果出奇好，避免需要基于嵌入的 RAG 基础设施。

### log.md（时间顺序）
是追加式的记录 — 发生了什么、何时发生 — 摄入、查询、Lint 通过。有用技巧：如果每个条目以一致前缀开始（如 `## [2026-04-02] ingest | 文章标题`），日志可用简单 unix 工具解析 — `grep "^\[\[" log.md | tail -5` 给你最后 5 个条目。日志给你 Wiki 演变的时间线，帮助 LLM 理解最近做了什么。

---

## 🛠️ 可选：CLI 工具

在某刻你可能想构建小工具帮助 LLM 更高效地操作 Wiki。最明显的是 Wiki 页面上的搜索引擎 — 小规模索引文件足够，但 Wiki 增长时你想要 proper 搜索。

[qmd](https://github.com/tobi/qmd) 是好选项：它是本地 Markdown 文件搜索引擎，带混合 BM25/向量搜索和 LLM 重排序，全部在设备上。它有 CLI（LLM 可以 shell 调用）和 MCP 服务器（LLM 可以作为原生工具使用）。你也可以自己构建更简单的 — LLM 可以帮助 vibe-code 一个朴素搜索脚本随需出现。

---

## 💡 技巧和窍门

- **Obsidian Web Clipper** 是浏览器扩展，将网页文章转换为 Markdown。非常有用快速将来源放入原始集合

- **本地下载图像**: Obsidian 设置 → 文件和链接，设置"附件文件夹路径"到固定目录（如 `raw/assets/`）。然后在设置 → 热键，搜索"Download"找到"Download attachments for current file"并绑定到热键（如 Ctrl+Shift+D）。剪贴文章后按热键，所有图像下载到本地磁盘。这是可选但有用 — 让 LLM 直接查看和引用图像，而非依赖可能断裂的 URL

- **Obsidian 的图视图** 是看 Wiki 形状的最佳方式 — 什么连接什么、哪些页面是枢纽、哪些是孤儿

- **Marp** 是基于 Markdown 的幻灯片格式。Obsidian 有插件。有用直接从 Wiki 内容生成演示

- **Dataview** 是 Obsidian 插件，在页面前言上运行查询。如果 LLM 添加 YAML 前言到 Wiki 页面（标签、日期、来源计数），Dataview 可以生成动态表格和列表

- **Wiki 只是 Markdown 文件的 git 仓库**。你免费获得版本历史、分支和协作

---

## 🧠 为什么这有效

维护知识库的枯燥部分不是阅读或思考 — 而是**记账**。更新交叉引用、保持摘要更新、注意新数据何时与旧声明矛盾、维护数十页面的一致性。人类放弃 Wiki 因为维护负担增长快于价值。**LLM 不无聊、不忘更新交叉引用、可以一次触及 15 个文件。Wiki 保持维护因为维护成本接近零。**

**人类的工作**: 策划来源、指导分析、问好问题、思考这一切意味着什么  
**LLM 的工作**: 其他一切

这个想法精神上相关于 Vannevar Bush 的 [Memex (1945)](https://en.wikipedia.org/wiki/Memex) — 个人策划的知识存储，文档间有关联轨迹。Bush 的愿景比这更接近网络变成什么：私人的、积极策划的、文档间的连接与文档本身一样有价值。他无法解决的部分是谁做维护。**LLM 处理那个。**

---

## 📝 注意

这个文档故意抽象。它描述想法，不是具体实现。确切目录结构、模式约定、页面格式、工具 — 所有取决于你的领域、偏好和选择的 LLM。上面提到的一切是可选和模块化的 — 选有用的、忽略无用的。

例如：你的来源可能只是文本，所以你根本不需要图像处理。你的 Wiki 可能足够小，索引文件就是你需要的一切，不需要搜索引擎。你可能不关心幻灯片只想要 Markdown 页面。你可能想要完全不同的输出格式集合。

**正确使用方式是分享给你的 LLM agent，一起工作实例化适合你需求的版本**。文档的唯一工作是沟通模式。你的 LLM 可以找出其余。

---

## 💬 社区评论亮点

### @grishasen (Apr 8, 2026)
> 这个方法深深引起共鸣，看起来很有希望。但在花两天从文档和团队消息线程构建库后，似乎比一天内构建本地 RAG 系统作为知识库更小众。RAG 立即可用，而 Wiki 构建感觉远未完成且消耗大量 token。好想法，但实践中可能与创建 Wiki 自己没什么不同。

### @Thrimbda (Apr 8, 2026)
> 感谢你的惊人想法，我已基于这个 gist 创建了技能：[llm-wiki](https://github.com/Thrimbda/legion-mind/blob/master/skills/llm-wiki/SKILL.md)

### @jurajskuska (Apr 8, 2026)
> 是的，.claude 中每个会话有本地保存的 jsonl。我正在索引它并用作会话的第二更深层次…所以 claude 总是可以在需要时查看你问了什么以及他回应了什么。我也使用 ctx mcp 所以大量节省 token，并在其中包含 sqlite 和 obsidian，所以与 claude 同步工作非常原生。我欣赏非 AI 专家也可以在 obsidian 中使用 md 文件，所以整个 qa 团队可以参与相同的来源和知识。

### @emailhuynhhuy (Apr 8, 2026)
> **确定性检索系统**: 我将数千个验证的 n8n 工作流 JSON 组织在本地 NAS 上。每个映射到带丰富元数据的 Obsidian MD 文件：标签、流程步骤、直接指向来源 JSON。
> 
> 它直接映射到你的三层架构：
> - **原始来源**: 验证的 JSON — 不可变、LLM 从不触碰
> - **Wiki 层**: Obsidian MD 文件 — 不用于阅读，用于导航
> - **Schema**: 本地 AI 纯粹作为路由器。它遍历图、找到正确的元数据指针、检索预验证的 JSON 供团队粘贴和运行
> 
> 不是让 LLM _生成_ 工作流，我们让它 _找到_ 一个。100% 可靠。无幻觉逻辑。

### @lkishfy (Apr 8, 2026)
> 一个缺点可能是 AI 幻觉可能永久嵌入为事实，导致错误传播。它也有维护负担，你必须检查和清理笔记。
> 
> 我用 actor-network 启发图（Bruno Latour）处理这个，节点通过类型关联连接。然后我有检索系统基于网络权重、中心性、新鲜度、争议信号和网关瓶颈优先 — 所以表面的是图积极支持的，不是每个旧声明同等。
> 
> 错误仍然可以进入，但除非图继续强化它们，否则不会作为真相传播。

### @waydelyle (Apr 8, 2026)
> **SwarmVault 更新** — 我们刚达到 v0.1.27。亮点：
> - 12+ 语言（JS/TS、Python、Go、Rust 等）的解析器支持代码分析
> - `swarmvault add` 捕获 arXiv 论文、DOI、推文、文章
> - 图中语义相似边 + 超边，嵌入缓存保持本地查询快速
> - 交互式图查看器带搜索、过滤器、导出到 HTML/SVG/GraphML/Cypher
> - 带 git hooks 的 repo-aware watch 模式
> - 完全离线能力
> 
> https://github.com/swarmclawai/swarmvault

### @ClayGendron (Apr 8, 2026)
> **grover** — 进程内 agent 文件系统，组织用于工程自己知识库的虚拟文件系统 — 类似"AI 语义层"。
> 
> - 只读来源、可写综合、一个文件系统
> - 交叉引用是第一类边，不是文本
> - Unix 原始语 agent 已经知道
> 
> https://github.com/ClayGendron/grover

---

## 🔧 与现有系统对比

| 系统 | 架构 | 维护者 | 复合 | 适用场景 |
|------|------|--------|------|----------|
| **LLM Wiki (Karpathy)** | Raw/Wiki/Schema 三层 | LLM 自动维护 | ✅ 持续复合 | 个人/研究/团队知识库 |
| **RAG 系统** | 原始文档 + 向量索引 | 无维护 | ❌ 每次重新发现 | 快速问答 |
| **Patina** | 应用同步→Markdown→AI | 自动同步 | ✅ 自动更新 | 生活操作系统 |
| **Stella (Ryan)** | Gmail/日历→Markdown→Todoist | 自动+人工审查 | ✅ 持续复合 | 个人助理 |
| **Muninn (Dek)** | 11 领域剧本+记忆文件 | 自动调度 | ✅ 定期更新 | AI 秘书 |
| **当前 KilroyContentBot** | X/YouTube→Markdown→GitHub | 自动抓取 | ✅ 自动归档 | 内容分析 |

---

## 📈 实施建议

### 对 KilroyContentBot 的启示

#### 短期（1-2 周）
1. **添加 Schema 文件**
   - 创建 `CLAUDE.md` 或 `WIKI_SCHEMA.md`
   - 定义 Wiki 结构、约定、工作流
   - 文档化摄入/查询/Lint 流程

2. **增强索引和日志**
   - 创建 `index.md` — 内容目录
   - 创建 `log.md` — 时间顺序记录
   - 每次分析自动追加

3. **实施 Lint 操作**
   - 每周日运行健康检查
   - 查找矛盾、孤立页面、缺失交叉引用
   - 生成改进建议

#### 中期（1 月）
1. **Wiki 结构优化**
   - 按类别组织页面（实体/概念/来源）
   - 添加 YAML 前言（标签、日期、来源计数）
   - 实施交叉引用系统

2. **CLI 工具集成**
   - 评估 qmd 本地搜索
   - 或构建简单搜索脚本
   - LLM 可通过 shell 调用

3. **复合机制**
   - 将分析答案归档为新页面
   - 追踪页面演变
   - 标记矛盾和更新

---

## 🎨 封面图提示词（使用 nano-banana-pro）

### 选项 1：三层架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Technical Infographic Cutaway (ID: 11165)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a high-resolution professional infographic of LLM Wiki System Architecture.

Display the system in a clean, semi-realistic technical illustration style with three distinct layers using a vertical cutaway view.

Layer 1 (Top) - Raw Sources:
Icon: Document stack + lock
Label: "Raw Sources (Immutable)"
Content: Articles, papers, images, data files
Note: "LLM reads, never modifies"

Layer 2 (Middle) - The Wiki:
Icon: Interlinked pages network
Label: "The Wiki (LLM-written)"
Content: Summaries, entity pages, concepts, comparisons
Note: "You read; LLM writes"

Layer 3 (Bottom) - The Schema:
Icon: Configuration file (CLAUDE.md)
Label: "The Schema (Co-evolved)"
Content: Structure, conventions, workflows
Note: "Makes LLM disciplined"

Operations Flow (side arrows):
→ Ingest: Source → Wiki (10-15 pages touched)
→ Query: Question → Answer → New Wiki page
→ Lint: Health check → Fix contradictions

Index Files (bottom corner):
- index.md: Content catalog
- log.md: Chronological record

Headline: "LLM Wiki — Persistent, Compounding Knowledge"
Subhead: "Knowledge compiled once, kept current"

Badge: "5000+ Stars" "2783 Forks" "Karpathy 2026"

Background: Clean white or light neutral tone
Lighting: Neutral studio lighting with soft shadows
Typography: Modern sans-serif with clear hierarchy
Style: Professional educational infographic, 4K resolution
Aspect ratio: 9:16 portrait
```

---

### 选项 2：RAG vs LLM Wiki 对比风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Premium liquid glass Bento grid (ID: 6847)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Input Variable: RAG vs LLM Wiki Comparison
Language: English

Create a premium liquid glass Bento grid infographic with 6 modules comparing RAG and LLM Wiki.

Color Palette:
- RAG: Red/gray tones
- LLM Wiki: Blue/green tones
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow

Module Content (6 Cards):

M1 — Hero: "RAG vs LLM Wiki" title + comparison icon

M2 — RAG Flow: 
"Upload → Retrieve → Generate"
"每次重新发现"
"无积累"

M3 — LLM Wiki Flow:
"Ingest → Integrate → Maintain"
"编译一次，保持更新"
"持续复合"

M4 — RAG Limitation:
"问微妙问题 = 重新拼凑碎片"
"NotebookLM/ChatGPT 工作模式"

M5 — LLM Wiki Advantage:
"交叉引用已存在"
"矛盾已标记"
"综合反映一切"

M6 — Architecture:
三层：Raw/Wiki/Schema
"Obsidian=IDE, LLM=程序员，Wiki=代码库"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

### 选项 3：知识复合循环风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Exploded View Infographic (ID: 11270)  
**示例图**: https://cms-assets.youmind.com/media/1772519703684_klovml_HCbTfBgXQAAtlhh.jpg

```prompt
product design, LLM Wiki Compounding Loop, exploded view diagram, white background, three-dimensional, highly detailed circular flow showing knowledge accumulation cycle, studio lighting, product photography, best quality, aspect ratio 9:16

Circular Flow (5 stages):
1. Add Source → Raw folder
2. LLM reads & extracts
3. Integrate into Wiki (10-15 pages updated)
4. Query → Answer → File as new page
5. Lint → Fix contradictions → Wiki richer

Center Badge:
"Persistent, Compounding Artifact"
"知识编译一次，保持更新"

Outer Ring:
Operations: Ingest → Query → Lint
Index: index.md + log.md
Tools: qmd search + Obsidian graph

Style: Clean technical illustration, minimal labels, professional educational infographic
```

---

## 📚 相关项目（来自评论）

| 项目 | 描述 | 链接 |
|------|------|------|
| **llm-wiki (Thrimbda)** | 基于 Gist 创建的技能 | [GitHub](https://github.com/Thrimbda/legion-mind/blob/master/skills/llm-wiki/SKILL.md) |
| **SwarmVault** | 12+ 语言代码分析，图遍历，离线能力 | [GitHub](https://github.com/swarmclawai/swarmvault) |
| **grover** | 进程内 agent 文件系统，AI 语义层 | [GitHub](https://github.com/ClayGendron/grover) |
| **Venn** | 嵌套 Venn 图 + 双向 Wiki 面板 | [GitHub](https://github.com/1024205457-boop/Venn) |
| **celestix-ifr** | 嵌入图遍历，多跳查询优化 | [GitHub](https://github.com/emil-celestix/celestix-ifr) |

---

## 🔧 实施检查清单

### 对 KilroyContentBot 的改进

- [ ] 创建 `WIKI_SCHEMA.md` 定义结构
- [ ] 创建 `index.md` 内容目录
- [ ] 创建 `log.md` 时间顺序日志
- [ ] 实施 Lint 操作（每周健康检查）
- [ ] 将分析答案归档为新 Wiki 页面
- [ ] 添加交叉引用系统
- [ ] 评估 qmd 本地搜索集成
- [ ] 添加 YAML 前言到页面
- [ ] 实施矛盾检测
- [ ] 追踪页面演变历史

---

*分析完成 | 下一步：推送到 GitHub*
