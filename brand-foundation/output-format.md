---
title: 输出格式规范
created: 2026-04-15
updated: 2026-04-15
type: config
tags: [brand-foundation]
reviewed: true
reviewed_at: 2026-04-15
confidence: high
confidence_reason: Human-defined brand guidelines
---

# 输出格式规范

**规则**：Agent 生成内容时遵循此规范。

---

## 标准工作流

### 1. 一句话总结（英文来源必选）

如果来源是英文，开头必须有：

```markdown
> **一句话总结**：[20-40 字概括核心内容]
```

### 2. 正文结构

```markdown
## 核心问题
[问题是什么，为什么重要]

## 解决方案
[具体方案，分点说明]

## 实践建议
[如何落地，步骤清晰]

## 相关链接
- [[wikilink]] - 内部链接
- [文本](URL) - 外部链接
```

### 3. 表格优先

对比、矩阵、决策框架优先用表格：

```markdown
| 维度 | 选项 A | 选项 B | 推荐 |
|------|--------|--------|------|
| 速度 | 快 | 慢 | ✅ |
| 成本 | 高 | 低 | ✅ |
```

---

## 代码示例规范

### Shell 命令

```bash
# 带注释的命令
cd /root/hermes-journal && git add -A && git commit -m "描述"
```

### 配置文件

```yaml
# ~/.hermes/config.yaml
skills:
  config:
    wiki:
      path: ~/hermes-journal
```

### Python 代码

```python
# 有注释的代码
def process_data(data):
    # 第一步：清洗
    cleaned = clean(data)
    # 第二步：处理
    return process(cleaned)
```

---

## 链接规范

### 内部链接（wikilinks）

- 每页至少 2 个出站链接
- 使用 `[[页面名称]]` 格式
- 链接到已存在的页面

### 外部链接

- 来源 URL 必须放在 frontmatter 的 `sources` 字段
- 正文中引用外部资源用 `[描述](URL)`
- GitHub 仓库用完整 URL

---

## 长度控制

| 页面类型 | 行数限制 | 超限处理 |
|----------|----------|----------|
| concept | 200 行 | 拆分为子主题 |
| entity | 150 行 | 拆分或摘要 |
| query | 300 行 | 可保留（深度分析） |
| comparison | 250 行 | 可保留 |

---

## 审查状态标记

每个页面必须在 frontmatter 中标记：

```yaml
reviewed: false          # AI 生成默认 false
reviewed_at:             # 人类审查后填写
```

**只有人类能将 `reviewed` 改为 `true`**。

---

## 版本控制

- 所有更改通过 Git 提交
- 提交信息格式：`类型：描述`
  - `Ingest: 添加来源 X`
  - `Update: 更新页面 Y`
  - `Lint: 健康检查`
  - `Fix: 修复问题 Z`

---

**最后更新**：2026-04-15
**审查状态**：human-reviewed
