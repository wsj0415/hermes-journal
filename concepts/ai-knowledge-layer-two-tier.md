---
title: AI Knowledge Layer 两层系统
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [knowledge-base, agent-architecture, brand-foundation, best-practice]
sources: [raw/articles/shannholmberg-ai-knowledge-layer-2026.md]
# 质量控制
reviewed: false
reviewed_at:
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

# AI Knowledge Layer 两层系统

## 编译知识

本文介绍一个两层系统（动态知识库 KBL + 静态品牌基础 BF），让 AI Agent 输出带有你的声音、数据和品味，20 分钟搭建，随时间自我增强。

**核心架构**：
- KBL（Knowledge Base Layer）：动态增长，Agent 自动编译
- BF（Brand Foundation）：静态不变，仅人类编辑

**关键优势**：
- 编译式方法比 RAG 节省 71.5x token
- 输出带有你的声音和品味
- 20 分钟搭建，随时间复合增长

**适用场景**：
- 内容创作者：编码个人写作风格和内容洞察
- 公司：共享大脑，新成员第一天有生产力
- 个人生活：追踪思考和模式

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/shannholmberg-ai-knowledge-layer-2026]]

---

> **一句话总结**：本文介绍一个两层系统（动态知识库 KBL + 静态品牌基础 BF），让 AI Agent 输出带有你的声音、数据和品味，20 分钟搭建，随时间自我增强。
> 
> 来源：[[raw/articles/shannholmberg-ai-knowledge-layer-2026]]

---

## 核心问题：你的 Agent 不认识你

Karpathy 最近提到他将大部分 token 支出从代码转向知识管理。这篇帖子引起共鸣是因为它命名了每个人都感受到的问题：

**你的 Agent 不认识你。每次对话从零开始。你反复解释你的业务、你的声音、你的目标、你的上下文，输出是通用的因为输入没有记忆。**

作者测试了多种方法，最终简化成一个有效的模式：
- 导入笔记、想法、推文、文章、书签
- Agent 编译成 230+ 结构化 wiki 页面
- 跨链接概念、实体和来源，随时可查询

---

## 什么是 AI Knowledge Layer

AI Knowledge Layer 是坐在你和 Agent 之间的基础设施。**没有它，Agent 猜测；有了它，Agent 知道。**

### 两层架构

| 层级 | 名称 | 特性 | 内容 | 编辑权限 |
|------|------|------|------|----------|
| **Layer 1** | Knowledge Base Layer (KBL) | 动态增长 | 推文、文章、书签、PDF、笔记、语音备忘录 | Agent 自动编译 |
| **Layer 2** | Brand Foundation (BF) | 静态不变 | 声音规则、视觉风格、定位、受众定义、禁用词 | 仅人类编辑 |

**KBL（知识库层）**：
- 你 dump 原始来源到文件夹
- AI Agent 读取所有内容，按类型分类
- 构建结构化 wiki 页面，带交叉引用
- 维护主索引，附带一行摘要便于快速扫描
- 每个问题被归档为新页面
- Wiki 随时间变得更丰富

**BF（品牌基础层）**：
- 只有你编辑的层
- 你的声音规则、视觉风格、定位、受众定义、永不使用的词
- Agent 在生产任何内容前读取，但永不重写
- 这是锚点，即使 Agent 干活，输出听起来仍像你

---

## 为什么不是 RAG

| 方法 | 时间段 | 特点 |
|------|--------|------|
| One-shot RAG | 2020-2023 | 查询时切片文档并搜索 |
| Agentic RAG | 2023-2024 | 多跳检索 |
| **Context Engineering** | 2025+ | Agent 从多来源构建自己的上下文 |

**Knowledge Layer 是第三阶段的基础设施。**

Karpathy 在约 100 篇文章时发现：**编译式方法在 Q&A 上胜过 RAG**。Graphify 测量显示：**每次查询 token 减少 71.5 倍**（相比搜索原始文件）。

---

## 为什么大多数人不搭建

