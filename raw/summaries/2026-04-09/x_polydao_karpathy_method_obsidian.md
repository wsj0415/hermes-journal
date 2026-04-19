# X 内容分析：Karpathy Method — Claude Skills + Obsidian 完整指南

**来源**: Mr. Buzzoni (@polydao)  
**链接**: https://x.com/polydao/status/2042203352054771748  
**类型**: X Article 长文  
**抓取时间**: 2026-04-09 13:04 UTC

---

## 📊 核心洞察

**一句话总结**: 这篇文章详细解释了如何实现 Karpathy 的 LLM Wiki 模式 — 使用 Obsidian + Claude Code + Skills + MCP，构建一个自我改进的知识库，LLM 作为编译器和图书管理员（而非聊天机器人），人类只负责捕获来源，LLM 负责所有组织、维护和健康检查，实现知识的持续复合积累。

---

## 🎯 完整翻译

### 引言

大多数人像使用稍微更聪明的 Google 一样使用 AI。

- 问问题 → 得答案 → 关闭标签 → 忘记一切
- 同时，一小群人正在悄悄构建**自我改进的知识库**，每周复合增长
- 这些人将在研究、产品和职业上超越其他人

> 这篇文章向你展示如何构建一个 — 使用 Obsidian、Claude Code、Skills 和纯 Markdown。不需要 PhD。只需一个周末就能设置的系统。

> 忘记"记笔记"。你在构建一个**活的 Wiki**，LLM 在后台为你编写和维护。

这个想法来自 Andrej Karpathy（前 OpenAI、Tesla AI），他最近分享了他的大部分 LLM 使用已经转变 — 更少写代码，更多操作存储为 Markdown 文件的知识。

---

## 🔄 完整循环

```
1. 你将原始数据（文章、论文、仓库、转录、图像）放入 raw/ 文件夹
2. LLM 将其编译成 wiki/ 中的结构化 Wiki — 带概念、反向链接、摘要的 Markdown 文件
3. 你在 Obsidian 中用图视图查看和导航
4. 你问复杂问题 — LLM 阅读你的 Wiki 并将答案写为新文件
5. 定期，LLM"健康检查"清理不一致并提出新文章
6. 每个查询归档回 Wiki，使其随时间更聪明
```

> **心态转变**: LLM 作为**编译器和图书管理员** — 不是聊天机器人。

如果保存信息很烦人，系统第一天就会死。所以从这里开始。

---

## 📦 安装什么

### 必需工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **Obsidian** | 免费、本地优先、基于 Markdown 的知识编辑器 | obsidian.md |
| **Obsidian Web Clipper** | 浏览器扩展，将任何网页保存为干净的 .md（带 URL、标题、日期、标签） | Obsidian 插件 |

### 文件夹结构

在你的 vault 中创建三个文件夹：

```
your-vault/
├── raw/           # 所有来源材料放在这里
├── wiki/          # 编译的知识放在这里
└── reports/       # 你的输出（答案、论文、幻灯片）
```

> **额外技巧**: 在 Obsidian 中绑定热键下载当前笔记的所有图像到本地 — 这样你的 LLM 可以引用它们而无需访问外部 URL。

### 你唯一的工作

任何时候看到有趣的东西，剪贴到 raw/。**不要组织。不要重命名。只需捕获。**

---

## 🤖 LLM 编译 Wiki

这里大多数"记笔记系统"崩溃：人类必须做所有组织工作。在这个系统中，**人类不做**。

LLM 扫描 raw/ 并生成或更新 wiki/ 中的页面。每个重要概念获得自己的 .md 文件，包含：

- 简短定义和关键洞察
- 链接回 raw/ 中的原始来源
- 反向链接到相关概念
- 索引页面列出关键子主题（如 RAG.md、prediction-markets.md、LLM-architectures.md）

**你几乎不手动触碰 wiki/。LLM 拥有它。**

不要认为 Obsidian 是"Markdown 编辑器"。在这个工作流中，**它是你的知识 IDE**。

### 为什么 Obsidian 有效

