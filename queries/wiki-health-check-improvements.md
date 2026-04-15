---
title: Wiki 健康检查与改进方案
created: 2026-04-15
updated: 2026-04-15
type: query
tags: [best-practice, debugging]
sources: []
---

# Wiki 健康检查与改进方案

> **一句话总结**：对比两篇 AI 知识库管理文章，发现当前 wiki 的 6 个问题，并提出 8 项改进建议，让 AI 更好地管理知识库。

---

## 健康检查结果

### ✅ 符合规范

- Frontmatter 完整：所有页面都有必需的 YAML frontmatter
- log.md 记录完整：所有操作都有 chronological 记录
- index.md 同步：所有 wiki 页面都在索引中
- Git 同步正常：GitHub 仓库已配置并推送

### ⚠️ 需要修复

| 问题 | 严重性 | 涉及页面 |
|------|--------|----------|
| **超过 200 行** | 中 | `agent-memory-architecture.md` (304 行), `ai-knowledge-layer-two-tier.md` (365 行) |
| **标签不在 SCHEMA 中** | 高 | 两个页面共 9 个标签未定义 |
| **损坏的 wikilinks** | 中 | 指向 raw 来源的链接（应改为外部链接） |
| **孤立页面** | 低 | `ai-knowledge-layer-two-tier.md` 无入链（正常，新页面） |

---

## SCHEMA.md 标签分类法更新建议

当前 SCHEMA.md 的标签分类法缺失以下标签，需要添加：

```markdown
## Tag Taxonomy

- 平台：telegram, whatsapp, discord, sms, web
- 功能：skills, cron, memory, browser, terminal, delegation, mcp
- 任务类型：config, troubleshooting, best-practice, workflow, api-reference
- 模型：model-config, provider, quantization, inference
- 开发：skill-development, debugging, testing, deployment
- ← 新增 →
- 架构：architecture, agent-architecture, knowledge-base, vector-search, graph
- 内容：brand-foundation, memory
```

---

## 两篇文章核心洞察对比

| 维度 | Agent Memory 架构 (Akshay) | AI Knowledge Layer (Shann) | 借鉴点 |
|------|---------------------------|---------------------------|--------|
| **核心问题** | LLM 无状态，需要持久化记忆 | Agent 不认识你，输出通用 | 两者互补：记忆 + 品味 |
| **架构** | 三存储（关系 + 向量 + 图） | 两层（KBL 动态 + BF 静态） | **BF 层是当前 wiki 缺失的** |
| **检索** | Cognee 四调用 API | 编译式 vs RAG（71.5x token 节省） | 编译式已采用，正确 |
| **质量控制** | 去重、增量处理 | Validation Gate + Bias Checks + Confidence Levels | **三项都可借鉴** |
| **工作流** | ingest → extract → store → retrieve → respond | 白天 clip → 夜间 ingest → 醒来更丰富 | 已有 cron，需确认执行 |
| **人类角色** | 策展来源、指导分析 | 80/20 规则（AI 做 80%，人类品味 20%） | 明确分工 |

---

## 8 项改进建议

### 1. 添加 Brand Foundation 层 ⭐⭐⭐ ✅ 已完成

**创建文件**：
- `brand-foundation/banned-words.md` - AI 禁用词列表
- `brand-foundation/voice-profile.md` - 声音画像
- `brand-foundation/output-format.md` - 输出格式规范

**规则**：
- 只有人类编辑，Agent 永不修改
- 每个 Agent 任务前必须读取
- 更新时记录到 log.md

---

### 2. 实现 Validation Gate ⭐⭐⭐ ✅ 已完成

**SCHEMA.md 已更新**：
```yaml
reviewed: false          # AI 生成时为 false，人类审查后改为 true
reviewed_at:             # 人类审查时填写日期
confidence: medium       # high | medium | low | uncertain
confidence_reason:       # 填写置信度依据
```

