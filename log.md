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
