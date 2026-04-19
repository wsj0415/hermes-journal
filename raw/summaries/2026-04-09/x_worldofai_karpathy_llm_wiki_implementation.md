# X 内容分析：使用 Karpathy 的 LLM Wiki 将 Claude Code 变成自进化系统

**来源**: WorldofAI (@intheworldofai)  
**链接**: https://x.com/intheworldofai/status/2041632641716514947  
**类型**: X Article 长文  
**抓取时间**: 2026-04-09 13:18 UTC

---

## 📊 核心洞察

**一句话总结**: 这篇文章分享了如何将 Karpathy 的 LLM Wiki 模式应用到 Claude Code 编程项目中，解决"上下文失忆"问题 — 通过让 LLM 构建并维护一个持久的、自更新的知识库（raw/→wiki/→schema.md），AI 从"一次性代码生成器"变成"领域专家"，随时间推移真正理解项目的架构、组件关系和决策历史。

---

## 🎯 完整翻译

### 问题：上下文失忆

我们大多数人都将 Claude Code 用作强大的结对程序员。

我们粘贴上下文，要求功能或修复，然后获得不错的代码返回。

但下次会话呢？它经常**忘记关键决策**、**重复你已经拒绝的模式**、或**缺乏对你现有组件和业务规则的意识**。

这是 **Context Amnesia（上下文失忆）** — 它扼杀大型项目的动力。

Andrej Karpathy 最近在他的病毒式帖子和附带的 LLM Wiki gist 中分享了一个更好的模式。

---

## 💡 核心理念

不是将 LLM 视为无状态的代码生成器，而是用它构建并维护一个**持久的、自更新的知识库** — 一个相互链接的 Markdown 文件的活的 Wiki。

```
原始来源放入 → LLM 编译、总结、链接、维护一切 → 你的 AI 随时间变得更聪明
```

作者将这个确切的想法应用到他的前端 + CRM 项目中。

他给 Claude Code 提供了：
- React/TypeScript 代码库
- Shadcn/ui 组件
- CRM 需求
- API 规范
- 过去的决策

**接下来发生的是开眼界的**：它构建了一个完全更新的仪表板，拉入了正确的 Shadcn 包，与设计系统保持一致，并持续用新的架构洞察、组件关系和理由更新自己的 wiki。

---

## 🔄 从一次性答案到复合 Wiki

### 传统方式的问题

传统提示或基础 RAG 每次都将原始文档扔给模型。**知识不积累。**

### Karpathy 的 LLM Wiki 改变

| 组件 | 用途 |
|------|------|
| **raw/ 文件夹** | 维护源材料（代码文件、文档、笔记、图像等） |
| **wiki/ 目录** | LLM 增量编译的结构化 Markdown 文件：摘要、实体页面、概念文章、反向链接、索引 |
| **持久 Wiki** | 成为未来工作的主要上下文 |
| **LLM 维护** | 标记矛盾、建议新连接、更新页面、归档输出 |

**结果**: 你的 AI 在项目中发展真正的长期专业知识，而非每次从头开始。

---

## 📈 作者项目中的实际效果

指向 Claude Code 他的前端仓库和 CRM 相关来源后，遵循 LLM Wiki 模式，要求它摄入一切并构建活的知识库。它：

- ✅ **发现并记录所有现有 Shadcn 组件**
- ✅ **为数据模型、用户流和架构决策创建相互链接的页面**
- ✅ **请求完全更新的仪表板时**，它参考 wiki 获取现有模式，选择合适的 Shadcn 包，确保一致性，然后用新实现细节、组件关系和理由更新 wiki
- ✅ **多次会话后**，输出持续变得更聪明 — 它开始基于早期决策主动建议改进并捕获潜在不一致

> **感觉像与一位资深工程师合作，他深刻内化了整个项目并积极演化其理解。**

---

## 🛠️ 逐步设置指南（可复制粘贴）

以下是确切如何复制这个（开始需 ~5-15 分钟，然后复合）：

### Step 1: 创建文件夹结构

为你的 LLM Wiki 选择专用目录（建议与主代码仓库分开以保持干净）：

