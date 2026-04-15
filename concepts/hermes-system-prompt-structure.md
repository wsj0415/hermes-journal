---
title: Hermes Agent 系统提示词结构与优化
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [architecture, best-practice, model-config]
sources: [raw/articles/lufzzliz-hermes-system-prompt-analysis-2026.md]
reviewed: false
reviewed_at:
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

Hermes Agent 系统提示词约 36,700 字符（~10K tokens），由 9 层结构组成。通过优化 AGENTS.md 加载策略可减少 50% token（约 5K tokens/对话）。

### 9 层结构

| 层级 | 名称 | 大小 | 说明 |
|------|------|------|------|
| 1 | SOUL.md | ~500 chars | Agent 身份定义（用户自定义） |
| 2 | Memory 使用指南 | ~600 chars | 硬编码，告诉模型如何使用 memory 工具 |
| 3 | MEMORY 快照 | ~3,725/4,000 chars | 冻结快照，包含用户偏好、环境事实等 |
| 4 | USER PROFILE 快照 | ~682/1,375 chars | 用户是谁、配置偏好、GitHub 排版偏好 |
| 5 | Skills 索引 | ~5,000 chars | ~80+ 个 Skill 分类列表（截断展示） |
| 6 | AGENTS.md | ~20,300 chars（截断到 14K+4K） | **最大头**，项目开发指南 |
| 7 | 会话元数据 | ~200 chars | 模型自我认知指令 |
| 8 | 平台提示 | ~200 chars | Telegram/Discord 等平台定制提示 |
| 9 | 会话上下文元信息 | ~400 chars | 当前会话位置、类型、Home Channel |

### AGENTS.md 截断机制

```
AGENTS.md 原文（20,360 chars）
├── 前 14,000 chars → 保留（项目结构、核心 API）
├── 中间 2,360 chars → 丢弃
└── 后 4,000 chars → 保留（Known Pitfalls、测试指南）
```

**单文件上限**：20,000 chars
**截断比例**：头部 70%（14K），尾部 30%（4-6K）

### 优化方案：减少 50% token

**问题**：默认启动会加载 `~/.hermes/hermes-agent/AGENTS.md`（5K tokens），对非开发者不必要。

**解决方案**：
1. 配置主 Agent 的 TERMINAL CWD 路径到自己的工作目录
2. 创建自定义 AGENTS.md（只保留需要的内容）
3. 重启会话，让 Hermes 加载新的 AGENTS.md

**效果**：
- 优化前：~10K tokens/对话
- 优化后：~5K tokens/对话
- 节省：50%

### 工具加载机制

Hermes 注册 51 个工具，会话按需加载约 30 个。

**筛选机制**：`model_tools.py` 的 `_discover_tools()`：
- `check_fn`：检查 API Key 是否存在
- `enabled_toolsets` / `disabled_toolsets`：控制加载

---

## 时间线

- 2026-04-15: 初始创建，来源 [[lufzzliz-hermes-system-prompt-analysis-2026]]

---

## 实践建议

### 优化 AGENTS.md 加载

```bash
# 1. 配置 TERMINAL CWD 到你的工作目录
# 编辑 ~/.hermes/config.yaml
terminal:
  cwd: /root/your-project  # 改为你的项目目录

# 2. 在项目目录创建精简版 AGENTS.md
# 只保留你需要的内容

# 3. 重启 Hermes
pkill -f "gateway run"
# 重新启动网关
```

### 监控 MEMORY 使用

当前 MEMORY 快照上限 4,000 chars，使用率 93%（~3,725 chars）。

**建议**：
- 定期审查 `~/.hermes/memories/MEMORY.md`
- 移除过期信息
- 避免保存临时任务进度（用 session_search 回忆）

### Skill 管理

Skills 索引占 5,000 chars（~80+ 个 Skill）。

**问题**：Skill 可能泛滥，增加提示词长度。

**建议**：
- 定期审查 `~/.hermes/skills/`
- 删除不再使用的 Skill
- 合并功能重复的 Skill

---

## 相关链接

- [[lufzzliz-hermes-system-prompt-analysis-2026]] - 原始来源
- [微信公众号版本](https://mp.weixin.qq.com/s/gM6mJsH0ay4Z7jkEBjGE0w)
