|
|### 2026-04-29 AI影响力周报 第19期
|- 生成周报：/root/.hermes/output/ai-influence-digest/weekly_report_2026-04-29.md
|- 同步到知识库：/root/hermes-journal/raw/articles/ai-influence-weekly-19-2026-04-29.md
|- 创建 wiki 总结：/root/hermes-journal/concepts/ai-influence-weekly-report-19-2026-04-29.md
|- 扫描账号：65 个
|- 精选推文：8 条
|- 核心洞察：AI 编程从"辅助"走向"委托" — Karpathy 确认 Agentic Engineering 范式，Andrew Ng 推出 Spec-Driven Development 课程
|
|
|### 2026-04-23 AI影响力周报 第17期
|- 生成周报：/root/.hermes/output/ai-influence-digest/weekly_report_2026-04-23.md
|- 同步到知识库：/root/hermes-journal/raw/articles/ai-influence-digest-week17-2026-04-23.md
|- 扫描账号：50 个
|- 精选推文：8 条
|
|
|## 2026-04-20
    10|
    11|- 📰 发布 AI 影响力周报 第 003 期
    12|  - 扫描 30 个核心 AI 账号
    13|  - 精选 10 条高价值内容
    14|  - 重点：开源模型、Agent 工具、MoE 架构
    15|
    16|## [2026-04-23] ingest | NeoAI 帖子 + Session Profiles 文档
    17|- 来源 1: @NeoAIForecast X 帖子（关于 agent browser 登录 session 持久化问题）
    18|- 来源 2: Notte Labs Medium 文章 - Session Profiles 概念
    19|- 来源 3: agent-browser.dev Sessions 文档
    20|- 保存到：raw/articles/nottelabs-session-profiles-2026-02.md
    21|- 创建页面：concepts/agent-browser-sessions.md
    22|- 核心发现：Chrome profile 复用 + remote debugging 导入 auth state 两种模式
    23|
    24|## [2026-04-23] ingest | Startup Ideas Podcast - Imran Hermes 深度使用案例
    25|- 来源：The Startup Ideas Podcast @startupideaspod
    26|- 保存到：raw/articles/startup-ideas-pod-hermes-imran-2026-04.md
    27|- 创建页面：
    28|  - entities/imran-hermes-power-user.md
    29|  - concepts/hermes-token-optimization.md（90% 成本降低策略）
    30|  - concepts/hermes-android-deployment.md（Termux + 真实设备）
    31|  - concepts/hermes-best-practices.md（综合官方指南 + 实证经验）
    32|- 核心发现：OpenRouter + 代码化重复任务 = $130/5 天→$10/5 天
    33|
    34|## [2026-04-23] ingest | Kevin Simback - Hermes 完全新手指南
    35|- 来源：Kevin Simback X 帖子 + Hermes Atlas 官方指南
    36|- 保存到：raw/articles/ksimback-hermes-beginners-guide-2026-04.md
    37|- 核心发现：Harness Engineering 理念，学习循环是核心功能
    38|
    39|## [2026-04-22] ingest | REFRAG: Rethinking RAG based Decoding (arxiv:2509.01092)
    40|- 来源：Meta Superintelligence Labs 论文
    41|- 保存到：raw/papers/refrag-2509.01092.md
    42|- 创建页面：concepts/refrag-rag-decoding.md
    43|- 核心发现：30.85× TTFT 加速，16×上下文扩展，无 perplexity 损失
    44|
    45|# Wiki Log