```
my-llm-wiki/
├── raw/              # 将所有源材料放在这里
│                   # （代码文件、PDF、会议笔记、导出的会话、网页剪贴、图像等）
├── wiki/             # 编译的、结构化的知识库（LLM 维护）
│   ├── index.md
│   ├── concepts/
│   ├── entities/
│   ├── components/   # 例如 Shadcn 或 React 组件
│   ├── decisions/
│   └── summaries/
└── schema.md         # 你的"wiki 规则"（类似 CLAUDE.md）— 对一致性至关重要
```

---

### Step 2: 从 Karpathy 的想法文件开始

前往 gist：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

复制全部内容。将其粘贴到新的 Claude Code 会话中作为起始提示。告诉 Claude：

```
"基于这个想法文件为我构建一个完整的 LLM Wiki 系统。
我用 Obsidian 查看。
如需要创建文件夹结构，定义一个好的 schema.md，
并给我关于如何摄入来源和让你维护 wiki 的清晰逐步指令。"
```

---

### Step 3: 定义你的 Schema（schema.md）

这是 LLM 应该如何行为的"宪法"。包括：

- 文件夹约定
- 页面命名规则
- 如何处理反向链接和引用
- 何时以及如何更新现有页面
- 风格指南（如：始终包含对原始来源的引用）
- 你的领域的具体细节（如："对于前端组件，记录 props、Shadcn 依赖和用法示例"）

**让 Claude 帮助起草并随时间演化这个文件。**

---

### Step 4: 摄入你的来源

将文件放入 raw/ 文件夹（代码、文档、截图、导出的聊天会话等）。然后在项目上下文中提示 Claude：

```
"从 raw/ 摄入新来源并编译/更新 wiki。
创建或更新相关页面，带摘要、反向链接和与现有知识的连接。
然后向我显示变更摘要。"
```

**一次开始一个或几个来源**，这样你可以审查和指导。一旦模式建立，你可以批量更多。

---

### Step 5: 工作 + 演化系统

对于编码任务，添加这个重复指令：

```
"首先咨询 wiki/ 获取相关上下文和模式。
完成任务后，用新决策、组件细节和任何学习更新 wiki。"
```

仪表板示例提示：

```
"使用 wiki 作为上下文，为 CRM 构建完全更新的仪表板。
使用适当的 Shadcn 包，与现有组件保持一致，
然后用新架构和关系更新 wiki。"
```

---

### Step 6: 在 Obsidian 中查看和导航

将整个 `my-llm-wiki/` 文件夹作为 vault 打开在 Obsidian 中。

你现在有一个**美丽的、可图视图的知识库**，LLM 做大部分编写和维护工作。

---

### Step 7: 维护和 Lint（自进化部分）

定期运行：

```
"对 wiki 运行健康检查：
找到矛盾、孤立页面、缺失链接或新连接机会。
建议改进并进行更新。"
```

**这是系统真正自进化的地方** — LLM 积极改进自己的知识库。

---

## 🔌 可选增强

| 增强 | 说明 |
|------|------|
| **Claude + Obsidian Memory Stack** | 结合 CLAUDE.md + MCP 获得更强的会话记忆 |
| **自动导出会话** | 添加工具/脚本自动导出 Claude 会话到 raw/ |
| **Obsidian 插件** | Marp（幻灯片）、Dataview 等可视化输出 |
| **索引文件** | 对于更大的 wiki，LLM 维护索引文件和摘要保持查询高效 |

---

## 🎯 收益

**仅几次会话后**，Claude 停止感觉像新鲜实习生，开始表现得像**记住每个先前决策的领域专家**。

仪表板不是通用的 — 它与项目模式深度一致，wiki 现在作为**活文档**，使未来变更更快、更不易出错。

> **这是 Karpathy 强调的转变：从"操作代码"到"操作复合的知识"。**

在 2026 年，最强的 AI 编码设置将不只是有大上下文窗口 — 它们将有**丰富的、自维护的知识库**，使 AI 每天对你的工作真正更聪明。

---

## 📐 与原始 Karpathy Gist 对比

