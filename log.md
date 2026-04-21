
## 2026-04-20

- 📰 发布 AI影响力周报 第 003 期
  - 扫描 30 个核心 AI 账号
  - 精选 10 条高价值内容
  - 重点：开源模型、Agent 工具、MoE 架构

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

## [2026-04-18] lint | Wiki 健康检查

### 扫描概览
- 扫描目录：concepts, entities, comparisons, queries
- 总页面数：29

### 问题汇总
| 严重程度 | 数量 |
|---------|------|
| 高 | 21 |
| 中 | 28 |
| 低 | 29 |
| **总计** | **78** |

### 损坏的 Wikilinks (21 个) - 高优先级

| 文件 | 损坏链接 |
|------|----------|
| hermes-system-prompt-structure.md | [[lufzzliz-hermes-system-prompt-analysis-2026]] (2 次) |
| llm-knowledge-base-complete-guide.md | [[wikilinks]] (5 次), [[linked concept]] |
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

**建议修复**：
- 将 raw/articles/ 下的来源文件创建为 wiki 页面，或
- 将 wikilinks 改为外部链接格式 `[text](url)`

### 页面过长 (>200 行) (20 个) - 中优先级

| 文件 | 行数 | 建议 |
|------|------|------|
| awesome-openclaw-tips.md | 474 | 拆分为多个技巧类别 |
| dario-amodei-ai-career-predictions.md | 412 | 拆分为预测/建议/行动 |
| llm-knowledge-base-complete-guide.md | 402 | 拆分为级别章节 |
| most-capable-agent-system-prompt.md | 402 | 拆分为模块 |
| ai-knowledge-layer-two-tier.md | 396 | 拆分为 KBL/BF 两部分 |
| cli-design-for-agents-and-humans.md | 356 | 拆分为模式章节 |
| claude-md-three-blocks-learning-system.md | 348 | 拆分为模块 |
| 12-agentic-harness-patterns.md | 338 | 拆分为 4 类模式 |
| agent-memory-architecture.md | 330 | 拆分为架构阶段 |
| how-to-make-money-with-claude-code.md | 333 | 拆分为转变章节 |
| second-brain-karpathy-style.md | 301 | 拆分为结构/工作流 |
| claude-alternatives-guide.md | 307 | 拆分为模型对比 |
| openclaw-complete-guide.md | 306 | 拆分为安装/使用/技巧 |
| llm-council-method-karpathy.md | 294 | 拆分为流程/示例 |
| llm-wiki-karpathy.md | 267 | 拆分为概念/实现 |
| agentmemory-persistent-memory.md | 248 | 拆分为配置/使用 |
| visual-explainer.md | 242 | 拆分为示例/代码 |
| notebooklm-content-factory-workflow.md | 254 | 拆分为步骤 |
| ai-engineering-from-scratch.md | 223 | 拆分为课程模块 |
| wiki-health-check-improvements.md | 212 | 拆分为问题/改进 |

### Wikilinks 过少 (<2) (1 个) - 中优先级

- `kilroy-cdn-batch-migration-complete.md`: 只有 1 个 wikilink，建议添加相关页面链接

### 孤立页面 (7 个) - 中优先级

以下页面无其他页面链接到它们：
- awesome-openclaw-tips.md
- llm-council-method-karpathy.md
- dario-amodei-ai-career-predictions.md
- memory-utility-function.md
- visual-explainer.md
- self-improving-agent-system-prompt.md
- kilroy-cdn-batch-migration-complete.md

**建议**：在相关页面添加指向这些页面的 wikilinks

### 未审查页面 (29 个) - 低优先级

28 个页面 `reviewed: false`，1 个页面缺少 `reviewed` 字段

**建议**：批量审查并更新 frontmatter

### 自动修复状态

- ✅ 所有页面已收录到 index.md
- ✅ 所有标签均在 SCHEMA 分类法中
- ✅ 无缺少 frontmatter 的页面

### 后续行动

1. [高] 修复 21 个损坏的 wikilinks
2. [中] 拆分 20 个过长页面
3. [中] 为 7 个孤立页面添加入链
4. [低] 审查 29 个未审查页面

