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
- P1 待执行：
  - 迁移 summaries（6 篇 AI/Agent 文章）
  - 迁移金句库、案例库、数据库
- 更新：index.md（Total pages: 13）