## 2026-04-27 AI影响力周报 第18期
- 生成周报：/root/.hermes/output/ai-influence-digest/weekly_report_2026-04-27.md
- 同步到知识库：/root/hermes-journal/raw/articles/ai-influence-weekly-18-2026-04-27.md
- 创建 wiki 页面：/root/hermes-journal/concepts/ai-influence-weekly-report-18-2026-04-27.md
- 扫描账号：65 个
- 候选推文：约 130+ 条
- 精选推文：8 条
- 核心话题：Spec-Driven Development、静态分析+LLM、Agent 集成、组织 AI 推广

    46|
    47|> 所有 wiki 操作的 chronological 记录。只追加。
    48|> 格式：`## [YYYY-MM-DD] action | subject`
    49|> 操作：ingest, update, query, lint, create, archive, delete
    50|> 当文件超过 500 条条目时，轮换：重命名为 log-YYYY.md，重新开始。
    51|
    52|## [2026-04-15] create | Wiki 初始化
    53|- Domain: Hermes Agent 使用日记
    54|- 创建结构：SCHEMA.md, index.md, log.md
    55|- 目录结构：raw/{articles,papers,transcripts,assets}, entities, concepts, comparisons, queries
    56|
    57|## [2026-04-15] rename | wiki → hermes-journal
    58|- 用户反馈：wiki 名字太泛，没有描述清楚内容
    59|- 重命名目录：/root/wiki → /root/hermes-journal
    60|
    61|## [2026-04-15] ingest | hermes-bailian-api-key-排查指南.md
    62|- 来源：用户提供的 Bailian API Key 配置故障排查文章
    63|- 保存到：raw/articles/hermes-bailian-api-key-排查指南.md
    64|- 内容：完整的 401 错误排查过程、两种解决方案、常见问题 FAQ
    65|
    66|## [2026-04-15] sync | GitHub 仓库同步设置
    67|- 创建仓库：https://github.com/wsj0415/hermes-journal
    68|- 添加同步脚本：sync-journal.sh
    69|- 配置 cron 任务：每小时自动同步 (job_id: a785c944a85b)
    70|- 首次推送：4 个文件（SCHEMA.md, index.md, log.md, raw/articles/*.md, sync-journal.sh）
    71|
    72|## [2026-04-15] ingest | akshay-pachaar-agent-memory-2026
    73|- 来源：https://x.com/akshay_pachaar/status/2043745099792953508
    74|- 保存到：raw/articles/akshay-pachaar-agent-memory-2026.md
    75|- 创建页面：concepts/agent-memory-architecture.md
    76|- 内容：Agent Memory 架构演进完整分析（Python List → Markdown → 向量搜索 → 图向量混合 → Cognee）
    77|- 更新：index.md（Total pages: 2）
    78|
    79|## [2026-04-15] preference | 英文内容处理规范
    80|- 用户要求：ingest 英文来源时
    81|  1. 开头提供一句话总结
    82|  2. 内容翻译成中文
    83|- 已保存到 memory
    84|
    85|## [2026-04-15] ingest | shannholmberg-ai-knowledge-layer-2026
    86|- 来源：https://x.com/shannholmberg/status/2044111115878326444
    87|- 保存到：raw/articles/shannholmberg-ai-knowledge-layer-2026.md
    88|- 创建页面：concepts/ai-knowledge-layer-two-tier.md
    89|- 内容：AI Knowledge Layer 两层系统（KBL 动态知识库 + BF 静态品牌基础）
    90|  - 为什么不是 RAG（编译式 vs 查询时检索）
    91|  - 内容创作者/公司/个人生活三种应用场景
    92|  - 20 分钟搭建指南
    93|  - 与 Agent Memory 架构的关联
    94|- 更新：index.md（Total pages: 3）
    95|
    96|## [2026-04-15] lint | Wiki 健康检查
    97|- 触发：用户要求检查流程规范性和借鉴价值
    98|- 检查项目：
    99|  - 孤立页面：1 个（ai-knowledge-layer-two-tier，正常新页面）
   100|  - 损坏 wikilinks：4 个（指向 raw 来源，应改为外部链接）
   101|  - 缺少 frontmatter：无
   102|  - 超过 200 行：2 个（agent-memory-architecture 304 行，ai-knowledge-layer-two-tier 365 行）
   103|  - 少于 2 个 wikilinks：无
   104|  - 标签不在 SCHEMA 中：9 个（已更新 SCHEMA 添加）
   105|- 创建页面：queries/wiki-health-check-improvements.md
   106|- 对比分析：两篇文章核心洞察对比表
   107|- 改进建议：8 项（P0-P3 优先级排序）
   108|- 更新：SCHEMA.md（添加架构/内容标签分类）
   109|- 更新：index.md（Total pages: 4）
   110|
   111|## [2026-04-15] improve | Validation Gate + Brand Foundation 实施
   112|- P0: Validation Gate ✅
   113|  - 更新 SCHEMA.md frontmatter 模板
   114|  - 添加 reviewed, reviewed_at, confidence, confidence_reason 字段
   115|  - 更新现有页面：agent-memory-architecture.md, ai-knowledge-layer-two-tier.md
   116|- P1: Brand Foundation 层 ✅
   117|  - 创建目录：brand-foundation/
   118|  - 创建文件：
   119|    - banned-words.md - AI 禁用词列表（客服话术、填充词、AI 味短语）
   120|    - voice-profile.md - 声音画像（核心原则、输出格式偏好、长度控制）
   121|    - output-format.md - 输出格式规范（工作流、代码示例、链接规范）
   122|- 更新：index.md（添加 Brand Foundation 分类，Total pages: 7）
   123|- 更新：queries/wiki-health-check-improvements.md（标记已完成项）
   124|
   125|## [2026-04-15] cron | 定时任务配置
   126|- 每日健康检查 (lint) ✅
   127|  - job_id: 1f5b328fca1b
   128|  -  schedule: 每天 9:00 AM (UTC+8 下午 5 点)
   129|  - 功能：扫描 wiki 页面，检查孤立/损坏链接/未审查页面等
   130|  - deliver: local（保存到 ~/.hermes/cron/output/）
   131|- 自动同步 GitHub ✅
   132|  - job_id: a785c944a85b
   133|  - schedule: 每小时
   134|  - 功能：检测更改并提交推送
   135|- Ingest 说明
   136|  - 需要用户提供来源（URL/文件）
   137|  - 方案：用户手动提供链接，或存到 raw/clippings/ 由 cron 处理
   138|
   139|## [2026-04-15] improve | GBrain 模式借鉴
   140|- Compiled Truth + Timeline ✅
   141|  - 更新 SCHEMA.md：添加页面格式规范
   142|  - 核心思想：编译知识（可更新）+ 时间线（只追加）
   143|  - 优势：快速查阅 + 证据链追溯
   144|- 创建模板文件 ✅
   145|  - references/person-template.md - 人物实体模板
   146|  - references/company-template.md - 公司实体模板
   147|  - references/concept-template.md - 概念页面模板
   148|- 更新现有页面 ✅
   149|  - concepts/agent-memory-architecture.md - 添加编译知识 + 时间线
   150|  - concepts/ai-knowledge-layer-two-tier.md - 添加编译知识 + 时间线
   151|- 更新 index.md ✅
   152|  - 添加 References 分类
   153|  - Total pages: 10
   154|
   155|## [2026-04-15] ingest | lufzzliz-hermes-system-prompt-analysis-2026
   156|- 来源：https://x.com/lufzzliz/status/2044258384556556743
   157|- 保存到：raw/articles/lufzzliz-hermes-system-prompt-analysis-2026.md
   158|- 创建页面：concepts/hermes-system-prompt-structure.md
   159|- 内容：Hermes Agent 系统提示词 9 层结构分析
   160|  - 总大小：~36,700 chars（~10K tokens）
   161|  - AGENTS.md 占 50%（截断机制：头 70% + 尾 30%）
   162|  - 优化方案：配置 TERMINAL CWD，减少 5K tokens/对话
   163|  - 工具加载机制：51 个注册，30 个按需加载
   164|- 更新：index.md（Total pages: 11）
   165|
   166|## [2026-04-15] migrate | kilroy-cdn 知识库迁移（P0）
   167|- 发现：/root/.openclaw/workspace/kilroy-cdn/ 包含大量有价值内容
   168|- 迁移计划：queries/kilroy-cdn-migration-plan.md
   169|- P0 已完成：
   170|  - 合并禁词库：brand-foundation/banned-words.md
   171|    - 新增 10 条详细示例（AI 写法 vs 人类写法）
   172|    - 来源：kilroy-cdn/writing-materials/05-禁词库.md
   173|  - 创建钩子库：references/hooks-collection.md
   174|    - 8 种爆款开头方式（对话式、反差对比、数字承诺等）
   175|    - 来源：kilroy-cdn/writing-materials/01-钩子库.md
   176|- P1 已完成：
   177|  - ✅ 迁移 summaries（6 篇 AI/Agent 文章）到 raw/articles/
   178|  - ✅ 创建概念页面：
   179|    - concepts/second-brain-karpathy-style.md - Karpathy 风格第二大脑
   180|    - concepts/llm-knowledge-base-complete-guide.md - LLM 知识库完整教程
   181|  - ✅ 迁移写作素材库：
   182|    - references/quotes-collection.md - 金句库（22 条）
   183|    - references/case-studies.md - 案例库（3 个故事）
   184|    - references/industry-data.md - 数据库（15 条数据）
   185|- P2 批量迁移：
   186|  - ✅ 复制 53 篇 raw 来源到 raw/articles/
   187|  - ✅ 创建迁移清单：queries/kilroy-cdn-batch-migration-complete.md
   188|- P3 按需编译：
   189|  - ✅ 第一轮（3 个）：
   190|    - concepts/12-agentic-harness-patterns.md - 12 个代理设计模式
   191|    - concepts/claude-md-three-blocks-learning-system.md - Claude MD 学习系统
   192|    - concepts/ai-engineering-from-scratch.md - AI Engineering 完整课程
   193|  - ✅ 第二轮（3 个）：
   194|    - concepts/agentmemory-persistent-memory.md - AgentMemory 持久记忆系统
   195|    - concepts/how-to-make-money-with-claude-code.md - Claude Code 赚钱指南
   196|    - concepts/llm-wiki-karpathy.md - Karpathy LLM Wiki 原始模式
   197|  - ✅ 第三轮（3 个）：
   198|    - concepts/dario-amodei-ai-career-predictions.md - Dario Amodei AI 职业预测
   199|    - concepts/most-capable-agent-system-prompt.md - 最强 Agent 系统提示词
   200|    - concepts/claude-alternatives-guide.md - Claude 替代方案指南
   201|  - ✅ 第四轮（7 个）：
   202|    - concepts/self-improving-agent-system-prompt.md - 自改进代理系统
   203|    - concepts/openclaw-complete-guide.md - OpenClaw 完整指南
   204|    - concepts/notebooklm-content-factory-workflow.md - NotebookLM 内容工厂
   205|    - concepts/cli-design-for-agents-and-humans.md - CLI 设计指南
   206|    - concepts/awesome-openclaw-tips.md - OpenClaw 26 个技巧
   207|   163|    - concepts/visual-explainer.md - Visual Explainer（终结 ASCII 艺术）
   208|   164|    - concepts/llm-council-method-karpathy.md - LLM 委员会方法
   209|   165|
   210|## [2026-04-15] ingest | SMF Semantic Memory Framework (Ashwin Gopinath)
   211|- 来源：https://x.com/ashwingop/status/2044085923185602747
   212|- 保存到：raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md
   213|- 编译 5 个概念页面：
   214|  - concepts/smf-semantic-memory-framework.md - SMF 核心架构（symlink 图谱 + 8 实体类型 + 14 检索通道）
   215|  - concepts/knowledge-base-vs-memory.md - 知识库 vs 记忆系统区别
   216|  - concepts/filesystem-as-knowledge-graph.md - 文件系统即知识图谱
   217|  - concepts/bjork-disuse-theory.md - Bjork 失用理论（记忆生命周期）
   218|  - concepts/memory-utility-function.md - 记忆效用函数（金门大桥思想实验）
   219|- 核心价值：⭐⭐⭐⭐⭐ SMF 是 Karpathy Wiki 的架构演进，解决组织记忆的可扩展性、访问控制、遗忘机制问题
   220|
   221|## [2026-04-16] lint | Wiki 健康检查
   222|
   223|**扫描范围**: concepts/, entities/, comparisons/, queries/
   224|**扫描页面数**: 29
   225|
   226|### 问题摘要
   227|- 高严重性：23 (损坏的 wikilinks)
   228|- 中严重性：49 (无效标签 28 + 页面过长 20 + 链接过少 1)
   229|- 低严重性：28 (未审查页面)
   230|- **总计**: 100 个问题
   231|
   232|### 详细问题
   233|
   234|#### 高严重性 - 损坏的 Wikilinks (23 个)
   235|指向不存在页面的链接，需要修复或创建目标页面：
   236|
   237|| 文件 | 损坏链接 |
   238||------|----------|
   239|| hermes-system-prompt-structure.md | [[lufzzliz-hermes-system-prompt-analysis-2026]] (2 次) |
   240|| llm-knowledge-base-complete-guide.md | [[wikilinks]] (6 次), [[linked concept]] |
   241|| filesystem-as-knowledge-graph.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
   242|| memory-utility-function.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
   243|| smf-semantic-memory-framework.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
   244|| llm-wiki-karpathy.md | [[wikilinks]] |
   245|| knowledge-base-vs-memory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
   246|| bjork-disuse-theory.md | [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] |
   247|| second-brain-karpathy-style.md | [[second-brain-part2-system]] |
   248|| agent-memory-architecture.md | [[akshay-pachaar-agent-memory-2026]] (3 次) |
   249|| ai-knowledge-layer-two-tier.md | [[shannholmberg-ai-knowledge-layer-2026]] (3 次) |
   250|| kilroy-cdn-migration-plan.md | [[ ]] (空链接，2 次) |
   251|
   252|**建议操作**:
   253|1. 将 raw/articles 中的来源文件链接改为正确路径（如 `raw/articles/xxx.md`）
   254|2. 或创建对应的 wiki 页面
   255|3. 或删除无效链接
   256|
   257|#### 中严重性 - 无效标签 (28 个)
   258|以下标签不在 SCHEMA.md 分类法中：
   259|
   260|| 标签 | 出现文件 |
   261||------|----------|
   262|| monetization, career | how-to-make-money-with-claude-code.md |
   263|| openclaw, tips | awesome-openclaw-tips.md |
   264|| content-creation, youtube, notebooklm | notebooklm-content-factory-workflow.md |
   265|| decision-making, agent-design, karpathy | llm-council-method-karpathy.md |
   266|| career, ai-trends | dario-amodei-ai-career-predictions.md |
   267|| education, curriculum | ai-engineering-from-scratch.md |
   268|| openclaw, agent-setup | openclaw-complete-guide.md |
   269|| visualization, agent-design, html | visual-explainer.md |
   270|| system-prompt, agent-design | self-improving-agent-system-prompt.md, most-capable-agent-system-prompt.md |
   271|| agent-design | 12-agentic-harness-patterns.md, agentmemory-persistent-memory.md |
   272|| cli, agent-design, ux | cli-design-for-agents-and-humans.md |
   273|
   274|**建议操作**: 更新 SCHEMA.md 添加新标签类别，或修改页面使用现有标签
   275|
   276|#### 中严重性 - 页面过长 (20 个)
   277|超过 200 行建议拆分的页面：
   278|
   279|| 文件 | 行数 |
   280||------|------|
   281|| awesome-openclaw-tips.md | 474 |
   282|| dario-amodei-ai-career-predictions.md | 412 |
   283|| llm-knowledge-base-complete-guide.md | 402 |
   284|| most-capable-agent-system-prompt.md | 402 |
   285|| ai-knowledge-layer-two-tier.md | 396 |
   286|| cli-design-for-agents-and-humans.md | 356 |
   287|| claude-md-three-blocks-learning-system.md | 348 |
   288|| 12-agentic-harness-patterns.md | 338 |
   289|| agent-memory-architecture.md | 330 |
   290|| how-to-make-money-with-claude-code.md | 333 |
   291|| openclaw-complete-guide.md | 306 |
   292|| claude-alternatives-guide.md | 307 |
   293|| second-brain-karpathy-style.md | 301 |
   294|| llm-council-method-karpathy.md | 294 |
   295|| llm-wiki-karpathy.md | 267 |
   296|| agentmemory-persistent-memory.md | 248 |
   297|| visual-explainer.md | 242 |
   298|| notebooklm-content-factory-workflow.md | 254 |
   299|| ai-engineering-from-scratch.md | 223 |
   300|| wiki-health-check-improvements.md | 212 |
   301|
   302|**建议操作**: 按主题拆分为子页面，添加交叉链接
   303|
   304|#### 中严重性 - 链接过少 (1 个)
   305|- kilroy-cdn-batch-migration-complete.md: 只有 1 个 wikilink
   306|
   307|**建议操作**: 添加更多相关页面链接
   308|
   309|#### 低严重性 - 未审查页面 (28 个)
   310|所有 concepts/ 和 queries/ 下的页面 reviewed 均为 false
   311|
   312|**建议操作**: 人工审查后设置 reviewed: true 和 reviewed_at 日期
   313|
   314|### 自动修复
   315|- 无自动修复执行（需要人工审查标签和链接修复）
   316|
   317|---
   318|
   319|
   320|---
   321|
   322|## Wiki Health Check - 2026-04-17 09:04:25
   323|
   324|
   325|Generated: 2026-04-17 09:04:25
   326|
   327|## Summary
   328|Total pages scanned: 30
   329|Total issues found: 100
   330|
   331|## 损坏的 wikilinks (23 个)
   332|
   333|### [高] /root/hermes-journal/concepts/hermes-system-prompt-structure.md
   334|- 损坏链接: [[lufzzliz-hermes-system-prompt-analysis-2026]]
   335|- 建议: 链接 [[lufzzliz-hermes-system-prompt-analysis-2026]] 指向不存在的页面，需要创建该页面或移除链接
   336|
   337|### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
   338|- 损坏链接: [[linked concept]]
   339|- 建议: 链接 [[linked concept]] 指向不存在的页面，需要创建该页面或移除链接
   340|
   341|### [高] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
   342|- 损坏链接: [[wikilinks]]
   343|- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接
   344|
   345|### [高] /root/hermes-journal/concepts/filesystem-as-knowledge-graph.md
   346|- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
   347|- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接
   348|
   349|### [高] /root/hermes-journal/concepts/memory-utility-function.md
   350|- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
   351|- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接
   352|
   353|### [高] /root/hermes-journal/concepts/smf-semantic-memory-framework.md
   354|- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
   355|- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接
   356|
   357|### [高] /root/hermes-journal/concepts/llm-wiki-karpathy.md
   358|- 损坏链接: [[wikilinks]]
   359|- 建议: 链接 [[wikilinks]] 指向不存在的页面，需要创建该页面或移除链接
   360|
   361|### [高] /root/hermes-journal/concepts/knowledge-base-vs-memory.md
   362|- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
   363|- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接
   364|
   365|### [高] /root/hermes-journal/concepts/bjork-disuse-theory.md
   366|- 损坏链接: [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
   367|- 建议: 链接 [[ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]] 指向不存在的页面，需要创建该页面或移除链接
   368|
   369|### [高] /root/hermes-journal/concepts/second-brain-karpathy-style.md
   370|- 损坏链接: [[second-brain-part2-system]]
   371|- 建议: 链接 [[second-brain-part2-system]] 指向不存在的页面，需要创建该页面或移除链接
   372|
   373|### [高] /root/hermes-journal/concepts/agent-memory-architecture.md
   374|- 损坏链接: [[akshay-pachaar-agent-memory-2026]]
   375|- 建议: 链接 [[akshay-pachaar-agent-memory-2026]] 指向不存在的页面，需要创建该页面或移除链接
   376|
   377|### [高] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
   378|- 损坏链接: [[shannholmberg-ai-knowledge-layer-2026]]
   379|- 建议: 链接 [[shannholmberg-ai-knowledge-layer-2026]] 指向不存在的页面，需要创建该页面或移除链接
   380|
   381|### [高] /root/hermes-journal/queries/kilroy-cdn-migration-plan.md
   382|- 损坏链接: [[ ]]
   383|- 建议: 链接 [[ ]] 指向不存在的页面，需要创建该页面或移除链接
   384|
   385|### [高] /root/hermes-journal/index.md
   386|- 损坏链接: [[person-template]]
   387|- 建议: 链接 [[person-template]] 指向不存在的页面，需要创建该页面或移除链接
   388|
   389|### [高] /root/hermes-journal/index.md
   390|- 损坏链接: [[hooks-collection]]
   391|- 建议: 链接 [[hooks-collection]] 指向不存在的页面，需要创建该页面或移除链接
   392|
   393|### [高] /root/hermes-journal/index.md
   394|- 损坏链接: [[banned-words]]
   395|- 建议: 链接 [[banned-words]] 指向不存在的页面，需要创建该页面或移除链接
   396|
   397|### [高] /root/hermes-journal/index.md
   398|- 损坏链接: [[concept-template]]
   399|- 建议: 链接 [[concept-template]] 指向不存在的页面，需要创建该页面或移除链接
   400|
   401|### [高] /root/hermes-journal/index.md
   402|- 损坏链接: [[case-studies]]
   403|- 建议: 链接 [[case-studies]] 指向不存在的页面，需要创建该页面或移除链接
   404|
   405|### [高] /root/hermes-journal/index.md
   406|- 损坏链接: [[quotes-collection]]
   407|- 建议: 链接 [[quotes-collection]] 指向不存在的页面，需要创建该页面或移除链接
   408|
   409|### [高] /root/hermes-journal/index.md
   410|- 损坏链接: [[output-format]]
   411|- 建议: 链接 [[output-format]] 指向不存在的页面，需要创建该页面或移除链接
   412|
   413|### [高] /root/hermes-journal/index.md
   414|- 损坏链接: [[company-template]]
   415|- 建议: 链接 [[company-template]] 指向不存在的页面，需要创建该页面或移除链接
   416|
   417|### [高] /root/hermes-journal/index.md
   418|- 损坏链接: [[voice-profile]]
   419|- 建议: 链接 [[voice-profile]] 指向不存在的页面，需要创建该页面或移除链接
   420|
   421|### [高] /root/hermes-journal/index.md
   422|- 损坏链接: [[industry-data]]
   423|- 建议: 链接 [[industry-data]] 指向不存在的页面，需要创建该页面或移除链接
   424|
   425|## 超过 200 行的页面 (20 个)
   426|
   427|### [中] /root/hermes-journal/concepts/llm-knowledge-base-complete-guide.md
   428|- 行数: 402
   429|- 建议: 页面有 402 行，建议拆分为多个子主题页面
   430|
   431|### [中] /root/hermes-journal/concepts/how-to-make-money-with-claude-code.md
   432|- 行数: 333
   433|- 建议: 页面有 333 行，建议拆分为多个子主题页面
   434|
   435|### [中] /root/hermes-journal/concepts/awesome-openclaw-tips.md
   436|- 行数: 474
   437|- 建议: 页面有 474 行，建议拆分为多个子主题页面
   438|
   439|### [中] /root/hermes-journal/concepts/notebooklm-content-factory-workflow.md
   440|- 行数: 254
   441|- 建议: 页面有 254 行，建议拆分为多个子主题页面
   442|
   443|### [中] /root/hermes-journal/concepts/llm-council-method-karpathy.md
   444|- 行数: 294
   445|- 建议: 页面有 294 行，建议拆分为多个子主题页面
   446|
   447|### [中] /root/hermes-journal/concepts/dario-amodei-ai-career-predictions.md
   448|- 行数: 412
   449|- 建议: 页面有 412 行，建议拆分为多个子主题页面
   450|
   451|### [中] /root/hermes-journal/concepts/ai-engineering-from-scratch.md
   452|- 行数: 223
   453|- 建议: 页面有 223 行，建议拆分为多个子主题页面
   454|
   455|### [中] /root/hermes-journal/concepts/openclaw-complete-guide.md
   456|- 行数: 306
   457|- 建议: 页面有 306 行，建议拆分为多个子主题页面
   458|
   459|### [中] /root/hermes-journal/concepts/llm-wiki-karpathy.md
   460|- 行数: 267
   461|- 建议: 页面有 267 行，建议拆分为多个子主题页面
   462|
   463|### [中] /root/hermes-journal/concepts/claude-alternatives-guide.md
   464|- 行数: 307
   465|- 建议: 页面有 307 行，建议拆分为多个子主题页面
   466|
   467|### [中] /root/hermes-journal/concepts/visual-explainer.md
   468|- 行数: 242
   469|- 建议: 页面有 242 行，建议拆分为多个子主题页面
   470|
   471|### [中] /root/hermes-journal/concepts/most-capable-agent-system-prompt.md
   472|- 行数: 402
   473|- 建议: 页面有 402 行，建议拆分为多个子主题页面
   474|
   475|### [中] /root/hermes-journal/concepts/12-agentic-harness-patterns.md
   476|- 行数: 338
   477|- 建议: 页面有 338 行，建议拆分为多个子主题页面
   478|
   479|### [中] /root/hermes-journal/concepts/cli-design-for-agents-and-humans.md
   480|- 行数: 356
   481|- 建议: 页面有 356 行，建议拆分为多个子主题页面
   482|
   483|### [中] /root/hermes-journal/concepts/agentmemory-persistent-memory.md
   484|- 行数: 248
   485|- 建议: 页面有 248 行，建议拆分为多个子主题页面
   486|
   487|### [中] /root/hermes-journal/concepts/claude-md-three-blocks-learning-system.md
   488|- 行数: 348
   489|- 建议: 页面有 348 行，建议拆分为多个子主题页面
   490|
   491|### [中] /root/hermes-journal/concepts/second-brain-karpathy-style.md
   492|- 行数: 301
   493|- 建议: 页面有 301 行，建议拆分为多个子主题页面
   494|
   495|### [中] /root/hermes-journal/concepts/agent-memory-architecture.md
   496|- 行数: 330
   497|- 建议: 页面有 330 行，建议拆分为多个子主题页面
   498|
   499|### [中] /root/hermes-journal/concepts/ai-knowledge-layer-two-tier.md
   500|- 行数: 396
   501|
---

## 2026-04-28 — Wiki Health Check (Scheduled Lint)

# Wiki Health Check Report
Date: 2026-04-28
Total wiki pages scanned: 43
Directories: concepts, entities, comparisons, queries

**Total issues found: 106**

## Summary

| 类别 | 数量 |
|------|------|
| 孤立页面 | 13 |
| 损坏的 wikilinks | 28 |
| 缺少 frontmatter | 0 |
| 超过 200 行 | 21 |
| 少于 2 个 wikilinks | 4 |
| 无效标签 | 0 |
| 未审查页面 | 40 |

## ❌ 孤立页面（无入链） (13 个问题)

### 🔴 [高] #1
- **文件**: `concepts/agent-browser-sessions.md`
- **basename**: `agent-browser-sessions`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #2
- **文件**: `concepts/ai-ide-productivity-funnel.md`
- **basename**: `ai-ide-productivity-funnel`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #3
- **文件**: `concepts/awesome-openclaw-tips.md`
- **basename**: `awesome-openclaw-tips`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #4
- **文件**: `concepts/dario-amodei-ai-career-predictions.md`
- **basename**: `dario-amodei-ai-career-predictions`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #5
- **文件**: `concepts/llm-council-method-karpathy.md`
- **basename**: `llm-council-method-karpathy`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #6
- **文件**: `concepts/memory-utility-function.md`
- **basename**: `memory-utility-function`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #7
- **文件**: `concepts/refrag-rag-decoding.md`
- **basename**: `refrag-rag-decoding`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #8
- **文件**: `concepts/self-improving-agent-system-prompt.md`
- **basename**: `self-improving-agent-system-prompt`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #9
- **文件**: `concepts/visual-explainer.md`
- **basename**: `visual-explainer`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #10
- **文件**: `entities/ai-influence-accounts-65.md`
- **basename**: `ai-influence-accounts-65`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #11
- **文件**: `entities/karpathy-ai-engineering.md`
- **basename**: `karpathy-ai-engineering`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #12
- **文件**: `queries/ai-evening-brief-2026-04-18.md`
- **basename**: `ai-evening-brief-2026-04-18`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

### 🔴 [高] #13
- **文件**: `queries/kilroy-cdn-batch-migration-complete.md`
- **basename**: `kilroy-cdn-batch-migration-complete`
- **建议**: 添加入链到其他页面，或确认是否应删除/归档

## ❌ 损坏的 wikilinks (28 个问题)

### 🔴 [高] #1
- **文件**: `concepts/agent-browser-sessions.md`
- **link_target**: `nottelabs-session-profiles-2026-02`
- **link_basename**: `nottelabs-session-profiles-2026-02`
- **建议**: 创建页面 nottelabs-session-profiles-2026-02.md 或修正链接

### 🔴 [高] #2
- **文件**: `concepts/agent-browser-sessions.md`
- **link_target**: `nottelabs-session-profiles-2026-02`
- **link_basename**: `nottelabs-session-profiles-2026-02`
- **建议**: 创建页面 nottelabs-session-profiles-2026-02.md 或修正链接

### 🔴 [高] #3
- **文件**: `concepts/agent-browser-sessions.md`
- **link_target**: `hermes-browser-automation`
- **link_basename**: `hermes-browser-automation`
- **建议**: 创建页面 hermes-browser-automation.md 或修正链接

### 🔴 [高] #4
- **文件**: `concepts/agent-harness.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-harness-2026.md`
- **link_basename**: `akshay-pachaar-agent-harness-2026`
- **建议**: 创建页面 akshay-pachaar-agent-harness-2026.md 或修正链接

### 🔴 [高] #5
- **文件**: `concepts/agent-harness.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-harness-2026.md`
- **link_basename**: `akshay-pachaar-agent-harness-2026`
- **建议**: 创建页面 akshay-pachaar-agent-harness-2026.md 或修正链接

### 🔴 [高] #6
- **文件**: `concepts/agent-harness.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-harness-2026.md`
- **link_basename**: `akshay-pachaar-agent-harness-2026`
- **建议**: 创建页面 akshay-pachaar-agent-harness-2026.md 或修正链接

### 🔴 [高] #7
- **文件**: `concepts/agent-memory-architecture.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-memory-2026.md`
- **link_basename**: `akshay-pachaar-agent-memory-2026`
- **建议**: 创建页面 akshay-pachaar-agent-memory-2026.md 或修正链接

### 🔴 [高] #8
- **文件**: `concepts/agent-memory-architecture.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-memory-2026.md`
- **link_basename**: `akshay-pachaar-agent-memory-2026`
- **建议**: 创建页面 akshay-pachaar-agent-memory-2026.md 或修正链接

### 🔴 [高] #9
- **文件**: `concepts/agent-memory-architecture.md`
- **link_target**: `raw/articles/akshay-pachaar-agent-memory-2026.md`
- **link_basename**: `akshay-pachaar-agent-memory-2026`
- **建议**: 创建页面 akshay-pachaar-agent-memory-2026.md 或修正链接

### 🔴 [高] #10
- **文件**: `concepts/ai-knowledge-layer-two-tier.md`
- **link_target**: `raw/articles/shannholmberg-ai-knowledge-layer-2026.md`
- **link_basename**: `shannholmberg-ai-knowledge-layer-2026`
- **建议**: 创建页面 shannholmberg-ai-knowledge-layer-2026.md 或修正链接

### 🔴 [高] #11
- **文件**: `concepts/ai-knowledge-layer-two-tier.md`
- **link_target**: `raw/articles/shannholmberg-ai-knowledge-layer-2026.md`
- **link_basename**: `shannholmberg-ai-knowledge-layer-2026`
- **建议**: 创建页面 shannholmberg-ai-knowledge-layer-2026.md 或修正链接

### 🔴 [高] #12
- **文件**: `concepts/ai-knowledge-layer-two-tier.md`
- **link_target**: `raw/articles/shannholmberg-ai-knowledge-layer-2026.md`
- **link_basename**: `shannholmberg-ai-knowledge-layer-2026`
- **建议**: 创建页面 shannholmberg-ai-knowledge-layer-2026.md 或修正链接

### 🔴 [高] #13
- **文件**: `concepts/bjork-disuse-theory.md`
- **link_target**: `raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md`
- **link_basename**: `ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14`
- **建议**: 创建页面 ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md 或修正链接

### 🔴 [高] #14
- **文件**: `concepts/filesystem-as-knowledge-graph.md`
- **link_target**: `raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md`
- **link_basename**: `ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14`
- **建议**: 创建页面 ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md 或修正链接

### 🔴 [高] #15
- **文件**: `concepts/hermes-android-deployment.md`
- **link_target**: `hermes-security-setup`
- **link_basename**: `hermes-security-setup`
- **建议**: 创建页面 hermes-security-setup.md 或修正链接

### 🔴 [高] #16
- **文件**: `concepts/hermes-android-deployment.md`
- **link_target**: `termux-api-reference`
- **link_basename**: `termux-api-reference`
- **建议**: 创建页面 termux-api-reference.md 或修正链接

### 🔴 [高] #17
- **文件**: `concepts/hermes-best-practices.md`
- **link_target**: `ksimback-hermes-beginners-guide-2026-04`
- **link_basename**: `ksimback-hermes-beginners-guide-2026-04`
- **建议**: 创建页面 ksimback-hermes-beginners-guide-2026-04.md 或修正链接

### 🔴 [高] #18
- **文件**: `concepts/hermes-best-practices.md`
- **link_target**: `startup-ideas-pod-hermes-imran-2026-04`
- **link_basename**: `startup-ideas-pod-hermes-imran-2026-04`
- **建议**: 创建页面 startup-ideas-pod-hermes-imran-2026-04.md 或修正链接

### 🔴 [高] #19
- **文件**: `concepts/hermes-system-prompt-structure.md`
- **link_target**: `raw/articles/lufzzliz-hermes-system-prompt-analysis-2026.md`
- **link_basename**: `lufzzliz-hermes-system-prompt-analysis-2026`
- **建议**: 创建页面 lufzzliz-hermes-system-prompt-analysis-2026.md 或修正链接

### 🔴 [高] #20
- **文件**: `concepts/hermes-system-prompt-structure.md`
- **link_target**: `raw/articles/lufzzliz-hermes-system-prompt-analysis-2026.md`
- **link_basename**: `lufzzliz-hermes-system-prompt-analysis-2026`
- **建议**: 创建页面 lufzzliz-hermes-system-prompt-analysis-2026.md 或修正链接

### 🔴 [高] #21
- **文件**: `concepts/hermes-token-optimization.md`
- **link_target**: `openrouter-model-pricing`
- **link_basename**: `openrouter-model-pricing`
- **建议**: 创建页面 openrouter-model-pricing.md 或修正链接

### 🔴 [高] #22
- **文件**: `concepts/knowledge-base-vs-memory.md`
- **link_target**: `raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md`
- **link_basename**: `ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14`
- **建议**: 创建页面 ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md 或修正链接

### 🔴 [高] #23
- **文件**: `concepts/memory-utility-function.md`
- **link_target**: `raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md`
- **link_basename**: `ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14`
- **建议**: 创建页面 ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md 或修正链接

### 🔴 [高] #24
- **文件**: `concepts/second-brain-karpathy-style.md`
- **link_target**: `raw/articles/second-brain-part2-system.md`
- **link_basename**: `second-brain-part2-system`
- **建议**: 创建页面 second-brain-part2-system.md 或修正链接

### 🔴 [高] #25
- **文件**: `concepts/smf-semantic-memory-framework.md`
- **link_target**: `raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md`
- **link_basename**: `ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14`
- **建议**: 创建页面 ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md 或修正链接

### 🔴 [高] #26
- **文件**: `entities/imran-hermes-power-user.md`
- **link_target**: `startup-ideas-pod-hermes-imran-2026-04`
- **link_basename**: `startup-ideas-pod-hermes-imran-2026-04`
- **建议**: 创建页面 startup-ideas-pod-hermes-imran-2026-04.md 或修正链接

### 🔴 [高] #27
- **文件**: `queries/kilroy-cdn-migration-plan.md`
- **link_target**: ` `
- **link_basename**: ` `
- **建议**: 创建页面  .md 或修正链接

### 🔴 [高] #28
- **文件**: `queries/kilroy-cdn-migration-plan.md`
- **link_target**: ` `
- **link_basename**: ` `
- **建议**: 创建页面  .md 或修正链接

## ✅ 缺少 frontmatter

无问题。

## ❌ 超过 200 行的页面 (21 个问题)

### 🟡 [中] #1
- **文件**: `concepts/12-agentic-harness-patterns.md`
- **line_count**: `338`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #2
- **文件**: `concepts/agent-memory-architecture.md`
- **line_count**: `330`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #3
- **文件**: `concepts/agentmemory-persistent-memory.md`
- **line_count**: `248`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #4
- **文件**: `concepts/ai-engineering-from-scratch.md`
- **line_count**: `223`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #5
- **文件**: `concepts/ai-knowledge-layer-two-tier.md`
- **line_count**: `396`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #6
- **文件**: `concepts/awesome-openclaw-tips.md`
- **line_count**: `474`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #7
- **文件**: `concepts/claude-alternatives-guide.md`
- **line_count**: `307`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #8
- **文件**: `concepts/claude-md-three-blocks-learning-system.md`
- **line_count**: `348`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #9
- **文件**: `concepts/cli-design-for-agents-and-humans.md`
- **line_count**: `356`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #10
- **文件**: `concepts/dario-amodei-ai-career-predictions.md`
- **line_count**: `412`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #11
- **文件**: `concepts/hermes-best-practices.md`
- **line_count**: `224`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #12
- **文件**: `concepts/how-to-make-money-with-claude-code.md`
- **line_count**: `333`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #13
- **文件**: `concepts/llm-council-method-karpathy.md`
- **line_count**: `294`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #14
- **文件**: `concepts/llm-knowledge-base-complete-guide.md`
- **line_count**: `402`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #15
- **文件**: `concepts/llm-wiki-karpathy.md`
- **line_count**: `267`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #16
- **文件**: `concepts/most-capable-agent-system-prompt.md`
- **line_count**: `402`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #17
- **文件**: `concepts/notebooklm-content-factory-workflow.md`
- **line_count**: `254`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #18
- **文件**: `concepts/openclaw-complete-guide.md`
- **line_count**: `306`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #19
- **文件**: `concepts/second-brain-karpathy-style.md`
- **line_count**: `301`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #20
- **文件**: `concepts/visual-explainer.md`
- **line_count**: `242`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

### 🟡 [中] #21
- **文件**: `queries/wiki-health-check-improvements.md`
- **line_count**: `212`
- **建议**: 页面超过 200 行，建议拆分为子主题并添加交叉链接

## ❌ 少于 2 个出站 wikilinks 的页面 (4 个问题)

### 🟡 [中] #1
- **文件**: `concepts/ai-influence-weekly-digest.md`
- **link_count**: `0`
- **建议**: 每页至少需要 2 个出站 wikilinks，请添加相关页面链接

### 🟡 [中] #2
- **文件**: `concepts/ai-influence-weekly-report-18-2026-04-27.md`
- **link_count**: `1`
- **建议**: 每页至少需要 2 个出站 wikilinks，请添加相关页面链接

### 🟡 [中] #3
- **文件**: `entities/ai-influence-accounts-65.md`
- **link_count**: `1`
- **建议**: 每页至少需要 2 个出站 wikilinks，请添加相关页面链接

### 🟡 [中] #4
- **文件**: `queries/kilroy-cdn-batch-migration-complete.md`
- **link_count**: `1`
- **建议**: 每页至少需要 2 个出站 wikilinks，请添加相关页面链接

## ✅ 标签不在 SCHEMA 分类法中

无问题。

## ❌ 未审查页面（reviewed: false） (40 个问题)

### 🟢 [低] #1
- **文件**: `concepts/12-agentic-harness-patterns.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #2
- **文件**: `concepts/agent-browser-sessions.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #3
- **文件**: `concepts/agent-harness.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #4
- **文件**: `concepts/agent-memory-architecture.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #5
- **文件**: `concepts/agentmemory-persistent-memory.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #6
- **文件**: `concepts/ai-engineering-from-scratch.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #7
- **文件**: `concepts/ai-ide-productivity-funnel.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #8
- **文件**: `concepts/ai-influence-weekly-digest.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #9
- **文件**: `concepts/ai-knowledge-layer-two-tier.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #10
- **文件**: `concepts/awesome-openclaw-tips.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #11
- **文件**: `concepts/bjork-disuse-theory.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #12
- **文件**: `concepts/claude-alternatives-guide.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #13
- **文件**: `concepts/claude-code-best-practices.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #14
- **文件**: `concepts/claude-md-three-blocks-learning-system.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #15
- **文件**: `concepts/cli-design-for-agents-and-humans.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #16
- **文件**: `concepts/dario-amodei-ai-career-predictions.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #17
- **文件**: `concepts/filesystem-as-knowledge-graph.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #18
- **文件**: `concepts/hermes-android-deployment.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #19
- **文件**: `concepts/hermes-best-practices.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #20
- **文件**: `concepts/hermes-system-prompt-structure.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #21
- **文件**: `concepts/hermes-token-optimization.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #22
- **文件**: `concepts/how-to-make-money-with-claude-code.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #23
- **文件**: `concepts/knowledge-base-vs-memory.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #24
- **文件**: `concepts/llm-council-method-karpathy.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #25
- **文件**: `concepts/llm-knowledge-base-complete-guide.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #26
- **文件**: `concepts/llm-wiki-karpathy.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #27
- **文件**: `concepts/memory-utility-function.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #28
- **文件**: `concepts/most-capable-agent-system-prompt.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #29
- **文件**: `concepts/notebooklm-content-factory-workflow.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #30
- **文件**: `concepts/openclaw-complete-guide.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #31
- **文件**: `concepts/second-brain-karpathy-style.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #32
- **文件**: `concepts/self-improving-agent-system-prompt.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #33
- **文件**: `concepts/smf-semantic-memory-framework.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #34
- **文件**: `concepts/visual-explainer.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #35
- **文件**: `entities/ai-influence-accounts-65.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #36
- **文件**: `entities/imran-hermes-power-user.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #37
- **文件**: `entities/karpathy-ai-engineering.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #38
- **文件**: `queries/ai-evening-brief-2026-04-18.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #39
- **文件**: `queries/kilroy-cdn-batch-migration-complete.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

### 🟢 [低] #40
- **文件**: `queries/kilroy-cdn-migration-plan.md`
- **建议**: 页面标记为 reviewed: false，建议人工审查后更新为 true

## 📋 index.md 同步检查

✅ 所有页面均在 index.md 中有引用。

## 🔧 自动修复

✅ index.md 同步正常，无需修复。


**操作**: 自动 lint 扫描，无手动修复执行（index.md 已同步）
**下次检查**: 待用户触发或下次 cron

## [2026-04-28] ingest | AI影响力周报第 18 期
- 来源：~/.hermes/output/ai-influence-digest/weekly_report_2026-04-28.md
- 保存到：raw/articles/ai-influence-weekly-18-2026-04-28.md
- 扫描账号：65 个 AI 领域影响力账号
- 候选推文：约 80+ 条（Google 搜索 + 公开抓取）
- 精选数量：8 条
- 核心话题：AI 平民化、Agent 工作流设计、企业 AI 预算、开源 AI 崛起
- 更新：index.md, log.md


---

# Wiki Health Check Report
**Date**: 2026-04-29
**Total pages scanned**: 43
**Directories**: concepts, entities, comparisons, queries
**SCHEMA tags**: 65
**Total issues**: 84

## 1. 孤立页面（无入链） — 严重程度: 高
发现 **13** 个页面

- ❌ `concepts/agent-browser-sessions.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/ai-ide-productivity-funnel.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/awesome-openclaw-tips.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/dario-amodei-ai-career-predictions.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/llm-council-method-karpathy.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/memory-utility-function.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/refrag-rag-decoding.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/self-improving-agent-system-prompt.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `concepts/visual-explainer.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `entities/ai-influence-accounts-65.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `entities/karpathy-ai-engineering.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `queries/ai-evening-brief-2026-04-18.md` — 建议：在 index.md 或其他相关页面添加入链
- ❌ `queries/kilroy-cdn-batch-migration-complete.md` — 建议：在 index.md 或其他相关页面添加入链

## 2. 损坏的 wikilinks — 严重程度: 高
发现 **4** 个真正损坏的链接 + **2** 个空链接

- ❌ `concepts/agent-browser-sessions.md` → `[[hermes-browser-automation]]` — 目标不存在
- ❌ `concepts/hermes-android-deployment.md` → `[[hermes-security-setup]]` — 目标不存在
- ❌ `concepts/hermes-android-deployment.md` → `[[termux-api-reference]]` — 目标不存在
- ❌ `concepts/hermes-token-optimization.md` → `[[openrouter-model-pricing]]` — 目标不存在
- ⚠️  `queries/kilroy-cdn-migration-plan.md` → `[[]]` — 空链接（需检查是否为代码示例）
- ⚠️  `queries/kilroy-cdn-migration-plan.md` → `[[]]` — 空链接（需检查是否为代码示例）

## 3. 缺少 frontmatter — 严重程度: 低

- ✅ 所有页面都有 frontmatter

## 4. 超过 200 行的页面 — 严重程度: 高
发现 **21** 个页面

- ⚠️  `concepts/12-agentic-harness-patterns.md` (338 行)
- ⚠️  `concepts/agent-memory-architecture.md` (330 行)
- ⚠️  `concepts/agentmemory-persistent-memory.md` (248 行)
- ⚠️  `concepts/ai-engineering-from-scratch.md` (223 行)
- ⚠️  `concepts/ai-knowledge-layer-two-tier.md` (396 行)
- ⚠️  `concepts/awesome-openclaw-tips.md` (474 行)
- ⚠️  `concepts/claude-alternatives-guide.md` (307 行)
- ⚠️  `concepts/claude-md-three-blocks-learning-system.md` (348 行)
- ⚠️  `concepts/cli-design-for-agents-and-humans.md` (356 行)
- ⚠️  `concepts/dario-amodei-ai-career-predictions.md` (412 行)
- ⚠️  `concepts/hermes-best-practices.md` (224 行)
- ⚠️  `concepts/how-to-make-money-with-claude-code.md` (333 行)
- ⚠️  `concepts/llm-council-method-karpathy.md` (294 行)
- ⚠️  `concepts/llm-knowledge-base-complete-guide.md` (402 行)
- ⚠️  `concepts/llm-wiki-karpathy.md` (267 行)
- ⚠️  `concepts/most-capable-agent-system-prompt.md` (402 行)
- ⚠️  `concepts/notebooklm-content-factory-workflow.md` (254 行)
- ⚠️  `concepts/openclaw-complete-guide.md` (306 行)
- ⚠️  `concepts/second-brain-karpathy-style.md` (301 行)
- ⚠️  `concepts/visual-explainer.md` (242 行)
- ⚠️  `queries/wiki-health-check-improvements.md` (212 行)

## 5. 少于 2 个 wikilinks 的页面 — 严重程度: 高
发现 **4** 个页面

- ⚠️  `concepts/ai-influence-weekly-digest.md` (0 个链接: (无))
- ⚠️  `concepts/ai-influence-weekly-report-18-2026-04-27.md` (1 个链接: ai-influence-weekly-report-18-2026-04-27)
- ⚠️  `entities/ai-influence-accounts-65.md` (1 个链接: ai-influence-weekly-digest)
- ⚠️  `queries/kilroy-cdn-batch-migration-complete.md` (1 个链接: kilroy-cdn-migration-plan)

## 6. 标签不在 SCHEMA 分类法中 — 严重程度: 低

- ✅ 所有标签都在 SCHEMA 分类法中

## 7. 未审查页面（reviewed: false） — 严重程度: 高
发现 **40** 个未审查页面

- ⚠️  `concepts/12-agentic-harness-patterns.md`
- ⚠️  `concepts/agent-browser-sessions.md`
- ⚠️  `concepts/agent-harness.md`
- ⚠️  `concepts/agent-memory-architecture.md`
- ⚠️  `concepts/agentmemory-persistent-memory.md`
- ⚠️  `concepts/ai-engineering-from-scratch.md`
- ⚠️  `concepts/ai-ide-productivity-funnel.md`
- ⚠️  `concepts/ai-influence-weekly-digest.md`
- ⚠️  `concepts/ai-knowledge-layer-two-tier.md`
- ⚠️  `concepts/awesome-openclaw-tips.md`
- ⚠️  `concepts/bjork-disuse-theory.md`
- ⚠️  `concepts/claude-alternatives-guide.md`
- ⚠️  `concepts/claude-code-best-practices.md`
- ⚠️  `concepts/claude-md-three-blocks-learning-system.md`
- ⚠️  `concepts/cli-design-for-agents-and-humans.md`
- ⚠️  `concepts/dario-amodei-ai-career-predictions.md`
- ⚠️  `concepts/filesystem-as-knowledge-graph.md`
- ⚠️  `concepts/hermes-android-deployment.md`
- ⚠️  `concepts/hermes-best-practices.md`
- ⚠️  `concepts/hermes-system-prompt-structure.md`
- ⚠️  `concepts/hermes-token-optimization.md`
- ⚠️  `concepts/how-to-make-money-with-claude-code.md`
- ⚠️  `concepts/knowledge-base-vs-memory.md`
- ⚠️  `concepts/llm-council-method-karpathy.md`
- ⚠️  `concepts/llm-knowledge-base-complete-guide.md`
- ⚠️  `concepts/llm-wiki-karpathy.md`
- ⚠️  `concepts/memory-utility-function.md`
- ⚠️  `concepts/most-capable-agent-system-prompt.md`
- ⚠️  `concepts/notebooklm-content-factory-workflow.md`
- ⚠️  `concepts/openclaw-complete-guide.md`
- ⚠️  `concepts/second-brain-karpathy-style.md`
- ⚠️  `concepts/self-improving-agent-system-prompt.md`
- ⚠️  `concepts/smf-semantic-memory-framework.md`
- ⚠️  `concepts/visual-explainer.md`
- ⚠️  `entities/ai-influence-accounts-65.md`
- ⚠️  `entities/imran-hermes-power-user.md`
- ⚠️  `entities/karpathy-ai-engineering.md`
- ⚠️  `queries/ai-evening-brief-2026-04-18.md`
- ⚠️  `queries/kilroy-cdn-batch-migration-complete.md`
- ⚠️  `queries/kilroy-cdn-migration-plan.md`

## 总结

| 类别 | 数量 | 严重程度 |
|------|------|----------|
| 孤立页面 | 13 | 高 |
| 损坏链接 | 6 | 高 |
| 缺少 frontmatter | 0 | 低 |
| 页面过长 | 21 | 高 |
| 链接不足 | 4 | 高 |
| 无效标签 | 0 | 低 |
| 未审查 | 40 | 高 |

**总计**: 84 个问题
## 2026-04-29: Wiki Health Check — Auto-Fixes Applied

### Auto-Fixes
1. **Fixed 4 inconsistent raw/article wikilinks** (bare name → full path):
   - `concepts/hermes-best-practices.md`: `[[ksimback-hermes-beginners-guide-2026-04]]` → `[[raw/articles/ksimback-hermes-beginners-guide-2026-04]]`
   - `concepts/hermes-best-practices.md`: `[[startup-ideas-pod-hermes-imran-2026-04]]` → `[[raw/articles/startup-ideas-pod-hermes-imran-2026-04]]`
   - `entities/imran-hermes-power-user.md`: `[[startup-ideas-pod-hermes-imran-2026-04]]` → `[[raw/articles/startup-ideas-pod-hermes-imran-2026-04]]`
   - `concepts/agent-browser-sessions.md`: `[[nottelabs-session-profiles-2026-02]]` → `[[raw/articles/nottelabs-session-profiles-2026-02]]`

2. **Fixed 14 raw/article wikilinks** (removed `.md` extension):
   - `hermes-system-prompt-structure.md`, `filesystem-as-knowledge-graph.md`, `memory-utility-function.md`, `smf-semantic-memory-framework.md`, `knowledge-base-vs-memory.md`, `bjork-disuse-theory.md`, `agent-harness.md`, `second-brain-karpathy-style.md`, `agent-memory-architecture.md`, `ai-knowledge-layer-two-tier.md`

3. **Fixed index.md**:
   - Corrected `ai-influence-weekly-report-017-2026-04-24` → `ai-influence-weekly-report-17-2026-04-24`
   - Updated last updated date to 2026-04-29
   - Updated total pages count to 43

### Remaining Issues (Manual Action Required)
- **4 truly broken links** (targets don't exist anywhere):
  - `hermes-browser-automation`
  - `hermes-security-setup`
  - `termux-api-reference`
  - `openrouter-model-pricing`
- **2 empty wikilinks** in `kilroy-cdn-migration-plan.md` (inline code examples, not actual links)
- **13 isolated pages** (no inbound links from other wiki pages)
- **21 pages over 200 lines** (recommend splitting)
- **4 pages with fewer than 2 wikilinks**
- **40 unreviewed pages** (reviewed: false)

### Stats After Fixes
| 类别 | 修复前 | 修复后 |
|------|--------|--------|
| 孤立页面 | 13 | 13 |
| 损坏链接 | 28 | 6 |
| 缺少 frontmatter | 0 | 0 |
| 页面过长 | 21 | 21 |
| 链接不足 | 4 | 4 |
| 无效标签 | 0 | 0 |
| 未审查 | 40 | 40 |
| **总计** | **106** | **84** |
