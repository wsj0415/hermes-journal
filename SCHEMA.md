# Wiki Schema

## Domain
Hermes Agent 使用日记 — 记录 Hermes Agent 框架的使用经验、配置方案、Skills 开发、故障排查和最佳实践。

## Conventions
- 文件名：小写，连字符，无空格（如 `telegram-channel-config.md`）
- 每个 wiki 页面以 YAML frontmatter 开头（见下方）
- 使用 `[[wikilinks]]` 链接到其他页面（每页至少 2 个出站链接）
- 更新页面时，必须 bump `updated` 日期
- 新页面必须添加到 `index.md` 的正确分类下
- 每个操作必须追加到 `log.md`

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | config | troubleshooting
tags: [来自下方分类法]
sources: [raw/articles/来源名称.md]
# 质量控制（新增）
reviewed: false          # AI 生成时为 false，人类审查后改为 true
reviewed_at:             # 人类审查时填写日期
confidence: medium       # high | medium | low | uncertain
confidence_reason:       # 填写置信度依据
---
```

## Tag Taxonomy
- 平台：telegram, whatsapp, discord, sms, web
- 功能：skills, cron, memory, browser, terminal, delegation, mcp
- 任务类型：config, troubleshooting, best-practice, workflow, api-reference
- 模型：model-config, provider, quantization, inference
- 开发：skill-development, debugging, testing, deployment
- 架构：architecture, agent-architecture, knowledge-base, vector-search, graph
- 内容：brand-foundation
- 人物/来源：karpathy, amodei
- 主题：monetization, career, ai-trends, education, curriculum, decision-making
- 工具/框架：openclaw, notebooklm, youtube
- 设计：agent-design, system-prompt, cli, ux, visualization, html, agent-setup
- 元数据：tips, content-creation, company, person

规则：页面上的每个标签必须出现在此分类法中。需要新标签时，先添加到这里再使用。

## Page Thresholds
- **创建页面**：当某个实体/概念在 2+ 个来源中出现，或是一个来源的核心内容
- **添加到现有页面**：当来源提到已覆盖的内容
- **不创建页面**：对于短暂提及、次要细节或领域外的内容
- **拆分页面**：超过 200 行时 — 拆分为子主题并添加交叉链接
- **归档页面**：内容完全被取代时 — 移至 `_archive/`，从索引中移除

## 页面格式：Compiled Truth + Timeline

每个 wiki 页面遵循以下结构（借鉴 GBrain 模式）：

```markdown
---
title: 页面标题
type: concept  # entity | concept | comparison | query
---

## 编译知识

[当前最佳理解，可随新证据更新]

[核心定义、解释、综合结论]

---

## 时间线

[只追加，不编辑。记录知识演变过程]

- YYYY-MM-DD: 初始创建，来源 [[source]]
- YYYY-MM-DD: 更新 X 信息，来源 [[source2]]
- YYYY-MM-DD: 修正 Y 错误，来源 [[source3]]
```

**规则**：
- `## 编译知识` 可以随新证据重写
- `## 时间线` 只追加，永不编辑
- 分隔线 `---` 必须存在
- 每次更新页面时，在时间线追加一条记录

**为什么**：
- 编译知识 = 当前答案（方便快速查阅）
- 时间线 = 证据链（方便追溯来源和变更）
- 分离后，既能快速获得综合结论，又能追溯知识演变

## Update Policy
当新信息与现有内容冲突时：
1. 检查日期 — 较新的来源通常取代较旧的
2. 如果确实矛盾，记录两种观点并附带日期和来源
3. 在 frontmatter 中标记矛盾：`contradictions: [页面名称]`
4. 在 lint 报告中标记供用户审查