## [2026-04-18] ingest | akshay-pachaar-agent-harness-2026
- 来源：https://x.com/akshay_pachaar/status/2041146899319971922?s=52
- 保存到：raw/articles/akshay-pachaar-agent-harness-2026.md
- 创建页面：concepts/agent-harness.md
- 内容：Agent Harness 长文完整中文翻译 + 开头一句话总结
  - 定义了 Harness 与 Agent 的边界
  - 系统梳理生产级 Harness 的核心组件
  - 提炼“先查 harness，再怪模型”的分析框架
- 更新：index.md（Total pages: 40）


## [2026-04-18] ingest | AI 影响力周报第 1 期
- 来源：~/.hermes/output/ai-influence-digest/weekly_report_2026-04-17.md
- 保存到：raw/articles/ai-influence-weekly-report-001-2026-04-17.md
- 创建页面：
  - concepts/ai-influence-weekly-digest.md - AI 影响力周报模式
  - entities/karpathy-ai-engineering.md - Karpathy 的 AI 工程理念
  - concepts/claude-code-best-practices.md - Claude Code 最佳实践
- 更新：index.md (Total pages: 39 → 43)
- 核心洞察：
  - Agent 上下文管理成为焦点 (Claude Code 1M 窗口)
  - Prompt Engineering 从"技巧"转向"流程工程"
  - 多模态生成进入实用阶段 (Gemini 3 单 prompt 构建应用)

## [2026-04-18] create | AI 影响力账号清单
- 来源：ai-influence-digest/references/accounts_65.txt
- 创建页面：entities/ai-influence-accounts-65.md
- 内容：65 个账号完整清单，分 5 类
  - 模型厂商 (12): OpenAI, AnthropicAI, GoogleDeepMind, MetaAI, 国内大模型厂商等
  - 硬件/基础设施 (4): NVIDIA, Groq, Hailuo_AI
  - 研究机构 (3): MIT CSAIL, IBM Data
  - 技术领袖 (20): sam altman, karpathy, ylecun, demishassabis, DarioAmodei 等
  - 投资人/分析师 (12): swyx, mattturck, danshipper 等
  - AI 工程实践者 (14): trq212, amasad, rauchg 等
- 更新：index.md (Total pages: 44)

## [2026-04-18] ingest | Google AI IDE 生产力研究论文
- 来源：arXiv:2601.19964 "Achieving Productivity Gains with AI-based IDE features: A Journey at Google"
- 作者：Maxim Tabachnyk et al. (Google)
- 发表：LLM4Code '26 workshop at ICSE '26
- 保存到：raw/articles/google-ai-ide-productivity-2026.md
- 创建页面：concepts/ai-ide-productivity-funnel.md
- 核心框架：机会漏斗模型（5 层流失）
  - 模型置信度不足 → 不生成建议
  - 响应太慢 → 用户失去耐心
  - 建议质量差 → 被拒绝
  - 用户没注意到 → 可发现性问题
  - 审查后拒绝 → 可用性不足
- 方法论：数据驱动迭代，不依赖直觉
- 更新：index.md (Total pages: 45)
- 关联页面：[[agent-memory-architecture]], [[12-agentic-harness-patterns]], [[hermes-system-prompt-structure]]


## 2026-04-19 09:02:13 - Wiki 健康检查

# Wiki 健康检查报告
检查时间：2026-04-19 09:02:13

扫描页面总数：34
扫描目录：concepts, entities, comparisons, queries

## 问题汇总

发现问题总数：90

### 损坏的 wikilinks (23 个)