**已更新页面**：
- `concepts/agent-memory-architecture.md` - 添加质量控制字段
- `concepts/ai-knowledge-layer-two-tier.md` - 添加质量控制字段

**工作流**：
1. AI 生成页面 → `reviewed: false`
2. 人类审查 → 改为 `reviewed: true` + 填写 `reviewed_at`
3. Lint 时报告未审查页面

---

### 3. 添加 Confidence Levels ⭐⭐ ✅ 已完成

已集成到 SCHEMA.md frontmatter 模板中。

---

### 4. 实现 Bias Checks ⭐⭐

**问题**：AI 可能只编译单一视角

**建议**：在概念页面模板中添加固定章节：
```markdown
## 反论点与数据缺口

<!-- AI 必须填写 -->
- **反论点**：[对立观点是什么]
- **数据缺口**：[缺少什么信息]
- **未解决问题**：[开放性问题]
```
### 5. 拆分超过 200 行的页面 ⭐

**当前问题**：
- `agent-memory-architecture.md` (304 行) → 拆分为：
  - `agent-memory-failure-modes.md` (失败模式)
  - `agent-memory-evolution.md` (架构演进)
  - `cognee-architecture.md` (Cognee 详解)
- `ai-knowledge-layer-two-tier.md` (365 行) → 拆分为：
  - `knowledge-base-layer.md` (KBL 详解)
  - `brand-foundation-layer.md` (BF 详解)
  - `knowledge-layer-setup.md` (搭建指南)

---

### 6. 添加 Obsidian Web Clipper 集成 ⭐⭐

**建议**：
1. 创建 `raw/clippings/` 文件夹
2. 安装 Obsidian Web Clipper 扩展
3. 浏览时一键 clip 到 `clippings/`
4. ingest 时自动处理 clippings

**好处**：降低输入摩擦，随时收集来源

---

### 7. 实现查询归档 ⭐

**当前缺失**：有价值的查询没有归档

**建议**：当查询满足以下条件时，创建 `queries/*.md`：
- 多页面综合答案
- 产生新洞察
- 可复用的分析

**示例**：
```
queries/agent-memory-vs-knowledge-layer.md
```

---

### 8. 增强 Lint 自动化 ⭐⭐⭐

**当前**：手动触发

**建议**：
1. 每周 cron 运行 lint（现有 cron 只同步 Git）
2. Lint 脚本检查：
   - 孤立页面
   - 损坏链接
   - 未审查页面
   - 过期标签
   - 超长大页面
3. 自动修复能修的，标记需要人类判断的

---

## 优先级排序

| 优先级 | 改进项 | 预计时间 | 影响力 |
|--------|--------|----------|--------|
| **P0** | 更新 SCHEMA 标签分类法 | 5 分钟 | 高（规范基础） |
| **P0** | 添加 Validation Gate | 10 分钟 | 高（质量控制） |
| **P1** | 创建 Brand Foundation 层 | 30 分钟 | 高（核心架构） |
| **P1** | 增强 Lint 自动化 | 30 分钟 | 中（持续维护） |
| **P2** | 拆分大页面 | 1 小时 | 中（可读性） |
| **P2** | 添加 Confidence Levels | 15 分钟 | 中（透明度） |
| **P3** | 实现 Bias Checks | 15 分钟 | 中（质量） |
| **P3** | Obsidian Web Clipper 集成 | 10 分钟 | 低（便利性） |
| **P3** | 查询归档 | 15 分钟 | 低（知识积累） |

---

## 下一步行动

1. **立即**：更新 SCHEMA.md 标签分类法
2. **本次会话**：创建 Brand Foundation 框架
3. **下次 ingest 前**：实现 Validation Gate + Confidence Levels
4. **本周内**：拆分大页面 + 设置 Lint cron

---

## 参考链接

- [[agent-memory-architecture]] - Agent Memory 架构演进
- [[ai-knowledge-layer-two-tier]] - AI Knowledge Layer 两层系统
- [llm-wiki skill](skill://llm-wiki) - LLM Wiki 技能文档