| 功能 | 用途 |
|------|------|
| **Backlinks** | 看到概念在整个 vault 中被引用的所有地方 |
| **Graph View** | 发现知识集群和孤立节点（= 你还没填充的空白） |
| **Dataview 插件** | 像数据库一样查询你的笔记 |
| **Marp 插件** | 直接将 Markdown 文件渲染为演示幻灯片 |

> **Karpathy 的关键观察**: 人类主要阅读，LLM 主要编写。你浏览、做小修、问新问题。你不像 2008 年那样手工编写 Wiki 页面。

---

## 📈 何时真正价值开始

一旦你的 Wiki 达到 **~50-100 篇文章**，真正价值开始。

不是在无状态聊天中问"解释预测市场套利"，而是问：

> "仅使用我的 Wiki，根据我目前研究的一切，解释预测市场交易者的关键边缘策略。"

背后你的 agent：

1. 定位 wiki/ 中的相关 Markdown 文件
2. 让 LLM 端到端阅读它们（现代 1M token 上下文窗口使这在个人规模可行）
3. 写新 Markdown 报告到 reports/，带链接回它使用的来源概念

**每个严肃问题成为 vault 中的新永久资产，而非消失到聊天历史中。**

---

## 📝 强制 LLM 以文件回答

一个习惯将这个系统的 ROI 提高 10 倍：**强制 LLM 以文件回答，而非 UI 中的文本。**

### 优秀输出格式

| 格式 | 用途 |
|------|------|
| **Markdown 报告** (reports/) | 你最好的思考，已保存可搜索 |
| **Marp 幻灯片** | .md 文件渲染为完整演示幻灯片（适合路演和同步） |
| **图表和图像** (images/) | 嵌入到 Wiki 页面中 |

### 然后你

- 将报告链接到相关概念页面
- 重用为未来查询的来源材料
- 推送到 Git 进行版本控制和历史

**你的查询字面上复合成更好的未来答案。**

---

## 🧹 知识 Lint（健康检查）

> 大多数人从不想到用 LLM 清理和重构知识 — 只想到添加。大错误。

Karpathy 运行定期"知识 linting"通过，LLM 扫描：

- 不同笔记中关于同一概念的**冲突声明**
- 频繁提及但**缺少专用页面**的实体
- 应该合并的**近似重复页面**
- 看起来**无来源或数字不一致**的声明
- 由新兴连接模式建议的**新文章候选**

你可以将这个包装成单个每周命令。随时间推移，你的 Wiki 趋向更高完整性和更少混乱，**零手工记账**。

---

## 🛠️ Claude Skills 集成

> Claude Code 正是为这类系统构建的：
> - 它在真实文件系统环境中运行 — 可以读写 Markdown、运行 bash 和脚本
> - 它支持 Skills — 可重用的工作流，打包为带 SKILL.md 加可选脚本和资源的目录

### 为你的第二大脑构建的 Skills 示例

| Skill | 用途 |
|-------|------|
| `/kb-compile` | 读取 raw/ 中的文件，创建或更新 wiki/ 中的概念页面 |
| `/kb-report` | 基于 Wiki 生成报告到 reports/ |
| `/kb-lint` | 健康检查 — 查找矛盾、孤立页面、缺失交叉引用 |
| `/kb-search` | 搜索 Wiki 页面 |
| `/kb-ingest` | 摄入新来源到 raw/ 并触发编译 |

Skills 可以捆绑额外的 Markdown 指令、脚本和参考文件 — 你一次性编码你的个人风格和领域偏好，并在 Claude 应用、Claude Code 和 API 间重用。

**你写一次剧本。Claude 按需执行。**

---

## 🔄 从 Stateless 到 Stateful

> 标准 AI 使用是无状态的。你问 → 得答案 → 关闭标签。下次会话，模型什么都不记得。你从零开始。永远。

**LLM 知识库将其转变为有状态的、复合的记忆：**

- 今天的答案成为明天的上下文
- 你的术语和框架成为规范的 Wiki 页面
- 六个月的工作 = 模型可在单个上下文窗口中摄入的私人语料库

### 真实世界收益