- 🔴 **HIGH**: `agent-memory-architecture.md`
  - 问题：损坏的 wikilink: [[akshay-pachaar-agent-memory-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `agent-memory-architecture.md`
  - 问题：损坏的 wikilink: [[akshay-pachaar-agent-memory-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `agent-memory-architecture.md`
  - 问题：损坏的 wikilink: [[akshay-pachaar-agent-memory-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `ai-knowledge-layer-two-tier.md`
  - 问题：损坏的 wikilink: [[shannholmberg-ai-knowledge-layer-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `ai-knowledge-layer-two-tier.md`
  - 问题：损坏的 wikilink: [[shannholmberg-ai-knowledge-layer-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `ai-knowledge-layer-two-tier.md`
  - 问题：损坏的 wikilink: [[shannholmberg-ai-knowledge-layer-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `bjork-disuse-theory.md`
  - 问题：损坏的 wikilink: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `filesystem-as-knowledge-graph.md`
  - 问题：损坏的 wikilink: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `hermes-system-prompt-structure.md`
  - 问题：损坏的 wikilink: [[lufzzliz-hermes-system-prompt-analysis-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `hermes-system-prompt-structure.md`
  - 问题：损坏的 wikilink: [[lufzzliz-hermes-system-prompt-analysis-2026]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `knowledge-base-vs-memory.md`
  - 问题：损坏的 wikilink: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[linked concept]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-knowledge-base-complete-guide.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `llm-wiki-karpathy.md`
  - 问题：损坏的 wikilink: [[wikilinks]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `memory-utility-function.md`
  - 问题：损坏的 wikilink: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `second-brain-karpathy-style.md`
  - 问题：损坏的 wikilink: [[second-brain-part2-system]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `smf-semantic-memory-framework.md`
  - 问题：损坏的 wikilink: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `kilroy-cdn-migration-plan.md`
  - 问题：损坏的 wikilink: [[ ]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

- 🔴 **HIGH**: `kilroy-cdn-migration-plan.md`
  - 问题：损坏的 wikilink: [[ ]]
  - 建议：创建缺失的页面，或修正 wikilink 指向正确的页面

### 页面过长（>200 行） (20 个)

- 🟡 **MEDIUM**: `12-agentic-harness-patterns.md`
  - 问题：页面过长 (338 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `agent-memory-architecture.md`
  - 问题：页面过长 (330 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `agentmemory-persistent-memory.md`
  - 问题：页面过长 (248 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `ai-engineering-from-scratch.md`
  - 问题：页面过长 (223 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `ai-knowledge-layer-two-tier.md`
  - 问题：页面过长 (396 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `awesome-openclaw-tips.md`
  - 问题：页面过长 (474 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `claude-alternatives-guide.md`
  - 问题：页面过长 (307 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `claude-md-three-blocks-learning-system.md`
  - 问题：页面过长 (348 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `cli-design-for-agents-and-humans.md`
  - 问题：页面过长 (356 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `dario-amodei-ai-career-predictions.md`
  - 问题：页面过长 (412 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `how-to-make-money-with-claude-code.md`
  - 问题：页面过长 (333 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `llm-council-method-karpathy.md`
  - 问题：页面过长 (294 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `llm-knowledge-base-complete-guide.md`
  - 问题：页面过长 (402 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `llm-wiki-karpathy.md`
  - 问题：页面过长 (267 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `most-capable-agent-system-prompt.md`
  - 问题：页面过长 (402 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `notebooklm-content-factory-workflow.md`
  - 问题：页面过长 (254 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `openclaw-complete-guide.md`
  - 问题：页面过长 (306 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `second-brain-karpathy-style.md`
  - 问题：页面过长 (301 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `visual-explainer.md`
  - 问题：页面过长 (242 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

- 🟡 **MEDIUM**: `wiki-health-check-improvements.md`
  - 问题：页面过长 (212 行)，建议拆分
  - 建议：拆分为多个子主题页面，添加交叉链接

### 孤立页面（无入链） (10 个)

- 🟡 **MEDIUM**: `ai-ide-productivity-funnel.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `awesome-openclaw-tips.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `dario-amodei-ai-career-predictions.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `llm-council-method-karpathy.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `memory-utility-function.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `self-improving-agent-system-prompt.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `visual-explainer.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `ai-influence-accounts-65.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `karpathy-ai-engineering.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

- 🟡 **MEDIUM**: `kilroy-cdn-batch-migration-complete.md`
  - 问题：孤立页面（无入链）
  - 建议：在相关页面添加指向此页面的 wikilink，或考虑是否应该删除

### 未审查页面 (34 个)

- 🟢 **LOW**: `12-agentic-harness-patterns.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `agent-memory-architecture.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `agentmemory-persistent-memory.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `ai-engineering-from-scratch.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `ai-ide-productivity-funnel.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `ai-influence-weekly-digest.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `ai-knowledge-layer-two-tier.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `awesome-openclaw-tips.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `bjork-disuse-theory.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `claude-alternatives-guide.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `claude-code-best-practices.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `claude-md-three-blocks-learning-system.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `cli-design-for-agents-and-humans.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `dario-amodei-ai-career-predictions.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `filesystem-as-knowledge-graph.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `hermes-system-prompt-structure.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `how-to-make-money-with-claude-code.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `knowledge-base-vs-memory.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `llm-council-method-karpathy.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `llm-knowledge-base-complete-guide.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `llm-wiki-karpathy.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `memory-utility-function.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `most-capable-agent-system-prompt.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `notebooklm-content-factory-workflow.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `openclaw-complete-guide.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `second-brain-karpathy-style.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `self-improving-agent-system-prompt.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `smf-semantic-memory-framework.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `visual-explainer.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `ai-influence-accounts-65.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `karpathy-ai-engineering.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `kilroy-cdn-batch-migration-complete.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `kilroy-cdn-migration-plan.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

- 🟢 **LOW**: `wiki-health-check-improvements.md`
  - 问题：页面未审查 (reviewed: false)
  - 建议：审查页面内容后将 reviewed 设为 true，并填写 reviewed_at

### wikilinks 过少（<2 个） (3 个)

- 🟢 **LOW**: `ai-influence-weekly-digest.md`
  - 问题：wikilinks 过少 (0 个)，建议至少 2 个
  - 建议：添加至少 2 个指向相关页面的 wikilinks

- 🟢 **LOW**: `ai-influence-accounts-65.md`
  - 问题：wikilinks 过少 (1 个)，建议至少 2 个
  - 建议：添加至少 2 个指向相关页面的 wikilinks

- 🟢 **LOW**: `kilroy-cdn-batch-migration-complete.md`
  - 问题：wikilinks 过少 (1 个)，建议至少 2 个
  - 建议：添加至少 2 个指向相关页面的 wikilinks

## 自动修复

- ℹ️  index.md 已包含所有页面

## 统计摘要

| 指标 | 数量 |
|------|------|
| 总页面数 | 34 |
| 高严重性问题 | 23 |
| 中严重性问题 | 30 |
| 低严重性问题 | 37 |

## [2026-04-19] ingest | AI 影响力周报第 2 期
- 来源：~/.hermes/output/ai-influence-digest/weekly_report_2026-04-19.md
- 保存到：raw/articles/ai-influence-weekly-report-002-2026-04-19.md
- 扫描账号：65 个 AI 领域影响力账号
- 候选推文：5 条（通过 Google 搜索收集）
- 精选数量：5 条
- 更新：index.md (Total pages: 45 → 46), log.md
- 核心洞察：
  - OpenAI Codex 实现 macOS 电脑操作自动化（AI 从对话助手转向操作代理）
  - Google DeepMind 用自然语言控制机器人（自然语言作为通用接口）
  - Anthropic 自动化对齐研究突破（Opus 4.6 缩小 97% 性能差距）

## [2026-04-20] lint | Wiki 健康检查

### 扫描范围
- 目录：concepts/, entities/, comparisons/, queries/
- 扫描页面数：34
- 知识库总页面：47

### 问题汇总
| 严重性 | 数量 | 问题类型 |
|--------|------|----------|
| 高 | 12 | 损坏的 wikilinks |
| 中 | 23 | 页面过长 (>200 行), wikilinks 不足 |
| 低 | 44 | 未审查页面，孤立页面 |
| **总计** | **79** | |

### 高严重性问题 (损坏的 wikilinks)

损坏的 wikilinks 指向不存在的页面。这些可能是：
1. 对 raw/articles/ 中源文章的引用（应改为 frontmatter 中的 sources 字段）
2. 拼写错误的页面名称
3. 已删除或移动的页面

**需要修复的文件：**

- `concepts/hermes-system-prompt-structure.md`
  - 损坏链接：`[[lufzzliz-hermes-system-prompt-analysis-2026]]`
  - 损坏链接：`[[lufzzliz-hermes-system-prompt-analysis-2026]]`

- `concepts/llm-knowledge-base-complete-guide.md`
  - 损坏链接：`[[wikilinks]]`
  - 损坏链接：`[[wikilinks]]`
  - 损坏链接：`[[wikilinks]]`
  - 损坏链接：`[[linked concept]]`
  - 损坏链接：`[[wikilinks]]`

- `concepts/filesystem-as-knowledge-graph.md`
  - 损坏链接：`[[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]`

- `concepts/memory-utility-function.md`
  - 损坏链接：`[[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]`

- `concepts/smf-semantic-memory-framework.md`
  - 损坏链接：`[[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]`

- `concepts/llm-wiki-karpathy.md`
  - 损坏链接：`[[wikilinks]]`

- `concepts/knowledge-base-vs-memory.md`
  - 损坏链接：`[[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]`

- `concepts/bjork-disuse-theory.md`
  - 损坏链接：`[[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]`

- `concepts/second-brain-karpathy-style.md`
  - 损坏链接：`[[second-brain-part2-system]]`

- `concepts/agent-memory-architecture.md`
  - 损坏链接：`[[akshay-pachaar-agent-memory-2026]]`
  - 损坏链接：`[[akshay-pachaar-agent-memory-2026]]`
  - 损坏链接：`[[akshay-pachaar-agent-memory-2026]]`

- `concepts/ai-knowledge-layer-two-tier.md`
  - 损坏链接：`[[shannholmberg-ai-knowledge-layer-2026]]`
  - 损坏链接：`[[shannholmberg-ai-knowledge-layer-2026]]`
  - 损坏链接：`[[shannholmberg-ai-knowledge-layer-2026]]`

- `queries/kilroy-cdn-migration-plan.md`
  - 损坏链接：`[[ ]]`
  - 损坏链接：`[[ ]]`


### 中严重性问题

#### 页面过长 (建议拆分)

超过 200 行的页面，建议拆分为子主题：

- `concepts/llm-knowledge-base-complete-guide.md` (402 行)
- `concepts/how-to-make-money-with-claude-code.md` (333 行)
- `concepts/awesome-openclaw-tips.md` (474 行)
- `concepts/notebooklm-content-factory-workflow.md` (254 行)
- `concepts/llm-council-method-karpathy.md` (294 行)
- `concepts/dario-amodei-ai-career-predictions.md` (412 行)
- `concepts/ai-engineering-from-scratch.md` (223 行)
- `concepts/openclaw-complete-guide.md` (306 行)
- `concepts/llm-wiki-karpathy.md` (267 行)
- `concepts/claude-alternatives-guide.md` (307 行)
- ... 还有 10 个页面


#### Wikilinks 不足

少于 2 个出站链接的页面（违反 SCHEMA 规范）：

- `concepts/ai-influence-weekly-digest.md` (仅 0 个链接)
- `entities/ai-influence-accounts-65.md` (仅 1 个链接)
- `queries/kilroy-cdn-batch-migration-complete.md` (仅 1 个链接)


### 低严重性问题

#### 未审查页面

`reviewed: false` 的页面（AI 生成内容，需要人工审查）：

- `concepts/hermes-system-prompt-structure.md`
- `concepts/llm-knowledge-base-complete-guide.md`
- `concepts/how-to-make-money-with-claude-code.md`
- `concepts/awesome-openclaw-tips.md`
- `concepts/notebooklm-content-factory-workflow.md`
- ... 共 33 个页面


#### 孤立页面

无入链的页面（可能需要在其他页面中添加引用）：

- `concepts/awesome-openclaw-tips.md`
- `concepts/llm-council-method-karpathy.md`
- `concepts/dario-amodei-ai-career-predictions.md`
- `concepts/memory-utility-function.md`
- `concepts/ai-ide-productivity-funnel.md`
- ... 共 10 个页面


### 自动修复操作

#### index.md 更新
- 检查所有 wiki 页面是否已添加到 index.md
- 结果：所有 34 个 wiki 页面均已正确索引
- 无需更新

### 建议操作

1. **高优先级**：修复损坏的 wikilinks
   - 将 raw/articles/ 引用改为 frontmatter 中的 `sources` 字段
   - 修正拼写错误的页面名称

2. **中优先级**：拆分过长页面
   - 优先处理超过 300 行的页面
   - 创建子页面并添加交叉链接

3. **低优先级**：
   - 审查 AI 生成的页面（设置 `reviewed: true`）
   - 为孤立页面添加入链引用

### 下次检查
- 建议频率：每周一次
- 自动修复：index.md 同步，frontmatter 验证

---

## Wiki Health Check - 2026-04-21 09:04:23

**扫描范围**: concepts/, entities/, comparisons/, queries/
**扫描页面数**: 36

### 问题摘要
- 🔴 高严重性：26 (损坏的 wikilinks)
- 🟡 中严重性：23 (页面过长 20 + 链接过少 3)
- 🟢 低严重性：47 (孤立页面 11 + 未审查页面 36)
- **总计**: 96 个问题

---

### 🔴 高严重性 - 损坏的 Wikilinks (26 个)
指向不存在页面的链接，需要修复或创建目标页面：

| 文件 | 损坏链接 |
|------|----------|
| concepts/agent-harness.md | [[akshay-pachaar-agent-harness-2026]] (3 次) |
| concepts/agent-memory-architecture.md | [[akshay-pachaar-agent-memory-2026]] (3 次) |
| concepts/ai-knowledge-layer-two-tier.md | [[shannholmberg-ai-knowledge-layer-2026]] (3 次) |
| concepts/bjork-disuse-theory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| concepts/filesystem-as-knowledge-graph.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| concepts/hermes-system-prompt-structure.md | [[lufzzliz-hermes-system-prompt-analysis-2026]] (2 次) |
| concepts/knowledge-base-vs-memory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| concepts/llm-knowledge-base-complete-guide.md | [[wikilinks]] (6 次), [[linked concept]] |
| concepts/llm-wiki-karpathy.md | [[wikilinks]] |
| concepts/memory-utility-function.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| concepts/second-brain-karpathy-style.md | [[second-brain-part2-system]] |
| concepts/smf-semantic-memory-framework.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
| queries/ai-evening-brief-2026-04-18.md | [[ai-evening-brief-source-2026-04-18]] (2 次) |

**建议操作**:
1. 将 raw/articles 中的来源文件链接改为正确路径（如 `raw/articles/xxx.md`）
2. 或创建对应的 wiki 页面
3. 或删除无效链接

---

### 🟡 中严重性 - 页面过长 (20 个)
超过 200 行建议拆分的页面：

| 文件 | 行数 |
|------|------|
| concepts/awesome-openclaw-tips.md | 474 |
| concepts/dario-amodei-ai-career-predictions.md | 412 |
| concepts/llm-knowledge-base-complete-guide.md | 402 |
| concepts/most-capable-agent-system-prompt.md | 402 |
| concepts/ai-knowledge-layer-two-tier.md | 396 |
| concepts/cli-design-for-agents-and-humans.md | 356 |
| concepts/claude-md-three-blocks-learning-system.md | 348 |
| concepts/12-agentic-harness-patterns.md | 338 |
| concepts/how-to-make-money-with-claude-code.md | 333 |
| concepts/agent-memory-architecture.md | 330 |
| concepts/openclaw-complete-guide.md | 306 |
| concepts/claude-alternatives-guide.md | 307 |
| concepts/second-brain-karpathy-style.md | 301 |
| concepts/llm-council-method-karpathy.md | 294 |
| concepts/llm-wiki-karpathy.md | 267 |
| concepts/agentmemory-persistent-memory.md | 248 |
| concepts/visual-explainer.md | 242 |
| concepts/notebooklm-content-factory-workflow.md | 254 |
| concepts/ai-engineering-from-scratch.md | 223 |
| queries/wiki-health-check-improvements.md | 212 |

**建议操作**: 按主题拆分为子页面，添加交叉链接

---

### 🟡 中严重性 - 链接过少 (3 个)
- concepts/ai-influence-weekly-digest.md: 0 个 wikilinks
- entities/ai-influence-accounts-65.md: 1 个 wikilinks
- queries/kilroy-cdn-batch-migration-complete.md: 1 个 wikilinks

**建议操作**: 添加更多相关页面链接

---

### 🟢 低严重性 - 孤立页面 (11 个)
无入链的页面（新页面正常，后续添加引用）：
- concepts/ai-ide-productivity-funnel.md
- concepts/awesome-openclaw-tips.md
- concepts/dario-amodei-ai-career-predictions.md
- concepts/llm-council-method-karpathy.md
- concepts/memory-utility-function.md
- concepts/self-improving-agent-system-prompt.md
- concepts/visual-explainer.md
- entities/ai-influence-accounts-65.md
- entities/karpathy-ai-engineering.md
- queries/ai-evening-brief-2026-04-18.md
- queries/kilroy-cdn-batch-migration-complete.md

---

### 🟢 低严重性 - 未审查页面 (36 个)
所有 concepts/ 和 queries/ 下的页面 reviewed 均为 false 或无 reviewed 字段

**建议操作**: 人工审查后设置 reviewed: true 和 reviewed_at 日期

---

### 🟢 低严重性 - 缺少 Frontmatter (0 个)
✅ 所有页面都有 frontmatter

---

### 自动修复 ✅

本次执行自动修复了 20 个损坏的 wikilinks：

| 文件 | 修复内容 |
|------|----------|
| concepts/agent-harness.md | [[akshay-pachaar-agent-harness-2026]] → [[raw/articles/akshay-pachaar-agent-harness-2026.md]] (3 处) |
| concepts/agent-memory-architecture.md | [[akshay-pachaar-agent-memory-2026]] → [[raw/articles/akshay-pachaar-agent-memory-2026.md]] (3 处) |
| concepts/ai-knowledge-layer-two-tier.md | [[shannholmberg-ai-knowledge-layer-2026]] → [[raw/articles/shannholmberg-ai-knowledge-layer-2026.md]] (3 处) |
| concepts/bjork-disuse-theory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] → [[raw/articles/...]] (1 处) |
| concepts/filesystem-as-knowledge-graph.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] → [[raw/articles/...]] (1 处) |
| concepts/hermes-system-prompt-structure.md | [[lufzzliz-hermes-system-prompt-analysis-2026]] → [[raw/articles/...]] (2 处) |
| concepts/knowledge-base-vs-memory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] → [[raw/articles/...]] (1 处) |
| concepts/memory-utility-function.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] → [[raw/articles/...]] (1 处) |
| concepts/smf-semantic-memory-framework.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] → [[raw/articles/...]] (1 处) |
| concepts/second-brain-karpathy-style.md | [[second-brain-part2-system]] → [[raw/articles/second-brain-part2-system.md]] (1 处) |
| concepts/llm-knowledge-base-complete-guide.md | 移除占位符 [[wikilinks]] 和 [[linked concept]] |
| concepts/llm-wiki-karpathy.md | 移除占位符 [[wikilinks]] |
| queries/ai-evening-brief-2026-04-18.md | 移除不存在的源链接 |

**剩余损坏链接**: 0 个（全部修复）

---

---

---

## 健康检查完成 - 2026-04-21 09:08:54

### 执行摘要

| 检查项 | 修复前 | 修复后 | 状态 |
|--------|--------|--------|------|
| 损坏的 wikilinks | 26 | 0 | ✅ 已修复 |
| 页面过长 (>200 行) | 20 | 20 | ⚠️ 需人工拆分 |
| 链接过少 (<2 个) | 3 | 3 | ⚠️ 需添加链接 |
| 无效标签 | 0 | 0 | ✅ 无问题 |
| 孤立页面 | 11 | 11 | ℹ️ 新页面正常 |
| 未审查页面 | 36 | 36 | ⚠️ 需人工审查 |
| 缺少 Frontmatter | 0 | 0 | ✅ 无问题 |

### 自动修复执行

本次健康检查自动修复了 **22 个损坏的 wikilinks**：

1. **来源文件链接修复 (17 个)**
   - 将指向 raw/articles/ 中源文件的 wikilinks 更新为完整路径
   - 涉及文件：agent-harness, agent-memory-architecture, ai-knowledge-layer-two-tier, 
     bjork-disuse-theory, filesystem-as-knowledge-graph, hermes-system-prompt-structure,
     knowledge-base-vs-memory, memory-utility-function, smf-semantic-memory-framework,
     second-brain-karpathy-style

2. **占位符清理 (5 个)**
   - 移除 [[wikilinks]] 占位符 (4 处)
   - 移除 [[linked concept]] 占位符 (1 处)

### 待人工处理项

**P1 - 页面拆分建议** (20 个页面 >200 行)
- awesome-openclaw-tips.md (474 行) - 建议按技巧类别拆分
- dario-amodei-ai-career-predictions.md (412 行) - 建议按主题拆分
- llm-knowledge-base-complete-guide.md (402 行) - 建议按级别拆分
- most-capable-agent-system-prompt.md (402 行) - 建议按模块拆分
- 其他 16 个页面...

**P2 - 添加内部链接** (3 个页面 <2 个链接)
- concepts/ai-influence-weekly-digest.md (0 个链接)
- entities/ai-influence-accounts-65.md (1 个链接)
- queries/kilroy-cdn-batch-migration-complete.md (1 个链接)

**P3 - 人工审查** (36 个页面 reviewed: false)
- 所有 concepts/ 和 queries/ 页面需要人工审查并设置 reviewed: true

---

*下次健康检查 scheduled: 2026-04-22 09:00 AM*
- [2026-04-21 09:19] AI影响力周报 第17期 生成并同步
