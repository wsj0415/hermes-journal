# Corey Ganim — Karpathy 第二大脑无代码实现指南

**来源**: https://x.com/coreyganim/status/2041144598446092411  
**作者**: Corey Ganim (@coreyganim)  
**抓取时间**: 2026-04-13 11:35 UTC  
**类型**: X 推文线程/无代码教程  
**标签**: karpathy, second-brain, personal-knowledge-base, no-code, claude-code, obsidian-alternative, wiki-automation, cluade-md

---

## 📊 一句话总结

Corey Ganim 分享 Karpathy 第二大脑的极简无代码实现：3 文件夹架构（raw/wiki/outputs）+CLAUDE.md schema 文件 +4 步实施（创建结构/写 schema/倾倒一切/让 AI 工作），无需特殊软件/数据库/Obsidian 插件，仅文件夹和文本文件，每月健康检查防止错误复合。

---

## 🏷️ 话题标签

#Karpathy #第二大脑 #个人知识库 #无代码 #ClaudeCode #Obsidian 替代 #Wiki 自动化 #CLAUDE MD

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:3 文件夹架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
3-Folder Knowledge Base Architecture diagram.

Layout: Horizontal 3-folder flow showing knowledge processing.

Color Palette:
- raw/: Red (#EF4444)
- wiki/: Green (#10B981)
- outputs/: Blue (#3B82F6)
- Background: Dark gradient

Folder 1 — raw/ 🔴:
图标：杂乱文档
"Your junk drawer"
"Articles / Notes / Screenshots"
"Meeting transcripts / Bookmarks / Research"
"Everything goes here"
"Don't organize it"
"That's the AI's job"
"Never modify these files"

Folder 2 — wiki/ 🟢:
图标：有序笔记网络
"AI writes organized version"
"Summaries / Connections between ideas"
"Topic pages / INDEX.md"
"You never edit by hand"
"AI maintains entirely"
"Every topic = own .md file"
"[[topic-name]] links"

Folder 3 — outputs/ 🔵:
图标：问答 + 报告
"AI-generated content"
"Answers / Reports / Research"
"Generated when you ask questions"
"Save answers back to knowledge base"
"Every question makes next answer better"

Center — CLAUDE.md Schema:
图标：配置文件
"Schema file in root"
"Tells AI what KB is about"
"How to organize it"
"Wiki rules"
"Your interests (3-5 things)"
"Like training manual for new employee"

Bottom Workflow:
"1. Dump everything into raw/"
"2. AI reads raw/, compiles wiki/"
"3. Ask questions → outputs/"
"4. Monthly health check"

Style: Clean architecture diagram, dark mode with folder colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 3 文件夹架构的内容，水平流程图直接展示 raw→wiki→outputs 的知识处理流，比单一架构图更能传达"简单架构"的价值。

---

### 选项 2：实施步骤流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
4-Step Implementation Flow infographic.

Layout: Vertical 4-stage flow showing setup process.

Color Palette:
- Step 1: Blue (#3B82F6)
- Step 2: Purple (#8B5CF6)
- Step 3: Green (#10B981)
- Step 4: Orange (#F97316)
- Background: Dark gradient

Step 1 — Create Structure 🔵:
图标：3 文件夹
"Create project folder anywhere"
"3 subfolders:"
"raw/ — Unprocessed sources"
"wiki/ — AI-organized wiki"
"outputs/ — Generated reports"
"That's entire architecture"

Step 2 — Write Schema 🟣:
图标：CLAUDE.md 文件
"Create CLAUDE.md in root"
"Template includes:"
"What This Is"
"How It's Organized"
"Wiki Rules"
"My Interests (3-5 things)"
"Like training manual"

Step 3 — Dump Everything 🟢:
图标：倾倒文件
"Copy-paste articles → .md/.txt"
"Export notes from any app"
"Save screenshots"
"Meeting notes / Research / Project docs"
"Don't rename anything"
"Don't clean it up"
"15+ raw source files typical"

Step 4 — Let AI Work 🟠:
图标：AI 工作
"Open Claude Code/Cursor"
"Point at project folder"
"Say: Read raw/, compile wiki/"
"Create INDEX.md first"
"One .md per major topic"
"Link related topics"
"Summarize every source"
"Then walk away"

Bottom Usage Loop:
"Ask questions → Save answers → Monthly health check"
"Every question makes next answer better"

Style: Modern implementation flow, dark mode with step colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：问题与答案循环

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "Knowledge Base Usage Loop".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Various loop colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"知识库使用循环"
"每问题让下次答案更好"
Icon: Brain + Loop

M2 — 问问题示例 1:
"Based on everything in wiki/"
"What are 3 biggest gaps in my"
"understanding of [topic]?"
"浮现未知领域"

M3 — 问问题示例 2:
"Compare source A vs source B"
"Where do they disagree on [concept]?"
"发现矛盾点"
"多视角分析"

M4 — 问问题示例 3:
"Write 500-word briefing on [topic]"
"Using only what's in KB"
"生成情境简报"
"带引用答案"

M5 — 保存答案:
"Save answers back to KB"
"Every question compounds"
"Next answer better than last"
"知识复合增长"

M6 — 每月健康检查:
"Review entire wiki/"
"Flag contradictions"
"Find unexplained topics"
"List unsupported claims"
"Suggest 3 new articles"
"Quality control"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心问题

> **你已经拥有建立竞争优势需要的一切。**

**它坐在**:
- 你的书签中
- 笔记应用里
- 忘记的截图中
- 保存从未重读的文章中
- 六个月前的会议笔记中

---

### 真正的问题

> **问题不是收集信息。你已经在做了。问题是你需要时找不到任何它。**

**个人知识库永久修复这个**:
- 你把一切倾倒到一个地方
- 指向 AI 它
- 它将混乱组织成可搜索的 wiki
- 每次使用变得更聪明

**无需特殊软件。无需数据库。仅文件夹和文本文件。**

---

## 3 文件夹架构

### Folder 1: raw/（原始来源）

| 特征 | 说明 |
|------|------|
| **比喻** | 你的杂物抽屉 |
| **内容** | 文章/笔记/截图/会议转录/书签/研究 |
| **规则** | 一切放这里 |
| **组织** | **不要组织它** — 那是 AI 的工作 |
| **修改** | **永不修改这些文件** |

---

### Folder 2: wiki/（维基）

| 特征 | 说明 |
|------|------|
| **内容** | AI 编写的组织版本（摘要/想法间连接/主题页面） |
| **编辑** | **你从不手动编辑这个** |
| **维护** | AI 完全维护 |
| **结构** | 每主题自己.md 文件，用 `[[topic-name]]` 格式链接相关主题 |
| **索引** | 维护 INDEX.md 列出每主题 |

---

### Folder 3: outputs/（输出）

| 特征 | 说明 |
|------|------|
| **内容** | AI 生成的答案/报告/研究 |
| **触发** | 当你对知识库问问题时生成 |
| **复合** | 保存答案回知识库，每问题让下次答案更好 |

---

## CLAUDE.md Schema 文件

**位置**: 项目文件夹根目录

**作用**: 告诉 AI 知识库关于什么和如何组织它

**比喻**: **就像第一天给新员工培训手册。没有它，AI 只是猜测什么重要。有了它，每输出 exactly 按你想要结构化。**

---

### 完整模板

```markdown
# Knowledge Base Schema

## What This Is
A personal knowledge base about [YOUR TOPIC].

## How It's Organized
- raw/ contains unprocessed source material. Never modify these files.
- wiki/ contains the organized wiki. AI maintains this entirely.
- outputs/ contains generated reports, answers, and analyses.

## Wiki Rules
- Every topic gets its own .md file in wiki/
- Every wiki file starts with a one-paragraph summary
- Link related topics using [[topic-name]] format
- Maintain an INDEX.md that lists every topic
- When new raw sources are added, update the relevant wiki articles

## My Interests
[List 3-5 things you want this knowledge base to focus on]
```

---

## 4 步实施

### Step 1: 创建结构

```
在任何电脑上创建项目文件夹。内部创建 3 个子文件夹：
- raw/
- wiki/
- outputs/

就是整个架构。3 文件夹。
```

---

### Step 2: 写 Schema

```
在根目录创建 CLAUDE.md（或 AGENTS.md，名字不重要）
粘贴上面模板
填写你的主题和兴趣
```

---

### Step 3: 倾倒一切

> **这是人们停滞的地方。他们创建文件夹然后盯着空目录。**

**答案**: **倾倒一切。**

**操作**:
- 复制粘贴文章到.md 或.txt 文件
- 从任何你用的应用导出笔记
- 保存截图
- 粘贴会议笔记/研究/项目文档
- **不要重命名任何东西**
- **不要清理它**

**作者实践**:
> 我在内容 pipeline 中保持 15+ 原始来源文件。剪贴的文章/竞争者分解/分析报告。没有它是手动组织的。

---

### Step 4: 让 AI 工作

**打开 Claude Code/Cursor 或任何可读取你文件的 AI 工具**

**指向你的项目文件夹并说**:
```
Read everything in raw/. Compile a wiki in wiki/ following the rules 
in CLAUDE.md. Create an INDEX.md first, then one .md file per major 
topic. Link related topics. Summarize every source.
```

**然后走开。让它工作。**

---

### 完成后你有

- wiki 文件夹充满组织文章
- 你没看到的连接
- 你忘记保存的东西的摘要
- 让一切秒 searchable 的索引

---

## 使用循环

### 何时开始提问

> **一旦 wiki 有 10+ 文章，开始问问题。**

---

### 示例问题 1: 识别知识差距

```
Based on everything in wiki/, what are the three biggest gaps in my 
understanding of [topic]?
```

**作用**: 浮现未知领域

---

### 示例问题 2: 比较来源

```
Compare what source A says about [concept] vs source B. Where do 
they disagree?
```

**作用**: 发现矛盾点，多视角分析

---

### 示例问题 3: 生成简报

```
Write me a 500-word briefing on [topic] using only what's in this 
knowledge base.
```

**作用**: 生成情境简报，带引用答案

---

### 保存答案

> **保存答案回知识库。每问题让下次答案更好。那是循环。**

---

## 每月健康检查

**频率**: 一月一次

**告诉 AI**:
```
Review the entire wiki/ directory. Flag contradictions between 
articles. Find topics mentioned but never explained. List claims 
not backed by a source in raw/. Suggest 3 new articles to fill gaps.
```

**作用**:
- 标记文章间矛盾
- 找到被提及但从未解释的主题
- 列出 raw/ 中没有来源支持的声明
- 建议 3 篇新文章填补空白

---

### 为什么重要

> **这防止错误复合。如果 AI 写有点错而你保存回，下次答案建立在那错误上。健康检查是你的质量控制。**

---

## 无需 Obsidian 插件

> **一半互联网在推销 Obsidian 插件用于这个。你不需要它们。**

**核心洞察**:
> **文件夹.md 文件 + 好 schema 文件 90% 时间胜过花哨工具栈。**

**作者观察**:
> 我看过人们花更多时间配置笔记应用而非实际建立知识库。**停止购物完美工具。开始建立。**

---

## 完整系统总结

> **3 文件夹。1 个 schema 文件。AI 维护一切。就是整个系统。**

**行动呼吁**:
1. 选你的主题
2. 创建文件夹
3. 放入你已经有的
4. 让 AI 做其余

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 文件夹数 | 3 |
| 设置时间 | ~15 分钟 |
| 作者原始文件 | 15+ |
| 开始提问阈值 | 10+ wiki 文章 |
| 健康检查频率 | 每月一次 |
| Karpathy 原文书签 | 41K |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "问题不是收集信息。是你需要时找不到" | 核心痛点 |
| "不要组织它。那是 AI 的工作" | 分工原则 |
| "像第一天给新员工培训手册" | Schema 价值 |
| "每问题让下次答案更好" | 复合机制 |
| "停止购物完美工具。开始建立" | 行动呼吁 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **3 文件夹极简架构** — raw/wiki/outputs 清晰分离
2. **CLAUDE.md schema** — 训练手册式配置
3. **倾倒一切策略** — 无摩擦捕获
4. **使用循环** — 问问题→保存答案→复合
5. **每月健康检查** — 质量控制防错误复合
6. **无需花哨工具** — 文件夹+md 文件足够

### 可实施
- 采用 3 文件夹架构管理内容
- 创建 CLAUDE.md 定义内容组织规则
- 倾倒所有内容到 raw/无需手动组织
- 建立问问题循环复合知识
- 实施每月健康检查
- 避免过度工具化，保持简单

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Corey Ganim 原文 | https://x.com/coreyganim/status/2041144598446092411 |
| Karpathy LLM Wiki Gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Claude Code | https://claude.ai/download |

---

*原始来源：https://x.com/coreyganim/status/2041144598446092411*
