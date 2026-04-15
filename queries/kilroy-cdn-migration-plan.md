---
title: kilroy-cdn 迁移计划
created: 2026-04-15
updated: 2026-04-15
type: summary
tags: [workflow, best-practice]
sources: []
reviewed: false
---

## 编译知识

kilroy-cdn 是之前的内容创作知识库，包含内容创作技能、写作素材库、心跳任务配置、以及大量 AI/Agent 相关 summaries。需要系统性迁移到 hermes-journal。

**核心资产**：
- Content Creator 技能（4 种文案风格 + 5 平台适配）
- 写作素材库（钩子库、金句库、案例库、数据库、禁词库）
- HEARTBEAT 任务配置
- 14 个日期的 summaries（AI/Agent 主题）
- 内容同步脚本和流程文档

---

## 时间线

- 2026-04-15: 发现 kilroy-cdn，创建迁移计划

---

## 迁移优先级

### P0 - 立即迁移（核心资产）

| 文件 | 目标位置 | 说明 |
|------|----------|------|
| `content-creator/SKILL.md` | `skills/content-creator.md` | 内容创作技能，461 行完整流程 |
| `writing-materials/05-禁词库.md` | `brand-foundation/banned-words.md` | **合并到现有禁用词** |
| `writing-materials/01-钩子库.md` | `references/hooks-collection.md` | 8 种爆款开头方式 |
| `HEARTBEAT.md` | `references/heartbeat-template.md` | 心跳任务模板 |

### P1 - 本周迁移（高价值）

| 文件 | 目标位置 | 说明 |
|------|----------|------|
| `writing-materials/02-金句库.md` | `references/quotes-collection.md` | 22 条金句 |
| `writing-materials/03-案例库.md` | `references/case-studies.md` | 3 个实战故事 |
| `writing-materials/04-数据库.md` | `references/industry-data.md` | 15 条行业数据 |
| `CONTENT-SYNC.md` | `references/content-sync-workflow.md` | 内容同步流程 |
| `summaries/2026-04-07/*.md` | `raw/articles/` | 最新 6 篇 AI/Agent 文章 |

### P2 - 可选迁移（按需）

| 文件 | 说明 |
|------|------|
| `summaries/2026-03-*/` | 早期 summaries，按需检索 |
| `week-plan/` | 过期的内容计划 |
| `content_output/` | 已发布的内容输出 |
| `reports/` | 行业报告简报 |

---

## 迁移发现

### ✅ 可复用的内容

1. **禁词库**（10 条）
   - 当前 hermes-journal 的 `banned-words.md` 有基础列表
   - kilroy-cdn 版本更详细（带示例对比）
   - **行动**：合并增强

2. **钩子库**（8 条）
   - 对话式、反差对比、数字承诺、内幕揭秘等
   - **行动**：创建新页面

3. **Content Creator 技能**
   - 完整的交互式创作流程
   - 4 种文案风格模板
   - 5 平台适配规则
   - 3 种封面图风格
   - **行动**：创建 skill

4. **Summaries**（最新 6 篇）
   - agent-skills-addyosmani.md
   - ai-agent-team-software-development.md
   - ai-secretary-muninn-system.md
   - llm-knowledge-base-complete-guide.md
   - second-brain-karpathy-style.md
   - second-brain-part2-system.md
   - **行动**：批量 ingest

### ⚠️ 需要注意

1. **内容重复**
   - kilroy-cdn 的 summaries 有些可能已存在于 hermes-journal
   - **解决**：迁移前用 search_files 检查

2. **格式差异**
   - kilroy-cdn 用 Obsidian wikilinks `[[ ]]`
   - hermes-journal 也用 `[[ ]]`（兼容）
   - kilroy-cdn 有些 HTML 标签（`<br>`）
   - **解决**：迁移时清理

3. **状态追踪**
   - kilroy-cdn 有进度追踪表格（钩子库 1/100 等）
   - **解决**：保留作为历史记录

---

## 执行步骤

### Step 1: 合并禁词库
```bash
# 读取 kilroy-cdn 禁词库
read_file /root/.openclaw/workspace/kilroy-cdn/writing-materials/05-禁词库.md

# 合并到 hermes-journal/brand-foundation/banned-words.md
# 保留现有内容，添加 kilroy-cdn 的 10 条详细示例
```

### Step 2: 创建钩子库
```bash
# 复制到 references/hooks-collection.md
# 更新 frontmatter
# 添加到 index.md
```

### Step 3: 迁移 Summaries
```bash
# 对每篇 summary：
# 1. 读取内容
# 2. 检查是否已存在（search_files）
# 3. 创建为 raw/articles/*.md
# 4. 如值得编译，创建 concepts/*.md
```

### Step 4: 更新索引
- 更新 index.md
- 更新 log.md
- Git 提交推送

---

## 预计工作量

| 任务 | 预计时间 |
|------|----------|
| 合并禁词库 | 15 分钟 |
| 创建钩子库 | 10 分钟 |
| 迁移 6 篇 summaries | 30 分钟 |
| 更新索引和日志 | 10 分钟 |
| **总计** | **约 1 小时** |

---

## 相关链接

- [[wiki-health-check-improvements]] - Wiki 改进方案
- [[ai-knowledge-layer-two-tier]] - Knowledge Layer 架构
