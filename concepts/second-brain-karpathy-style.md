---
title: Karpathy 风格第二大脑 - 个人知识库构建指南
created: 2026-04-15
updated: 2026-04-15
type: summary
tags: [knowledge-base, best-practice, workflow]
sources: [raw/articles/second-brain-karpathy-style.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

Karpathy 风格的第二大脑是一个极简个人知识库系统：将所有内容倾倒到一个文件夹，让 AI 组织成个人 wiki，每次使用时变得更聪明。无需特殊软件、无需数据库、仅需文件夹和文本文件。

**核心理念**：
```
不要将笔记分散在不同应用中
→ 将所有内容倾倒到一个文件夹
→ 告诉 AI 将其组织成个人 wiki
→ 每次使用时变得更聪明
```

**设置时间**：7 分钟内完成

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Nick Spisak (@NickSpisak_) 推文

---

## 8 步完整指南

### 步骤 1：创建三个文件夹（2 分钟）

```
your-knowledge-base/
├── raw/          # 原始源材料（杂物抽屉）
├── wiki/         # AI 组织的知识库
└── outputs/      # 问题答案存储
```

**说明**：
- **raw/** — 源材料杂物抽屉（文章、截图、笔记等）
- **wiki/** — AI 将混乱转为有序的地方
- **outputs/** — 你对问题的答案存储

**关键**：无需安装应用，无需创建账户，三个文件夹。

---

### 步骤 2：填充 raw 文件夹（10 分钟）

**可以放入的内容**：
- 复制粘贴文章到 .md 或 .txt 文件
- 保存截图或图表为图像
- 从任何应用导出笔记
- 粘贴会议笔记、研究论文、项目文档
- 倾倒数月来收藏的书签

**关键原则**：
```
❌ 不要组织它
❌ 不要重命名任何东西
❌ 不要清理它
✅ 那是 AI 的工作
```

---

### 步骤 3：自动化源收集（可选）

**工具**：Vercel Labs 的 `agent-browser`

```bash
npm install -g @vercel/agent-browser
agent-browser install-chrome
```

**优势**：
- AI 可控制真实浏览器
- 抓取任何网页，提取文本
- 直接保存到 raw/ 文件夹
- 比 Playwright MCP 少用 82% token

---

### 步骤 4：编写 Schema 文件（5 分钟）

**创建文件**：`CLAUDE.md`（或 `AGENTS.md`）

**文件作用**：告诉 AI 知识库关于什么以及如何组织它。

**Karpathy 确认**：
> 他保持 schema"超级简单和扁平"在 AGENTS.md 文件中。无数据库。无插件。只是告诉 AI 规则的文本文件。

---

### 步骤 5：告诉 AI 编译 Wiki（15 分钟）

**提示词**：
```
Read everything in raw/. Then compile a wiki in wiki/ 
following the rules in CLAUDE.md. Create an INDEX.md first, 
then create one .md file per major topic. Link related topics. 
Summarize every source.
```

**完成时你将拥有**：
- wiki/ 文件夹充满组织好的文章
- 你没看到的连接
- 你忘记保存的东西的摘要
- 使一切可秒搜索的索引文件

**关键原则**：
> 你不用手编辑 wiki。那是 AI 的工作。你阅读它，你问问题，AI 保持更新。

---

### 步骤 6：问问题并保存答案（持续）

**当 wiki 有 10+ 文章时**：

**示例问题**：
```
"Based on everything in wiki/, what are the three biggest 
gaps in my understanding of [topic]?"

"Compare what source A says about [concept] vs what source B 
says. Where do they disagree?"

"Write me a 500-word briefing on [topic] using only what's 
in this knowledge base."
```

**保存答案**：
- 将输出放入 outputs/
- 或让 AI 用新洞察更新相关 wiki 文章

**复合循环**：
> 每个问题使下一个答案更好。这就是循环。

---

### 步骤 7：运行健康检查（每月）

**提示词**：
```
Review the entire wiki/ directory. Flag any contradictions 
between articles. Find topics mentioned but never explained. 
List any claims that aren't backed by a source in raw/. 
Suggest 3 new articles that would fill gaps.
```

**关键洞察（来自 @HFloyd）**：
> "When outputs get filed back, errors compound too."

**问题**：如果 AI 写了稍错的东西你保存回去，下一个答案建立在那个错误之上。

**修复**：运行定期健康检查。

---

### 步骤 8：你不需要 Obsidian（但可以用）

**Karpathy 实际说的**：
> "I'm trying to keep it super simple and flat. It's just a nested directory of .md files."

**整个产品**：
```
一个文本文件夹 + 一个 schema 文件
```

**警告**：
> Obsidian 带 47 个插件是 Notion 陷阱重演。你花更多时间配置工具而非使用知识库。扁平文件 + 好 schema 90% 时间胜过花哨工具栈。

**建议**：
> 停止寻找完美工具。开始构建。

---

## 核心洞察

### 洞察 1：简单战胜复杂

**Karpathy 哲学**：
```
超级简单 + 扁平
  ↓
嵌套 .md 文件目录
  ↓
无数据库 + 无插件
```

**为什么有效**：
- ✅ 无学习曲线
- ✅ 无供应商锁定
- ✅ 纯文本永不过时
- ✅ AI 原生格式

---

### 洞察 2：AI 做繁重工作

| 人类角色 | AI 角色 |
|----------|--------|
| 策划源 | 组织 raw/ 到 wiki/ |
| 问问题 | 创建连接 |
| 阅读输出 | 写摘要 |
| 思考意义 | 维护一致性 |
| | 运行健康检查 |

**关键**：
> 不要手动组织。那是 AI 的工作。

---

### 洞察 3：复合效应

**循环**：
```
问问题 → 保存答案 → wiki 更丰富 → 更好答案
```

**每次使用**：
- 添加新源到 raw/
- AI 更新 wiki/
- 问新问题
- 保存新洞察

**结果**：
> 知识库每次使用变得更聪明。

---

### 洞察 4：错误复合风险

**@HFloyd 洞察**：
> "When outputs get filed back, errors compound too."

**问题**：
```
AI 写稍错内容 → 你保存回去
  ↓
下一个答案建立在错误上
  ↓
错误传播和放大
```

**解决**：
- ✅ 每月健康检查
- ✅ 标记矛盾
- ✅ 验证声称有源支持
- ✅ 填补空白

---

## 工具推荐

### 必需工具

| 工具 | 用途 | 必需性 |
|------|------|--------|
| **文本编辑器** | 查看/编辑 .md 文件 | 必需 |
| **AI 编码代理** | 编译 wiki、回答问题 | 必需 |
| **文件夹结构** | raw/wiki/outputs | 必需 |

### 可选工具

| 工具 | 用途 | 推荐度 |
|------|------|--------|
| **agent-browser** | 自动化网页抓取 | ⭐⭐⭐⭐ |
| **Obsidian** | 可视化浏览（可选） | ⭐⭐ |
| **VS Code** | 代码编辑（可选） | ⭐⭐⭐ |

---

## 对比：传统笔记 vs 第二大脑

| 维度 | 传统笔记 | 第二大脑 |
|------|----------|----------|
| **组织** | 手动 | AI 自动 |
| **连接** | 手动链接 | AI 发现 |
| **搜索** | 关键词 | 语义 + 上下文 |
| **更新** | 手动维护 | AI 持续更新 |
| **复合** | 无 | 每次使用更聪明 |
| **工具** | 多应用 | 文件夹 + 文本 |
| **锁定** | 供应商锁定 | 纯文本无锁定 |

---

## 相关链接

- [[second-brain-part2-system]] - 第二大脑完整系统（三层设计 + 四操作循环）
- [[llm-knowledge-base-complete-guide]] - LLM 知识库完整教程（3 级别）
- [[ai-knowledge-layer-two-tier]] - AI Knowledge Layer 两层系统
- [原文推文](https://x.com/nickspisak_/status/2040448463540830705)