| 维度 | Karpathy Gist | WorldofAI 实施 |
|------|--------------|---------------|
| **焦点** | 通用知识库模式 | 前端 + CRM 编程项目 |
| **工具** | Obsidian（推荐） | Obsidian + Claude Code |
| **来源** | 文章、论文、图像 | 代码文件、Shadcn 组件、API 规范 |
| **Wiki 结构** | 抽象概念/实体 | components/、decisions/、前端具体 |
| **Schema** | CLAUDE.md 风格 | schema.md 带前端具体规则 |
| **输出** | 摘要、比较、幻灯片 | 代码、仪表板、组件文档 |
| **视频指南** | 无 | 有完整设置视频 |

---

## 🎨 封面图提示词（使用 nano-banana-pro）

### 选项 1：自进化系统流程图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Technical Infographic Cutaway (ID: 11165)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a high-resolution professional infographic of LLM Wiki Self-Evolving System for Claude Code.

Display the system as a circular flow diagram showing knowledge compounding cycle in a clean, semi-realistic technical illustration style.

Center Circle - Core Loop:
Icon: LLM brain + wiki pages
Label: "Self-Evolving System"
Text: "From Context Amnesia → Domain Expert"

Stage 1 (Top) - Raw Sources:
Icon: Code files + docs + screenshots
Label: "raw/ — Drop Everything"
Content: React/TS code, Shadcn components, API specs, decisions
Note: "Don't organize. Just capture."

Stage 2 - LLM Compiles:
Icon: Markdown files being created
Label: "wiki/ — LLM Maintains"
Content: Component pages, data models, architecture decisions, backlinks
Note: "LLM writes; You read"

Stage 3 - Work with Context:
Icon: Claude Code + dashboard
Label: "Consult Wiki First"
Task: "Build dashboard using wiki patterns"
Note: "Consistent with existing"

Stage 4 - Update Wiki:
Icon: Wiki pages being updated
Label: "File New Knowledge"
Content: Implementation details, component relationships, rationale
Note: "Compounds over time"

Stage 5 - Lint & Evolve:
Icon: Health check + wrench
Label: "Periodic Lint Pass"
Checks: Contradictions, orphans, missing links, new connections
Note: "Self-improving"

Bottom Section - Results:

Before (Left):
❌ "Context Amnesia"
❌ "Forgets decisions"
❌ "Repeats rejected patterns"
❌ "Fresh intern every session"

After (Right):
✅ "Domain Expert"
✅ "Remembers everything"
✅ "Proactively suggests"
✅ "Senior engineer feel"

Tools Row:
Obsidian | Claude Code | schema.md | raw/ | wiki/

Headline: "Karpathy's LLM Wiki — Self-Evolving Coding System"
Subhead: "5-15 min setup. Compounds forever."

Badge: "Frontend + CRM Project" "Shadcn/ui" "React/TypeScript"

Background: Clean white or light neutral tone
Lighting: Neutral studio lighting with soft shadows
Typography: Modern sans-serif with clear hierarchy
Style: Professional educational infographic, 4K resolution
Aspect ratio: 9:16 portrait
```

---

### 选项 2：前后对比风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Premium liquid glass Bento grid (ID: 6847)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Input Variable: Context Amnesia vs LLM Wiki
Language: English

Create a premium liquid glass Bento grid infographic with 6 modules comparing traditional Claude Code usage vs LLM Wiki pattern.

Color Palette:
- Traditional: Red/gray tones
- LLM Wiki: Blue/green tones
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow

Module Content (6 Cards):

M1 — Hero: "Context Amnesia vs Self-Evolving Wiki" + brain icon

M2 — Traditional Flow: 
"Ask → Code → Close Tab"
"下次会话 = 忘记一切"
"重复拒绝的模式"

M3 — LLM Wiki Flow:
"raw/ → wiki/ → Consult → Update"
"每次会话更聪明"
"记住每个决策"

M4 — Traditional Problem:
"无长期记忆"
"通用输出"
"像新鲜实习生"

M5 — LLM Wiki Advantage:
"持久知识库"
"项目特定专家"
"像资深工程师"

M6 — Real Results:
仪表板深度一致 | 活文档 | 更快变更 | 更少错误

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

### 选项 3：文件夹结构可视化风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Exploded View Infographic (ID: 11270)  
**示例图**: https://cms-assets.youmind.com/media/1772519703684_klovml_HCbTfBgXQAAtlhh.jpg

```prompt
product design, LLM Wiki Folder Structure, exploded view diagram, white background, three-dimensional, showing my-llm-wiki directory tree, studio lighting, product photography, best quality, aspect ratio 9:16

