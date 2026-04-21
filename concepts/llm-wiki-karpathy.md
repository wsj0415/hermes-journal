---
title: Karpathy LLM Wiki — 用 LLM 构建个人知识库
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [knowledge-base, workflow, best-practice]
sources: [raw/articles/llm-wiki-karpathy.md]
reviewed: false
confidence: high
confidence_reason: 来自 Andrej Karpathy 原始 Gist，内容忠实原文
---

## 编译知识

LLM Wiki 是 Andrej Karpathy 提出的个人知识库构建模式：**LLM 增量构建并维护一个持久的 wiki（结构化的、相互链接的 markdown 文件集合），位于你和原始源之间**。核心创新：知识编译一次，然后保持最新，而非 RAG 式每次查询重新推导。

**来源**：Karpathy 原始 Gist（https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f）

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Andrej Karpathy (@karpathy)

---

## 核心问题

**大多数人的 LLM+ 文档体验是 RAG 模式：**

```
上传文件集合 → LLM 在查询时检索相关块 → 生成答案
```

**问题：**
- ❌ LLM 每次问题都从头重新发现知识
- ❌ 没有积累
- ❌ 问需要综合 5 个文档的微妙问题，LLM 必须找到并拼凑相关片段
- ❌ 没有构建起来的东西

**RAG 系统（NotebookLM、ChatGPT 文件上传等）都这样工作。**

---

## 核心想法

**不是仅在查询时从原始文档检索，LLM 增量构建并维护一个持久的 wiki — 一个结构化的、相互链接的 markdown 文件集合，位于你和原始源之间。**

### 工作流程

```
添加新源
  ↓
LLM 读取它
  ↓
提取关键信息
  ↓
整合到现有 wiki
  ↓
更新实体页面
  ↓
修订主题摘要
  ↓
注意新数据与旧主张的矛盾
  ↓
加强或挑战 evolving 综合
```

**关键区别：**
- ✅ 知识编译一次，然后保持最新
- ✅ 不在每次查询时重新推导
- ✅ wiki 是持久、复合的产物
- ✅ 交叉引用已经在那里
- ✅ 矛盾已经被标记
- ✅ 综合已经反映你读过的一切
- ✅ wiki 随着每个源和每个问题变得更丰富

---

## 分工

| 角色 | 人类负责 | LLM 负责 |
|------|----------|----------|
| ** sourcing** | 源的探索、选择 | 无 |
| **探索** | 方向引导 | 无 |
| **提问** | 问正确的问题 | 无 |
| **总结** | 无 | 所有总结工作 |
| **交叉引用** | 无 | 所有交叉引用 |
| **归档** | 无 | 所有归档 |
| **簿记** | 无 | 所有簿记 |

**实践设置：**
```
LLM 代理（一侧） + Obsidian（另一侧）
  ↓
LLM 根据对话编辑
  ↓
你实时浏览结果
  ↓
跟随链接、检查图视图、阅读更新页面
```

**Obsidian 是 IDE；LLM 是程序员；wiki 是代码库。**

---

## 应用场景

### 1️⃣ 个人

追踪自己的目标、健康、心理学、自我提升：
- 归档日记条目
- 文章、播客笔记
- 随时间建立结构化自我画像

### 2️⃣ 研究

数周或数月深入研究一个主题：
- 阅读论文、文章、报告
- 增量构建综合 wiki
- evolving 论文

### 3️⃣ 读书

逐章归档：
- 为人物、主题、情节线索建立页面
- 它们如何连接
- 结束时拥有丰富的伴侣 wiki

**类比：** 粉丝 wiki（如 [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page)）— 数千个相互链接页面覆盖人物、地点、事件、语言，由志愿者社区多年构建。你可以个人构建类似的东西，LLM 做所有交叉引用和维护。

### 4️⃣ 商业/团队

LLM 维护的内部 wiki：
- 输入：Slack 线程、会议转录、项目文档、客户通话
- 可能有人类审查更新
- wiki 保持最新因为 LLM 做没人想做的维护工作

### 5️⃣ 其他场景

| 场景 | 说明 |
|------|------|
| **竞争分析** | 积累竞争对手知识 |
| **尽职调查** | 结构化调查记录 |
| **旅行计划** | 组织旅行信息 |
| **课程笔记** | 综合课程材料 |
| **爱好深挖** | 任何随时间积累知识的场景 |

---

## 为什么不是 RAG

| 维度 | RAG | LLM Wiki |
|------|-----|----------|
| **知识状态** | 每次查询重新发现 | 持久编译 |
| **交叉引用** | 无 | 自动建立 |
| **矛盾检测** | 无 | 自动标记 |
| **复合效应** | 无 | 每次使用更丰富 |
| **Token 效率** | 低（重复检索） | 高（一次编译） |

**Karpathy 的观察**：
> 在约 100 篇文章后，编译式方法在 Q&A 上胜过 RAG。

---

## 实施步骤

### 第 1 步：设置文件夹结构

```
your-wiki/
├── raw/              # 原始源（只读）
│   ├── articles/
│   ├── papers/
│   └── notes/
├── wiki/             # 编译的 wiki
│   ├── index.md
│   ├── entities/
│   ├── concepts/
│   └── summaries/
└── CLAUDE.md         # 模式文件
```

### 第 2 步：编写 CLAUDE.md

```markdown
# Wiki Schema

## Domain
[你的 wiki 覆盖的主题]

## Conventions
- 文件名：小写，连字符，无空格
- 每个页面以 YAML frontmatter 开头
- 使用 wikilinks 链接（每页至少 2 个）
- 更新时 bump updated 日期

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | summary
tags: [标签]
sources: [raw/articles/来源.md]
---
```

## Tag Taxonomy
[定义你的标签分类法]
```

### 第 3 步：添加第一个源

```
1. 复制一篇文章到 raw/articles/
2. 告诉 LLM："读取 raw/articles/*.md，编译到 wiki/"
3. LLM 创建：
   - 源摘要
   - 概念页面
   - 实体页面
   - 主索引
```

### 第 4 步：开始使用

```
1. 问问题
2. LLM 读取 wiki/ 产生答案
3. 答案归档回 wiki/
4. 下次问题受益于之前工作
```

---

## 与第二大脑对比

| 维度 | Karpathy LLM Wiki | 第二大脑（常见实现） |
|------|-------------------|---------------------|
| **核心理念** | 编译式知识 | 类似 |
| **工具** | Obsidian + LLM | Obsidian + LLM |
| **结构** | raw/ + wiki/ | raw/ + wiki/ + outputs/ |
| **创新点** | 强调编译 vs RAG | 强调简单 |
| **来源** | Karpathy Gist | Nick Spisak 推文 |

**结论**：两者本质相同，Karpathy 更早提出编译式理念。

---

## 关键洞察

1. **编译优于检索** — 知识编译一次，而非每次查询重新发现
2. **分工明确** — 人类策展和提问，LLM 做所有簿记
3. **Obsidian 是 IDE** — 你浏览，LLM 编辑
4. **复合效应** — wiki 随每个源和每个问题变得更丰富
5. **矛盾是特性** — 标记矛盾而非隐藏它们

---

## 相关链接

- [[second-brain-karpathy-style]] - Karpathy 风格第二大脑
- [[llm-knowledge-base-complete-guide]] - LLM 知识库完整教程
- [[claude-md-three-blocks-learning-system]] - Claude MD 三模块学习系统
- [Karpathy 原始 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
