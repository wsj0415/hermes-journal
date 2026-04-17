# Wiki Log

> 所有 wiki 操作的 chronological 记录。只追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作：ingest, update, query, lint, create, archive, delete
> 当文件超过 500 条条目时，轮换：重命名为 log-YYYY.md，重新开始。

## [2026-04-15] create | Wiki 初始化
- Domain: Hermes Agent 使用日记
- 创建结构：SCHEMA.md, index.md, log.md
- 目录结构：raw/{articles,papers,transcripts,assets}, entities, concepts, comparisons, queries

## [2026-04-15] rename | wiki → hermes-journal
- 用户反馈：wiki 名字太泛，没有描述清楚内容
- 重命名目录：/root/wiki → /root/hermes-journal

## [2026-04-15] ingest | hermes-bailian-api-key-排查指南.md
- 来源：用户提供的 Bailian API Key 配置故障排查文章
- 保存到：raw/articles/hermes-bailian-api-key-排查指南.md
- 内容：完整的 401 错误排查过程、两种解决方案、常见问题 FAQ

## [2026-04-15] sync | GitHub 仓库同步设置
- 创建仓库：https://github.com/wsj0415/hermes-journal
- 添加同步脚本：sync-journal.sh
- 配置 cron 任务：每小时自动同步 (job_id: a785c944a85b)
- 首次推送：4 个文件（SCHEMA.md, index.md, log.md, raw/articles/*.md, sync-journal.sh）

## [2026-04-15] ingest | akshay-pachaar-agent-memory-2026
- 来源：https://x.com/akshay_pachaar/status/2043745099792953508
- 保存到：raw/articles/akshay-pachaar-agent-memory-2026.md
- 创建页面：concepts/agent-memory-architecture.md
- 内容：Agent Memory 架构演进完整分析（Python List → Markdown → 向量搜索 → 图向量混合 → Cognee）
- 更新：index.md（Total pages: 2）

## [2026-04-15] preference | 英文内容处理规范
- 用户要求：ingest 英文来源时
  1. 开头提供一句话总结
  2. 内容翻译成中文
- 已保存到 memory

## [2026-04-15] ingest | shannholmberg-ai-knowledge-layer-2026
- 来源：https://x.com/shannholmberg/status/2044111115878326444
- 保存到：raw/articles/shannholmberg-ai-knowledge-layer-2026.md
- 创建页面：concepts/ai-knowledge-layer-two-tier.md
- 内容：AI Knowledge Layer 两层系统（KBL 动态知识库 + BF 静态品牌基础）
  - 为什么不是 RAG（编译式 vs 查询时检索）
  - 内容创作者/公司/个人生活三种应用场景
  - 20 分钟搭建指南
  - 与 Agent Memory 架构的关联
- 更新：index.md（Total pages: 3）

## [2026-04-15] lint | Wiki 健康检查
- 触发：用户要求检查流程规范性和借鉴价值
- 检查项目：
  - 孤立页面：1 个（ai-knowledge-layer-two-tier，正常新页面）
  - 损坏 wikilinks：4 个（指向 raw 来源，应改为外部链接）
  - 缺少 frontmatter：无
  - 超过 200 行：2 个（agent-memory-architecture 304 行，ai-knowledge-layer-two-tier 365 行）
  - 少于 2 个 wikilinks：无
  - 标签不在 SCHEMA 中：9 个（已更新 SCHEMA 添加）
- 创建页面：queries/wiki-health-check-improvements.md
- 对比分析：两篇文章核心洞察对比表
- 改进建议：8 项（P0-P3 优先级排序）
- 更新：SCHEMA.md（添加架构/内容标签分类）
- 更新：index.md（Total pages: 4）

## [2026-04-15] improve | Validation Gate + Brand Foundation 实施
- P0: Validation Gate ✅
  - 更新 SCHEMA.md frontmatter 模板
  - 添加 reviewed, reviewed_at, confidence, confidence_reason 字段
  - 更新现有页面：agent-memory-architecture.md, ai-knowledge-layer-two-tier.md
- P1: Brand Foundation 层 ✅
  - 创建目录：brand-foundation/
  - 创建文件：
    - banned-words.md - AI 禁用词列表（客服话术、填充词、AI 味短语）
    - voice-profile.md - 声音画像（核心原则、输出格式偏好、长度控制）
    - output-format.md - 输出格式规范（工作流、代码示例、链接规范）
- 更新：index.md（添加 Brand Foundation 分类，Total pages: 7）
- 更新：queries/wiki-health-check-improvements.md（标记已完成项）

## [2026-04-15] cron | 定时任务配置
- 每日健康检查 (lint) ✅
  - job_id: 1f5b328fca1b
  -  schedule: 每天 9:00 AM (UTC+8 下午 5 点)
  - 功能：扫描 wiki 页面，检查孤立/损坏链接/未审查页面等
  - deliver: local（保存到 ~/.hermes/cron/output/）
- 自动同步 GitHub ✅
  - job_id: a785c944a85b
  - schedule: 每小时
  - 功能：检测更改并提交推送
- Ingest 说明
  - 需要用户提供来源（URL/文件）
  - 方案：用户手动提供链接，或存到 raw/clippings/ 由 cron 处理

## [2026-04-15] improve | GBrain 模式借鉴
- Compiled Truth + Timeline ✅
  - 更新 SCHEMA.md：添加页面格式规范
  - 核心思想：编译知识（可更新）+ 时间线（只追加）
  - 优势：快速查阅 + 证据链追溯
- 创建模板文件 ✅
  - references/person-template.md - 人物实体模板
  - references/company-template.md - 公司实体模板
  - references/concept-template.md - 概念页面模板
- 更新现有页面 ✅
  - concepts/agent-memory-architecture.md - 添加编译知识 + 时间线
  - concepts/ai-knowledge-layer-two-tier.md - 添加编译知识 + 时间线
- 更新 index.md ✅
  - 添加 References 分类
  - Total pages: 10

## [2026-04-15] ingest | lufzzliz-hermes-system-prompt-analysis-2026
- 来源：https://x.com/lufzzliz/status/2044258384556556743
- 保存到：raw/articles/lufzzliz-hermes-system-prompt-analysis-2026.md
- 创建页面：concepts/hermes-system-prompt-structure.md
- 内容：Hermes Agent 系统提示词 9 层结构分析
  - 总大小：~36,700 chars（~10K tokens）
  - AGENTS.md 占 50%（截断机制：头 70% + 尾 30%）
  - 优化方案：配置 TERMINAL CWD，减少 5K tokens/对话
  - 工具加载机制：51 个注册，30 个按需加载
- 更新：index.md（Total pages: 11）

## [2026-04-15] migrate | kilroy-cdn 知识库迁移（P0）
- 发现：/root/.openclaw/workspace/kilroy-cdn/ 包含大量有价值内容
- 迁移计划：queries/kilroy-cdn-migration-plan.md
- P0 已完成：
  - 合并禁词库：brand-foundation/banned-words.md
    - 新增 10 条详细示例（AI 写法 vs 人类写法）
    - 来源：kilroy-cdn/writing-materials/05-禁词库.md
  - 创建钩子库：references/hooks-collection.md
    - 8 种爆款开头方式（对话式、反差对比、数字承诺等）
    - 来源：kilroy-cdn/writing-materials/01-钩子库.md
- P1 已完成：
  - ✅ 迁移 summaries（6 篇 AI/Agent 文章）到 raw/articles/
  - ✅ 创建概念页面：
    - concepts/second-brain-karpathy-style.md - Karpathy 风格第二大脑
    - concepts/llm-knowledge-base-complete-guide.md - LLM 知识库完整教程
  - ✅ 迁移写作素材库：
    - references/quotes-collection.md - 金句库（22 条）
    - references/case-studies.md - 案例库（3 个故事）
    - references/industry-data.md - 数据库（15 条数据）
- P2 批量迁移：
  - ✅ 复制 53 篇 raw 来源到 raw/articles/
  - ✅ 创建迁移清单：queries/kilroy-cdn-batch-migration-complete.md
- P3 按需编译：
  - ✅ 第一轮（3 个）：
    - concepts/12-agentic-harness-patterns.md - 12 个代理设计模式
    - concepts/claude-md-three-blocks-learning-system.md - Claude MD 学习系统
    - concepts/ai-engineering-from-scratch.md - AI Engineering 完整课程
  - ✅ 第二轮（3 个）：
    - concepts/agentmemory-persistent-memory.md - AgentMemory 持久记忆系统
    - concepts/how-to-make-money-with-claude-code.md - Claude Code 赚钱指南
    - concepts/llm-wiki-karpathy.md - Karpathy LLM Wiki 原始模式
  - ✅ 第三轮（3 个）：
    - concepts/dario-amodei-ai-career-predictions.md - Dario Amodei AI 职业预测
    - concepts/most-capable-agent-system-prompt.md - 最强 Agent 系统提示词
    - concepts/claude-alternatives-guide.md - Claude 替代方案指南
  - ✅ 第四轮（7 个）：
    - concepts/self-improving-agent-system-prompt.md - 自改进代理系统
    - concepts/openclaw-complete-guide.md - OpenClaw 完整指南
    - concepts/notebooklm-content-factory-workflow.md - NotebookLM 内容工厂
    - concepts/cli-design-for-agents-and-humans.md - CLI 设计指南
    - concepts/awesome-openclaw-tips.md - OpenClaw 26 个技巧
   163|    - concepts/visual-explainer.md - Visual Explainer（终结 ASCII 艺术）
   164|    - concepts/llm-council-method-karpathy.md - LLM 委员会方法
   165|
## [2026-04-15] ingest | SMF Semantic Memory Framework (Ashwin Gopinath)
- 来源：https://x.com/ashwingop/status/2044085923185602747
- 保存到：raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md
- 编译 5 个概念页面：
  - concepts/smf-semantic-memory-framework.md - SMF 核心架构（symlink 图谱 + 8 实体类型 + 14 检索通道）
  - concepts/knowledge-base-vs-memory.md - 知识库 vs 记忆系统区别
  - concepts/filesystem-as-knowledge-graph.md - 文件系统即知识图谱
  - concepts/bjork-disuse-theory.md - Bjork 失用理论（记忆生命周期）
  - concepts/memory-utility-function.md - 记忆效用函数（金门大桥思想实验）
- 核心价值：⭐⭐⭐⭐⭐ SMF 是 Karpathy Wiki 的架构演进，解决组织记忆的可扩展性、访问控制、遗忘机制问题

## [2026-04-16] lint | Wiki 健康检查

**扫描范围**: concepts/, entities/, comparisons/, queries/
**扫描页面数**: 29

### 问题摘要
- 高严重性：23 (损坏的 wikilinks)
- 中严重性：49 (无效标签 28 + 页面过长 20 + 链接过少 1)
- 低严重性：28 (未审查页面)
- **总计**: 100 个问题

### 详细问题

#### 高严重性 - 损坏的 Wikilinks (23 个)
指向不存在页面的链接，需要修复或创建目标页面：

| 文件 | 损坏链接 |
|------|----------|
| hermes-system-prompt-structure.md | [[lufzzliz-hermes-system-prompt-analysis-2026]] (2 次) |
| llm-knowledge-base-complete-guide.md | [[wikilinks]] (6 次), [[linked concept]] |
| filesystem-as-knowledge-graph.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| memory-utility-function.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| smf-semantic-memory-framework.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| llm-wiki-karpathy.md | [[wikilinks]] |
| knowledge-base-vs-memory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| bjork-disuse-theory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| second-brain-karpathy-style.md | [[second-brain-part2-system]] |
| agent-memory-architecture.md | [[akshay-pachaar-agent-memory-2026]] (3 次) |
| ai-knowledge-layer-two-tier.md | [[shannholmberg-ai-knowledge-layer-2026]] (3 次) |
| kilroy-cdn-migration-plan.md | [[ ]] (空链接，2 次) |

**建议操作**:
1. 将 raw/articles 中的来源文件链接改为正确路径（如 `raw/articles/xxx.md`）
2. 或创建对应的 wiki 页面
3. 或删除无效链接

#### 中严重性 - 无效标签 (28 个)
以下标签不在 SCHEMA.md 分类法中：

| 标签 | 出现文件 |
|------|----------|
| monetization, career | how-to-make-money-with-claude-code.md |
| openclaw, tips | awesome-openclaw-tips.md |
| content-creation, youtube, notebooklm | notebooklm-content-factory-workflow.md |
| decision-making, agent-design, karpathy | llm-council-method-karpathy.md |
| career, ai-trends | dario-amodei-ai-career-predictions.md |
| education, curriculum | ai-engineering-from-scratch.md |
| openclaw, agent-setup | openclaw-complete-guide.md |
| visualization, agent-design, html | visual-explainer.md |
| system-prompt, agent-design | self-improving-agent-system-prompt.md, most-capable-agent-system-prompt.md |
| agent-design | 12-agentic-harness-patterns.md, agentmemory-persistent-memory.md |
| cli, agent-design, ux | cli-design-for-agents-and-humans.md |

**建议操作**: 更新 SCHEMA.md 添加新标签类别，或修改页面使用现有标签

#### 中严重性 - 页面过长 (20 个)
超过 200 行建议拆分的页面：

| 文件 | 行数 |
|------|------|
| awesome-openclaw-tips.md | 474 |
| dario-amodei-ai-career-predictions.md | 412 |
| llm-knowledge-base-complete-guide.md | 402 |
| most-capable-agent-system-prompt.md | 402 |
| ai-knowledge-layer-two-tier.md | 396 |
| cli-design-for-agents-and-humans.md | 356 |
| claude-md-three-blocks-learning-system.md | 348 |
| 12-agentic-harness-patterns.md | 338 |
| agent-memory-architecture.md | 330 |
| how-to-make-money-with-claude-code.md | 333 |
| openclaw-complete-guide.md | 306 |
| claude-alternatives-guide.md | 307 |
| second-brain-karpathy-style.md | 301 |
| llm-council-method-karpathy.md | 294 |
| llm-wiki-karpathy.md | 267 |
| agentmemory-persistent-memory.md | 248 |
| visual-explainer.md | 242 |
| notebooklm-content-factory-workflow.md | 254 |
| ai-engineering-from-scratch.md | 223 |
| wiki-health-check-improvements.md | 212 |

**建议操作**: 按主题拆分为子页面，添加交叉链接

#### 中严重性 - 链接过少 (1 个)
- kilroy-cdn-batch-migration-complete.md: 只有 1 个 wikilink

**建议操作**: 添加更多相关页面链接

#### 低严重性 - 未审查页面 (28 个)
所有 concepts/ 和 queries/ 下的页面 reviewed 均为 false

**建议操作**: 人工审查后设置 reviewed: true 和 reviewed_at 日期

### 自动修复
- 无自动修复执行（需要人工审查标签和链接修复）

---


---

## Wiki Health Check - 2026-04-17 09:04:25


Generated: 2026-04-17 09:04:25

## Summary
Total pages scanned: 30
Total issues found: 100

## 损坏的 wikilinks (23 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[person-template]]
- 建议: 链接 [[person-template]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[hooks-collection]]
- 建议: 链接 [[hooks-collection]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[banned-words]]
- 建议: 链接 [[banned-words]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[concept-template]]
- 建议: 链接 [[concept-template]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[case-studies]]
- 建议: 链接 [[case-studies]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[quotes-collection]]
- 建议: 链接 [[quotes-collection]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[output-format]]
- 建议: 链接 [[output-format]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[company-template]]
- 建议: 链接 [[company-template]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[voice-profile]]
- 建议: 链接 [[voice-profile]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/index.md
- 损坏链接: [[industry-data]]
- 建议: 链接 [[industry-data]] 指向不存在的页面，需要创建该页面或移除链接

## 超过 200 行的页面 (20 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (1 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

## 标签不在 SCHEMA 分类法中 (28 个)

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: monetization
- 建议: 标签 'monetization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: tips
- 建议: 标签 'tips' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: content-creation
- 建议: 标签 'content-creation' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: youtube
- 建议: 标签 'youtube' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: notebooklm
- 建议: 标签 'notebooklm' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: decision-making
- 建议: 标签 'decision-making' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: karpathy
- 建议: 标签 'karpathy' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: ai-trends
- 建议: 标签 'ai-trends' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: education
- 建议: 标签 'education' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: curriculum
- 建议: 标签 'curriculum' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: agent-setup
- 建议: 标签 'agent-setup' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: visualization
- 建议: 标签 'visualization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: html
- 建议: 标签 'html' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: cli
- 建议: 标签 'cli' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: ux
- 建议: 标签 'ux' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

## 未审查页面 (28 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at


---

## Wiki Health Check - 2026-04-17 09:05:16


Generated: 2026-04-17 09:05:16

## Summary
Total pages scanned: 40
Total issues found: 123

## 损坏的 wikilinks (28 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 2]]
- 建议: 链接 [[相关概念 2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 1]]
- 建议: 链接 [[相关概念 1]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[人物姓名]]
- 建议: 链接 [[人物姓名]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关人物]]
- 建议: 链接 [[相关人物]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[页面名称]]
- 建议: 链接 [[页面名称]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

## 缺少 frontmatter (3 个)

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 建议: 添加 YAML frontmatter（title, created, updated, type, tags）

### [高] /root/hermes-journal/brand-foundation/banned-words.md
- 建议: 添加 YAML frontmatter（title, created, updated, type, tags）

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 建议: 添加 YAML frontmatter（title, created, updated, type, tags）

## 超过 200 行的页面 (23 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/quotes-collection.md
- 行数: 289
- 建议: 页面有 289 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/hooks-collection.md
- 行数: 235
- 建议: 页面有 235 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/industry-data.md
- 行数: 255
- 建议: 页面有 255 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (4 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/references/hooks-collection.md
- 链接数: 1
- 当前链接: banned-words
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/voice-profile.md
- 链接数: 1
- 当前链接: wikilink
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/banned-words.md
- 链接数: 0
- 建议: 页面只有 0 个 wikilinks，建议至少添加 2 个内部链接

## 标签不在 SCHEMA 分类法中 (30 个)

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: monetization
- 建议: 标签 'monetization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: tips
- 建议: 标签 'tips' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: content-creation
- 建议: 标签 'content-creation' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: youtube
- 建议: 标签 'youtube' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: notebooklm
- 建议: 标签 'notebooklm' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: decision-making
- 建议: 标签 'decision-making' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: karpathy
- 建议: 标签 'karpathy' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: ai-trends
- 建议: 标签 'ai-trends' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: education
- 建议: 标签 'education' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: curriculum
- 建议: 标签 'curriculum' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: agent-setup
- 建议: 标签 'agent-setup' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: visualization
- 建议: 标签 'visualization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: html
- 建议: 标签 'html' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: cli
- 建议: 标签 'cli' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: ux
- 建议: 标签 'ux' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/company-template.md
- 问题标签: company
- 建议: 标签 'company' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/person-template.md
- 问题标签: person
- 建议: 标签 'person' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

## 未审查页面 (35 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/quotes-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/concept-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/case-studies.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/hooks-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/industry-data.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/company-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/person-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at


---

## Wiki Health Check - 2026-04-17 09:06:46


Generated: 2026-04-17 09:06:46

## Summary
Total pages scanned: 40
Total issues found: 120

## 损坏的 wikilinks (28 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 2]]
- 建议: 链接 [[相关概念 2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 1]]
- 建议: 链接 [[相关概念 1]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[人物姓名]]
- 建议: 链接 [[人物姓名]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关人物]]
- 建议: 链接 [[相关人物]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[页面名称]]
- 建议: 链接 [[页面名称]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

## 超过 200 行的页面 (23 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/quotes-collection.md
- 行数: 289
- 建议: 页面有 289 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/hooks-collection.md
- 行数: 235
- 建议: 页面有 235 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/industry-data.md
- 行数: 255
- 建议: 页面有 255 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (4 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/references/hooks-collection.md
- 链接数: 1
- 当前链接: banned-words
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/voice-profile.md
- 链接数: 1
- 当前链接: wikilink
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/banned-words.md
- 链接数: 0
- 建议: 页面只有 0 个 wikilinks，建议至少添加 2 个内部链接

## 标签不在 SCHEMA 分类法中 (30 个)

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: monetization
- 建议: 标签 'monetization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: tips
- 建议: 标签 'tips' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: content-creation
- 建议: 标签 'content-creation' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: youtube
- 建议: 标签 'youtube' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: notebooklm
- 建议: 标签 'notebooklm' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: decision-making
- 建议: 标签 'decision-making' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: karpathy
- 建议: 标签 'karpathy' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: ai-trends
- 建议: 标签 'ai-trends' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: education
- 建议: 标签 'education' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: curriculum
- 建议: 标签 'curriculum' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: agent-setup
- 建议: 标签 'agent-setup' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: visualization
- 建议: 标签 'visualization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: html
- 建议: 标签 'html' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: cli
- 建议: 标签 'cli' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: ux
- 建议: 标签 'ux' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/company-template.md
- 问题标签: company
- 建议: 标签 'company' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/person-template.md
- 问题标签: person
- 建议: 标签 'person' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

## 未审查页面 (35 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/quotes-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/concept-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/case-studies.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/hooks-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/industry-data.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/company-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/person-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at


---

## Wiki Health Check - 2026-04-17 09:06:54


Generated: 2026-04-17 09:06:54

## Summary
Total pages scanned: 40
Total issues found: 120

## 损坏的 wikilinks (28 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 1]]
- 建议: 链接 [[相关概念 1]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 2]]
- 建议: 链接 [[相关概念 2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[人物姓名]]
- 建议: 链接 [[人物姓名]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关人物]]
- 建议: 链接 [[相关人物]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[页面名称]]
- 建议: 链接 [[页面名称]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

## 超过 200 行的页面 (23 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/quotes-collection.md
- 行数: 289
- 建议: 页面有 289 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/hooks-collection.md
- 行数: 235
- 建议: 页面有 235 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/industry-data.md
- 行数: 255
- 建议: 页面有 255 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (4 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/references/hooks-collection.md
- 链接数: 1
- 当前链接: banned-words
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/voice-profile.md
- 链接数: 1
- 当前链接: wikilink
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/banned-words.md
- 链接数: 0
- 建议: 页面只有 0 个 wikilinks，建议至少添加 2 个内部链接

## 标签不在 SCHEMA 分类法中 (30 个)

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: monetization
- 建议: 标签 'monetization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 问题标签: tips
- 建议: 标签 'tips' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: content-creation
- 建议: 标签 'content-creation' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: youtube
- 建议: 标签 'youtube' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 问题标签: notebooklm
- 建议: 标签 'notebooklm' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: decision-making
- 建议: 标签 'decision-making' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 问题标签: karpathy
- 建议: 标签 'karpathy' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: career
- 建议: 标签 'career' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 问题标签: ai-trends
- 建议: 标签 'ai-trends' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: education
- 建议: 标签 'education' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 问题标签: curriculum
- 建议: 标签 'curriculum' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: openclaw
- 建议: 标签 'openclaw' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 问题标签: agent-setup
- 建议: 标签 'agent-setup' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: visualization
- 建议: 标签 'visualization' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 问题标签: html
- 建议: 标签 'html' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: system-prompt
- 建议: 标签 'system-prompt' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: cli
- 建议: 标签 'cli' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 问题标签: ux
- 建议: 标签 'ux' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 问题标签: agent-design
- 建议: 标签 'agent-design' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/company-template.md
- 问题标签: company
- 建议: 标签 'company' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

### [中] /root/hermes-journal/references/person-template.md
- 问题标签: person
- 建议: 标签 'person' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除

## 未审查页面 (35 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/quotes-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/concept-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/case-studies.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/hooks-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/industry-data.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/company-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/person-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at


---

## Wiki Health Check - 2026-04-17 09:07:44


Generated: 2026-04-17 09:07:44

## Summary
Total pages scanned: 40
Total issues found: 90

## 损坏的 wikilinks (28 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 1]]
- 建议: 链接 [[相关概念 1]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 2]]
- 建议: 链接 [[相关概念 2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[人物姓名]]
- 建议: 链接 [[人物姓名]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关人物]]
- 建议: 链接 [[相关人物]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[页面名称]]
- 建议: 链接 [[页面名称]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

## 超过 200 行的页面 (23 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/quotes-collection.md
- 行数: 289
- 建议: 页面有 289 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/hooks-collection.md
- 行数: 235
- 建议: 页面有 235 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/industry-data.md
- 行数: 255
- 建议: 页面有 255 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (4 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/references/hooks-collection.md
- 链接数: 1
- 当前链接: banned-words
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/voice-profile.md
- 链接数: 1
- 当前链接: wikilink
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/banned-words.md
- 链接数: 0
- 建议: 页面只有 0 个 wikilinks，建议至少添加 2 个内部链接

## 未审查页面 (35 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/quotes-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/concept-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/case-studies.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/hooks-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/industry-data.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/company-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/person-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at


---

## Wiki Health Check - 2026-04-17 09:07:53


Generated: 2026-04-17 09:07:53

## Summary
Total pages scanned: 40
Total issues found: 90

## 损坏的 wikilinks (28 个)

### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 损坏链接: [[linked concept]]
- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/memory-utility-function.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 损坏链接: [[wikilinks]]
- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 损坏链接: [[second-brain-part2-system]]
- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 损坏链接: [[ ]]
- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 2]]
- 建议: 链接 [[相关概念 2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[相关概念 1]]
- 建议: 链接 [[相关概念 1]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/concept-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/company-template.md
- 损坏链接: [[人物姓名]]
- 建议: 链接 [[人物姓名]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关人物]]
- 建议: 链接 [[相关人物]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[相关公司]]
- 建议: 链接 [[相关公司]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source]]
- 建议: 链接 [[source]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/references/person-template.md
- 损坏链接: [[source2]]
- 建议: 链接 [[source2]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/voice-profile.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[页面名称]]
- 建议: 链接 [[页面名称]] 指向不存在的页面，需要创建该页面或移除链接

### [高] /root/hermes-journal/brand-foundation/output-format.md
- 损坏链接: [[wikilink]]
- 建议: 链接 [[wikilink]] 指向不存在的页面，需要创建该页面或移除链接

## 超过 200 行的页面 (23 个)

### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 行数: 333
- 建议: 页面有 333 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 行数: 474
- 建议: 页面有 474 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 行数: 254
- 建议: 页面有 254 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 行数: 294
- 建议: 页面有 294 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 行数: 412
- 建议: 页面有 412 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 行数: 223
- 建议: 页面有 223 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 行数: 306
- 建议: 页面有 306 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 行数: 267
- 建议: 页面有 267 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 行数: 307
- 建议: 页面有 307 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/visual-explainer.md
- 行数: 242
- 建议: 页面有 242 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 行数: 402
- 建议: 页面有 402 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 行数: 338
- 建议: 页面有 338 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 行数: 356
- 建议: 页面有 356 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 行数: 248
- 建议: 页面有 248 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 行数: 348
- 建议: 页面有 348 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 行数: 301
- 建议: 页面有 301 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
- 行数: 330
- 建议: 页面有 330 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 行数: 396
- 建议: 页面有 396 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/queries/wiki-health-check-improvements.md
- 行数: 212
- 建议: 页面有 212 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/quotes-collection.md
- 行数: 289
- 建议: 页面有 289 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/hooks-collection.md
- 行数: 235
- 建议: 页面有 235 行，建议拆分为多个子主题页面

### [中] /root/hermes-journal/references/industry-data.md
- 行数: 255
- 建议: 页面有 255 行，建议拆分为多个子主题页面

## 少于 2 个 wikilinks (4 个)

### [中] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 链接数: 1
- 当前链接: kilroy-cdn-migration-plan
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/references/hooks-collection.md
- 链接数: 1
- 当前链接: banned-words
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/voice-profile.md
- 链接数: 1
- 当前链接: wikilink
- 建议: 页面只有 1 个 wikilinks，建议至少添加 2 个内部链接

### [中] /root/hermes-journal/brand-foundation/banned-words.md
- 链接数: 0
- 建议: 页面只有 0 个 wikilinks，建议至少添加 2 个内部链接

## 未审查页面 (35 个)

### [低] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/awesome-openclaw-tips.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-council-method-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/memory-utility-function.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/openclaw-complete-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/llm-wiki-karpathy.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-alternatives-guide.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/visual-explainer.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/self-improving-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/bjork-disuse-theory.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/second-brain-karpathy-style.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/agent-memory-architecture.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/queries/kilroy-cdn-batch-migration-complete.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/quotes-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/concept-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/case-studies.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/hooks-collection.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/industry-data.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/company-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at

### [低] /root/hermes-journal/references/person-template.md
- 建议: 审查页面后将 reviewed 改为 true，并填写 reviewed_at