Folder Tree Visualization:

my-llm-wiki/
├── raw/
│   ├── code/ (React, TypeScript files)
│   ├── docs/ (API specs, requirements)
│   ├── notes/ (meeting notes, decisions)
│   └── images/ (screenshots, diagrams)
│
├── wiki/
│   ├── index.md
│   ├── concepts/ (RAG, Shadcn, CRM patterns)
│   ├── entities/ (User, Deal, Pipeline)
│   ├── components/ (Dashboard, Forms, Tables)
│   ├── decisions/ (Architecture, Tech choices)
│   └── summaries/ (Session outputs, reports)
│
└── schema.md (Constitution for LLM behavior)

Annotations:
- raw/: "Immutable sources"
- wiki/: "LLM-written, living knowledge"
- schema.md: "Rules & conventions"

Side Badge:
"5-15 min setup"
"Compounds over sessions"
"Obsidian for viewing"

Style: Clean technical illustration, minimal labels, professional educational infographic
```

---

## 🔧 实施建议

### 对 KilroyContentBot 的启示

#### 短期（1-2 周）
1. **创建 Wiki 结构**
   - 当前：summaries/ + memory/
   - 添加：wiki/（编译知识）+ raw/（原始来源）
   - 创建 schema.md 定义规则

2. **实施摄入流程**
   - X 分析 → raw/
   - LLM 编译 → wiki/
   - 反向链接 + 索引更新

3. **增强会话连续性**
   - 每次会话后更新 running-brief.md
   - 追踪决策和开放问题
   - 避免上下文失忆

#### 中期（1 月）
1. **Schema 演化**
   - 让 Claude 帮助起草 schema.md
   - 定义内容创作约定
   - 多平台适配规则

2. **自进化机制**
   - 每周 Lint 健康检查
   - 查找矛盾、孤立页面
   - 主动建议改进

3. **Obsidian 集成**
   - 评估 MCP for Obsidian
   - 实时读写能力
   - 图视图导航

---

## 📈 关键数据

| 指标 | 数值 |
|------|------|
| 设置时间 | 5-15 分钟 |
| 复合周期 | 每次会话 |
| 效果转变 | 实习生 → 资深工程师 |
| 项目类型 | 前端 + CRM（React/TS/Shadcn） |
| Karpathy Gist | 5000+ Stars · 2783 Forks |

---

## 💬 核心引用

| 引用 | 场景 |
|------|------|
| "上下文失忆扼杀大型项目的动力" | 问题定义 |
| "感觉像与资深工程师合作，他深刻内化了整个项目" | 实际效果 |
| "从操作代码到操作复合的知识" | 核心理念 |
| "2026 年最强的 AI 编码设置将有丰富的、自维护的知识库" | 未来展望 |

---

## 📚 相关资源

| 资源 | 链接 |
|------|------|
| Karpathy LLM Wiki Gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Polydao 完整指南 | https://x.com/polydao/status/2042203352054771748 |
| 12 Claude 用法 | https://x.com/sharbel/status/2041884808809226574 |
| Obsidian Web Clipper | Obsidian 插件商店 |
| MCP for Obsidian | GitHub (3.3k stars) |

---

## 🔧 实施检查清单

### 对 KilroyContentBot 的改进

- [ ] 创建 raw/ 文件夹（原始来源）
- [ ] 创建 wiki/ 文件夹（编译知识）
- [ ] 编写 schema.md（wiki 规则宪法）
- [ ] 实施摄入流程（raw/ → wiki/）
- [ ] 添加反向链接系统
- [ ] 创建 index.md 内容目录
- [ ] 实施每周 Lint 健康检查
- [ ] 会话后更新 running-brief.md
- [ ] 评估 Obsidian MCP 集成
- [ ] 将分析输出归档为 wiki 页面

---

*分析完成 | 下一步：推送到 GitHub*