**和大多数人周日不备餐的原因一样**：花 1 小时 upfront 工作，一周节省 10 小时。大多数人宁愿抱怨糟糕的 AI 输出，也不愿花 20 分钟搭建修复它的系统。

**90% 用 AI 的人现在在做同样的事**：prompting → accepting → shipping，没有判断力，没有品味。

**Knowledge Layer 是你离开那 90% 的方式**。它编码你的品味、你的数据、你的模式，让 Agent 产出听起来像你写的东西，而不是任何 AI slop 都能产出的通用内容。

**摩擦是真实的**：你需要策划什么进入。如果某事感觉不到 80%+ 与你正在做的事相关，跳过它。高信号输入让输出更好，填充噪音就得到噪音。

---

## 实践：内容创作者和个人品牌

作者用自己的数据测试：

**初始输入**：
- 坐下来写出脑中所有东西：项目笔记、半成产品想法、对 niche 中有效内容的观察、对 AI 营销走向的思考（原始思考，不关注结构）
- dump X 档案（6 周 87 条推文）、3 篇已发布文章、所有书签

**输出**：
- 15 个主题来源页面
- 14 个概念页面
- 11 个实体页面
- 100+ 交叉链接
- 197 个书签通过 X API 拉取
- Agent 下载 81 张图片，转录 49 个视频
- 分析视觉内容，编织进 wiki

**结果**：笔记、想法、推文、书签、文章全部连接且可搜索。

---

## 两层在实践中的运作

### KBL（知识库层）

存放增长的内容：来源按类型分类（transcript、article、tweet、paper），用 wikilinks 交叉引用，用 TLDR 索引。

**文件夹结构**：
```
wiki/
├── raw/
│   ├── clippings/     ← Obsidian Web Clipper 投放处
│   ├── articles/
│   ├── tweets/
│   └── bookmarks/
├── entities/
├── concepts/
└── index.md
```

**工作流**：
1. 安装 Obsidian Web Clipper 浏览器扩展
2. 浏览 X、读文章、查 GitHub、刷 Reddit 时，一键 clip
3. 保存到 `raw/clippings/`，frontmatter 包含来源 URL
4. 下次运行 `/wiki-ingest`，Agent：
   - 读取 URL
   - 检测来源类型（tweet、article、PDF、video）
   - 排序到正确子文件夹
   - 抓取完整内容
   - 下载所有图片
   - 编译进 wiki

**你白天 clip，Agent 夜间处理，醒来时知识库更丰富。**

### BF（品牌基础层）

存放不变的内容：
- AI 禁用文档（每个标记为 AI 的禁用词、短语、结构列表）
- 视觉内容风格指南（终端截图 + 美丽背景、彩色流程图）
- 声音画像

**每个 Agent 在生产任何内容前读取这些。**

---

## Agent 如何接入

| Agent 类型 | 读取内容 | 功能 |
|-----------|----------|------|
| Writer Agent | BF（声音）+ Wiki（主题研究）+ 内容表现数据 | 选择正确格式写作 |
| Researcher Agent | X、Reddit、YouTube 信号 | 监控新来源，feed 进 raw 文件夹，扩展 wiki 主题 |
| Content Strategist | Wiki + niche 表现数据 | 交叉引用现有覆盖，识别缺口 |

**每个 Agent 的质量取决于它读取的 Knowledge Layer。**

- 薄知识库的 Agent 产出 slop
- 读取 200+ 结构化 wiki 页面（你的声音、数据、表现历史）的 Agent 产出听起来像你的作品

**测试结果**：Helena（AI 营销工具）可以仅从 URL 分析品牌，生成准确的品牌声音画像。但仅凭品牌分析生成的内容是"一分钟产出一个月营销 slop"。**品牌分析不够，需要 Knowledge Layer 叠加。**

---

## 映射到 AI 营销 5 层级