| 收益 | 说明 |
|------|------|
| **更快** | 大多数问题简化为"使用我的 Wiki 生成报告" |
| **更一致** | 每次会话没有随机的不同定义或符号 |
| **工作中更有价值** | 你的第二大脑是文档、入职材料、研究档案和幻灯片工厂的集合 |

**所有这一切都存在于纯 Markdown 和图像中 — 不锁定在封闭 SaaS 内。完全可移植。完全属于你。**

---

## 🔒 本地运行选项

不想让你的研究上云？你不必。

整个架构可在本地运行，使用 **Obsidian + Ollama**（本地 LLM 运行器）：

- 通过 Clipper 捕获网页到本地 vault
- 本地 LLM 阅读和更新你的 Wiki — 无东西离开你的机器
- Claude Code 可在顶部层用于特定任务，云处理可接受时

**你决定哪些项目保持完全私密，哪些受益于更强大的云模型。**

---

## 🎯 终极状态：Fine-tuning

一旦你的 Wiki 足够大，另一扇门打开。

> Karpathy 指出自然终点：**不是总是依赖巨大上下文窗口，你可以将 Wiki 视为 fine-tuning 语料库 — 将你的知识直接烘焙到模型权重中。**

- **对个人**: 你的笔记、研究、代码压缩成"你风味"模型
- **对团队**: 内部文档、API、事件历史、设计决策 → fine-tuned 组织助手

即使没有 fine-tuning，编译的 Wiki 模式已经给出巨大杠杆。**Fine-tuning 只是压缩和加速它。**

---

## 🔌 MCP for Obsidian（关键层）

> Claude Skills + Obsidian 已经强大。但有一层大多数人完全跳过。

**MCP for Obsidian** — 一个 MCP 服务器，让 Claude 实时直接读写你的 vault。不是复制粘贴。不是导出。**Claude 字面上打开你的笔记、编辑它们、创建新文件、在特定标题下插入内容 — 全部从聊天窗口。**

- 3.3k stars on GitHub
- 384 forks
- 稳定运行

### Claude 可以用你的 vault 做什么

| 命令 | 用途 |
|------|------|
| `list_files_in_vault` | 浏览 vault 的完整结构 |
| `list_files_in_dir` | 探索特定文件夹 |
| `get_file_contents` | 按名称读取任何文件 |
| `search` | 找到提及主题的所有笔记 |
| `patch_content` | 在特定标题或块引用下插入内容 |
| `append_content` | 追加内容到现有笔记末尾 |
| `delete_file` | 删除文件或文件夹 |

### 你可立即使用的真实提示

```
"找到所有提及 Polymarket 的笔记，给我每个的简短摘要"

"拿我最后的会议笔记，创建一个新文件 summary.md，带我可以邮件发送的介绍"

"将这个想法添加到我的现有研究笔记中，在'方法论'标题下"
```

**你的 Obsidian vault 停止成为存储系统。它成为 Claude 积极维护的实时工作空间。**

---

## ⚙️ MCP 安装步骤

### Step 1: 在 Obsidian 中安装插件

设置 → 社区插件 → 浏览 → 搜索 "Local REST API" → 安装并启用。从插件设置复制 API 密钥。

### Step 2: 打开 Claude Desktop 配置

- **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

### Step 3: 添加这个块

```json
{
  "mcp-obsidian": {
    "command": "uvx",
    "args": [
      "mcp-obsidian"
    ],
    "env": {
      "OBSIDIAN_API_KEY": "<your_api_key_here>",
      "OBSIDIAN_HOST": "127.0.0.1",
      "OBSIDIAN_PORT": "27124"
    }
  }
}
```

> 重启 Claude。完成。

### 开始前需要知道的事情

| 事项 | 说明 |
|------|------|
| **uvx 路径** | 如果 Claude 找不到 uvx — 在终端运行 `which uvx` 并将完整路径粘贴到"command"字段 |
| **默认端口** | 27124，默认主机 127.0.0.1 — 无需更改，除非你配置了其他 |
| **Obsidian 必须打开** | Local REST API 插件仅在 vault 活动时运行 |
| **第一提示** | 以"Use Obsidian to..."开始 — 帮助 Claude 立即理解它应该访问 vault |
| **调试** | 查看日志：`tail -n 20 -f ~/Library/Logs/Claude/mcp-server-mcp-obsidian.log` |