| 层级 | 描述 | Knowledge Layer 状态 |
|------|------|---------------------|
| Level 1 | 自定义 prompts | ❌ 无 Knowledge Layer |
| Level 2 | 手动 skills | ⚠️ 薄 Knowledge Layer |
| Level 3 | Skills + Brand Foundation | ✅ BF 层添加 |
| Level 4 | Agents with skills 读取编译知识 | ✅ KBL + BF 协同工作 |
| Level 5 | 自主 Agent 团队 + 完整复合 Knowledge Layer | ✅ 完全体 |

**大多数人停留在 Level 1 或 2。Knowledge Layer 是带你到 4 和 5 的东西。**

---

## 分发角度

**Vibe coding 解决了构建**：每个人都能在 48 小时内发布应用。**分发仍然困难。**

Knowledge Layer 是你复合分发智能的方式：
- 每个内容洞察被捕获
- 每个书签被分析
- 每个表现指标被追踪
- 让下一块内容定位更精准

**定时触发器每天早晨运行 ingest**，处理你前一天 clip 的内容。**分发在你睡觉时变聪明。**

### 服务机会

为别人搭建 Knowledge Layer 是 **$1,500-3,000 一次性 + $300-500 月费** 的服务。10 个客户 = 第一年 $56,800。这是可产品化的技能。

---

## 公司和项目规模

相同架构适用于公司尺度。区别在于：
- 多人的 Agent 读取和写入同一个 Knowledge Layer
- 层持有操作知识，不只是内容知识

**案例**：

**EspressioAI**：
- 知识库包含客户交付模式、Agent 架构模板、内部 SOP

**Lunar Strategy**：
- 包含活动 playbook、客户研究、内容框架
- 新成员将 Agent 指向知识库，**第一天就有生产力**，而不是花几周学习未文档化的工作方式

**Eric Osiu 全公司推广**：
> "个人助理有天花板。解锁点是 role-tuned Agent 通过中央大脑共享上下文。"

- 销售签单后，客户经理的 Agent 已有交接信息
- 内容表现好时，销售 Agent 自动调整外展角度
- **没有信息掉裂缝，因为 Knowledge Layer 接住一切**

---

## 如何扩展

| 规模 | 特点 |
|------|------|
| 1 人 | 个人 wiki |
| 小团队 (5-10 人) | 共享一个知识库 |
| 组织 (50+ 人) | Role-tuned Agent 读取编译情报 |

**每层相同模式**：
1. 原始来源进入
2. Agent 编译结构化页面
3. 交叉引用自动构建
4. 人类通过探索门验证（每页从 unreviewed 开始，只有人类能标记为 confirmed）
5. Git 同步一切，知识版本可控且可逆

**Cody Schneider** 为本地服务企业构建了 10 能力 GTM Agent 集群：
> "没有它，Agent 无法做出好决策。"

他称之为数据仓库，Eric Osiu 称之为共享大脑，Karpathy 称之为 LLM Wiki。**名字不重要，Agent 需要编译的、结构化的知识来做有用工作。**

**极端版本**：Greg Isenberg 称为"ambient businesses"——主要在 Agent 上运行的公司，所有者每隔几天检查一次。

**Medvi 是证明**：$1.8B 年收入运行率，2 名员工，零 VC。AI 处理代码、创意、声音、客服。**Knowledge Layer 是前提条件**。没有它，Agent 需要持续人类指导；有了它，它们从编译的组织智能运作。

---

## 个人生活应用

最被低估的用途。追踪内容表现的系统同样可以追踪你的思考：

**输入**：日记条目、读书笔记、播客亮点、健康指标、目标回顾、凌晨 2 点的随机想法

**处理**：全部进入 `raw/`，Agent 编译成结构化页面

**查询**：
- "我在能量水平中看到什么模式？"
- "上季度我学到了什么关于生产力的东西？"

得到引用你自己数据的答案。答案被归档，下次问题更聪明。

**复合循环**：
- 每个问题让系统更丰富
- 每个来源创建新连接
- 你的好奇心反馈进答案质量

### 质量控制（此处最重要）

**盲目信任 AI 最危险的地方**：