---

## 📅 2 天实施计划

### Day 1 — 设置和捕获

- 安装 Obsidian，创建带 raw/、wiki/、reports/ 的 vault
- 安装 Obsidian Web Clipper，设置默认保存位置到 raw/
- 选择一个你关心的主题（加密货币、预测市场、LLM agent 等）
- 剪贴 20-30 篇文章到 raw/ — 不要组织任何东西，只需捕获

### Day 2 — 构建循环

- 在 Claude Code 中，创建基础 `/kb-compile` Skill，读取 raw/ 中的文件，让 Claude 创建或更新 wiki/ 中的概念页面
- 运行它。打开 Obsidian 并探索图视图和反向链接
- 创建 `/kb-report` Skill。问它一个关于你主题的真实问题
- 阅读 reports/ 中的输出。将其链接到相关 Wiki 页面

**如果你为一个持续研究主题认真做这个，一周内你会感觉到差异。**

你不再"只是聊天"。你在**培养一个与你一起写作的第二大脑**。

---

## 💡 与 Karpathy Gist 对比

| 功能 | Karpathy Gist | Polydao 文章 |
|------|--------------|-------------|
| **架构** | Raw/Wiki/Schema 三层 | Raw/Wiki/Reports 三层 |
| **工具** | Obsidian（推荐） | Obsidian + Claude Code + Skills + MCP |
| **操作** | Ingest/Query/Lint | Compile/Report/Lint |
| **索引** | index.md + log.md | 未明确提及 |
| **CLI 工具** | qmd（推荐） | MCP for Obsidian |
| **本地运行** | 提及 Ollama | 详细 Ollama 配置 |
| **Fine-tuning** | 未提及 | 作为终极状态 |
| **实施计划** | 抽象 | 2 天具体计划 |

---

## 🎨 封面图提示词（使用 nano-banana-pro）

### 选项 1：完整循环流程图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Technical Infographic Cutaway (ID: 11165)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a high-resolution professional infographic of Karpathy Method — Claude Skills + Obsidian Complete Loop.

Display the system as a circular flow diagram with 6 stages in a clean, semi-realistic technical illustration style.

Stage 1 (Top) - Raw Capture:
Icon: Web clipper + folder
Label: "raw/ — Capture Everything"
Content: Articles, papers, repos, transcripts, images
Note: "Don't organize. Just capture."

Stage 2 - LLM Compile:
Icon: LLM brain + markdown files
Label: "wiki/ — LLM Compiles"
Content: Concepts, backlinks, summaries, index pages
Note: "LLM owns this layer"

Stage 3 - Obsidian Navigate:
Icon: Graph view + backlinks
Label: "Obsidian — Knowledge IDE"
Features: Graph view, backlinks, Dataview, Marp
Note: "Human reads; LLM writes"

Stage 4 - Query:
Icon: Question bubble + search
Label: "Ask Complex Questions"
Example: "Using my wiki, explain edge strategies"
Note: "1M token context windows"

Stage 5 - Report:
Icon: Markdown document
Label: "reports/ — Answers as Files"
Formats: Reports, Marp slides, PNG diagrams
Note: "Every query = permanent asset"

Stage 6 - Lint:
Icon: Health check + wrench
Label: "Weekly Lint Pass"
Checks: Contradictions, orphans, duplicates, unsourced claims
Note: "Zero manual bookkeeping"

Center Badge:
"LLM as Compiler & Librarian"
"Not Chatbot"
"Knowledge Compounds Weekly"

Tools Row (bottom):
Obsidian | Claude Code | Skills | MCP | Ollama (local)

Headline: "Karpathy Method — Second Brain That Writes With You"
Subhead: "Set up this weekend. Compound forever."

Badge: "5000+ Stars" "Karpathy 2026"

Background: Clean white or light neutral tone
Lighting: Neutral studio lighting with soft shadows
Typography: Modern sans-serif with clear hierarchy
Style: Professional educational infographic, 4K resolution
Aspect ratio: 9:16 portrait
```

---

### 选项 2：Stateless vs Stateful 对比风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Premium liquid glass Bento grid (ID: 6847)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Input Variable: Stateless AI vs Stateful Knowledge Base
Language: English

Create a premium liquid glass Bento grid infographic with 6 modules comparing Stateless AI and Stateful LLM Knowledge Base.

Color Palette:
- Stateless: Red/gray tones
- Stateful: Blue/green tones
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow

Module Content (6 Cards):

M1 — Hero: "Stateless vs Stateful" title + comparison icon

M2 — Stateless Flow: 
"Ask → Answer → Close Tab"
"下次会话 = 从零开始"
"永远无积累"

M3 — Stateful Flow:
"Query → Report → File to Wiki"
"今天的答案 = 明天的上下文"
"每周复合"

M4 — Stateless Limitation:
"问微妙问题 = 重新拼凑"
"定义每次不同"
"聊天历史消失"

M5 — Stateful Advantage:
"Wiki 已编译"
"术语规范"
"6 个月 = 私人语料库"

M6 — Real Benefits:
更快 | 更一致 | 更有价值
"文档 + 入职 + 研究 + 幻灯片"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

### 选项 3：MCP 集成架构图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Exploded View Infographic (ID: 11270)  
**示例图**: https://cms-assets.youmind.com/media/1772519703684_klovml_HCbTfBgXQAAtlhh.jpg

```prompt
product design, MCP for Obsidian Architecture, exploded view diagram, white background, three-dimensional, highly detailed showing Claude ↔ Obsidian real-time integration, studio lighting, product photography, best quality, aspect ratio 9:16

Top Layer - Claude Desktop:
Claude chat window with prompts:
"Find all notes mentioning Polymarket"
"Add this idea under 'Methodology' heading"

Middle Layer - MCP Server:
Commands visualization:
- list_files_in_vault
- get_file_contents
- search
- patch_content
- append_content

Bottom Layer - Obsidian Vault:
File structure:
raw/ | wiki/ | reports/
Real-time editing indicators
Graph view in background

Side Badge:
"3.3k Stars" "384 Forks"
"Real-time ↔ Not Copy-Paste"

Style: Clean technical illustration, minimal labels, professional educational infographic
```

---

## 🔧 实施建议

### 对 KilroyContentBot 的启示

#### 短期（1-2 周）
1. **创建 Skills**
   - `/kb-compile`: 读取 summaries/ → 更新 wiki/
   - `/kb-report`: 基于记忆生成报告
   - `/kb-lint`: 每周健康检查

2. **增强文件夹结构**
   - 当前：summaries/ + memory/
   - 添加：wiki/（编译知识）+ reports/（输出）

3. **实施 MCP 集成**
   - 评估 Obsidian MCP 服务器
   - 实现实时读写能力

#### 中期（1 月）
1. **Wiki 编译流程**
   - X 分析 → raw/
   - LLM 编译 → wiki/
   - 反向链接 + 索引

2. **输出格式多样化**
   - Markdown 报告
   - Marp 幻灯片
   - 图表嵌入

3. **Fine-tuning 准备**
   - 追踪高质量内容
   - 准备 fine-tuning 语料库

---

## 📈 关键数据

| 指标 | 数值 |
|------|------|
| X 文章互动 | 未显示（新发布） |
| MCP Obsidian | 3.3k Stars · 384 Forks |
| Karpathy Gist | 5000+ Stars · 2783 Forks |
| 实施时间 | 2 天（周末） |
| Wiki 规模阈值 | ~50-100 篇文章开始复合 |

---

## 📚 相关资源

| 资源 | 链接 |
|------|------|
| Karpathy LLM Wiki Gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| MCP for Obsidian | GitHub (3.3k stars) |
| Obsidian Web Clipper | Obsidian 插件商店 |
| Ollama（本地 LLM） | https://ollama.ai |
| Marp（Markdown 幻灯片） | https://marp.app |

---

*分析完成 | 下一步：推送到 GitHub*