| 控制机制 | 功能 |
|---------|------|
| **Bias Checks** | 每页强制反论点和数据缺口。如果 dump 10 篇都说同样东西的 article，wiki 会注意但也标记图片中缺失什么 |
| **Validation Gate** | 每个 AI 生成页面从 `explored: false` 开始，只有你能标记为 reviewed。你总是知道什么被人类验证过 |
| **Confidence Levels** | 每页标记 high/medium/low/uncertain。Agent 必须诚实地说明知识支持程度 |

**80/20 规则**（来自作者的 three moats 文章）：
- 让 AI 做 80% 的组织、编译、交叉引用
- 将你的品味应用到 20%：策划、验证、只有你能看到的连接
- Knowledge Layer 是你编码品味的方式，让 80% 随时间变好

---

## 20 分钟搭建指南

### Step 1: Clone 仓库（2 分钟）
```bash
git clone github.com/shannhk/llm-wikid
# 作为 Obsidian vault 打开文件夹
```

### Step 2: 运行 Agent（3 分钟）
在文件夹中打开 Claude Code（或任何读取 markdown 和运行 bash 的 Agent）。它读取 `CLAUDE.md`，这是控制一切的 schema。Agent 读取此文件，理解完整 schema，自动 scaffolding wiki 结构。

### Step 3: 填充（10 分钟）
- 从设置请求 X 档案
- 安装 Obsidian Web Clipper 扩展，开始 clip 推文、文章、值得保留的 threads
- 坐下来 10 分钟写出脑中所有东西
- dump 书签，任何感觉 80%+ 相关的进入 `raw/`

### Step 4: 运行 Ingest（5 分钟）
Agent 会：
- 排序 clippings
- 从 URL 抓取完整内容
- 下载并分析图片
- 按类型分类每个来源
- 构建带交叉引用的 wiki 页面
- 每页添加反论点和数据缺口
- 更新主索引

### Step 5: 打开 Graph
打开 Obsidian 的 Graph View。你的想法、你关注的人、你使用的工具、你关心的概念现在链接在视觉网络中。

**尝试查询**：
- "过去一个月我 bookmark 最多的内容主题是什么？" → 显示信号模式
- "[我的主要论点] 的反论点是什么？" → 强制压力测试思考
- "总结我对 [竞争对手/工具/主题] 知道的一切" → 从所有提及来源合成简报
- "我的 wiki 中哪些概念来源最少？" → 显示知识薄弱处和下一步研究方向

**每个答案被归档，wiki 生长。**

---

## 接下来做什么

1. **设置定时触发器**（Claude Dispatch 或 cron）：每天早上运行 `/wiki-ingest`
   - 白天 clip，夜间处理，醒来时知识库更丰富

2. **每周运行 `/wiki-lint`**：
   - 捕获页面间矛盾
   - 陈旧内容
   - 无人链接的孤立页面
   - 不同名称下的重复概念
   - Agent 修复能修的，标记需要你判断的

3. **300+ 页面时安装 qmd**（Tobi Lutke 构建）：
   - 本地混合搜索：BM25 + 向量检索 + LLM re-ranking
   - 有 MCP server，Agent 可将 wiki 作为原生工具搜索

4. **连接其他 Agent**：
   - 读取它的 Writer Agent
   - feed 进它的 Researcher Agent
   - 查询它的 Content Strategist
   - Knowledge Layer 是让所有 Agent 有用的共享大脑

---

## 时间窗口

Karpathy 帖子获得 99,000+ 书签。Graphify 48 小时内发布，获得 27,000+ 书签。多个实现在同一周病毒式传播。**需求显而易见。**

**大多数人会 bookmark，想"这很酷"，然后永不搭建。**

**今天花 20 分钟的人，下个月会有复合知识库**——任何搜索引擎、任何通用 AI prompt 无法复制的东西。它会知道你的声音、你的数据、你的模式、你的品味。

**你等待的每一周都是你无法收回的复合周。**

---

## 相关链接

- [[raw/articles/shannholmberg-ai-knowledge-layer-2026]] - 原始来源
- [[agent-memory-architecture]] - 相关：Agent Memory 架构演进
- [llm-wikid GitHub](https://github.com/shannhk/llm-wikid)
