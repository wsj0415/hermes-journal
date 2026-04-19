# 🐦 X 推文总结：Grep Is Dead - 让 Claude Code 真正记住上下文

**日期**: 2026-03-06  
**来源**: X/Twitter  
**作者**: @ArtemXTech (Artem Zhutov)  
**原文链接**: https://x.com/artemxtech/status/2028330693659332615  
**互动数据**: 👍 2,574 | 🔄 198 | 👁 847,926 | ⭐ 8,779  
**爆款指数**: ⭐⭐⭐⭐⭐ (收藏率 1.03%，超高价值)

---

## 📋 核心摘要

**问题**: 每次与 Claude Code 对话都从零开始，700 次会话/3 周，无法追溯历史决策和上下文。

**解决方案**: 使用 **QMD 本地搜索引擎** + **/recall skill**，在对话前自动加载完整上下文。

**核心洞察**: "Tools change. Your context stays." - 工具会变，但上下文永远有价值。

---

## 🎯 痛点分析

### 当前问题

| 场景 | 问题 | 后果 |
|------|------|------|
| **新会话** | 每次打开新终端都从零开始 | 700 次会话后完全失控 |
| **会话中途** | 达到 60% 上下文限制需压缩 | 一半决策丢失 |
| **隔天继续** | 不记得之前发生了什么 | 需要重新解释一切 |
| **文件搜索** | grep 暴力匹配字符串 | 3 分钟等待，结果差 |

> "Every conversation with Claude Code starts from zero. I'm losing control."

---

## 🛠️ 解决方案：QMD + /recall

### QMD 是什么？

**QMD** = 本地搜索引擎，由 Shopify CEO @tobi 开发

**功能**: 
- 索引 Obsidian 知识库
- 1 秒内搜索任何内容
- 三种搜索模式 (BM25/语义/混合)

**安装**:
```bash
# 索引你的 vault
qmd index /path/to/vault
```

---

### 三种搜索模式对比

| 模式 | 命令 | 原理 | 速度 | 适用场景 |
|------|------|------|------|----------|
| **BM25** | `qmd search` | 全文搜索，按词频评分 | 2 秒 | 结构化笔记 (80% 搜索) |
| **语义** | `qmd vsearch` | 嵌入向量，理解含义 | 较快 | 转录/头脑风暴 |
| **混合** | `qmd query` | BM25 + 语义结合 | 中等 | 最佳结果 |

---

### 实战对比：搜索 "sleep"

| 方法 | 结果数 | 质量 | 时间 |
|------|--------|------|------|
| **grep** | 200 个文件 | ❌ 包含 sleep() 函数 | 3 分钟 |
| **BM25** | 精准结果 | ✅ 睡眠质量反思 | 2 秒 |
| **语义** | 5 个结果 | ✅ 4 个不含 "sleep" 关键词 | 瞬间 |
| **混合** | 5 个结果 | ✅ 相关性评分 89%/51%/42% | 瞬间 |

**关键差异**:
- grep 匹配字符串 → 找到 `sleep()` 函数 (无关)
- BM25 按词频评分 → 找到睡眠质量实验笔记
- 语义搜索 → 找到 "couldn't sleep, bad night" 相关目标 (无关键词)

---

## 🧠 /recall Skill - 对话前加载上下文

### 三种模式

| 模式 | 命令 | 功能 |
|------|------|------|
| **时间** | `/recall yesterday` | 按日期扫描会话历史 |
| **主题** | `/recall topic graph` | BM25 搜索 QMD 集合 |
| **图谱** | `/recall graph last week` | 交互式可视化 |

### 实战案例

#### 1. 重建昨天 (39 次会话)
```
/recall yesterday
```
**输出**: 时间线、消息数、完成内容

#### 2. 主题搜索 (1 分钟内)
```
/recall topic "QMD video"
```
**结果**: Dashboard、生产计划、待办清单

#### 3. 图谱可视化
```
/recall graph last week
```
**效果**: 
- 会话 = 彩色气泡 (旧的变暗，新的紫色高亮)
- 文件按类型聚类 (目标/研究/语音/文档/内容/skills)

---

## 💡 惊喜发现

### 1. 未执行的想法

搜索 "find the ideas that I have never acted on" 发现：
- 10 月 19 日：想建 PhD 写作 Dashboard 但未做
- 基于插图的应用想法但未跟进
- 想录 Obsidian 工作流屏幕录制但未执行

### 2. 被遗忘的洞察

搜索 "happy days" 发现：
- 最快乐的日子 = 发布产品 + 良好睡眠恢复 (桑拿/9 小时睡眠)

搜索 "PhD thesis" 发现：
- 10 月写论文时想放弃的记录
- 关键洞察："需要坚持度过不适，而非逃避到快速修复"

> "I didn't remember writing that. I didn't expect the search could surface this."

---

## 📊 技术细节

### 会话数据处理

```
Claude Code 会话 → JSONL 文件 → 解析 Markdown → 提取用户消息 → 嵌入到 QMD 索引
```

**自动化**:
- 每次会话结束时自动 hook
- 导出并嵌入到 QMD
- 索引始终保持最新

### 架构

```
┌─────────────┐
│ Obsidian    │
│ Vault       │
└──────┬──────┘
       │ QMD Index
       ▼
┌─────────────┐
│ /recall     │
│ Skill       │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Claude Code │
│ (任何会话)   │
└─────────────┘
```

---

## 🔄 跨设备同步

**配置**:
1. Mac + Mac Mini (常开)
2. Obsidian Sync 同步 vault
3. Mac Mini 运行 OpenClaw 24/7
4. 手机访问 OpenClaw

**效果**: 任何设备都有相同的 vault、QMD 索引、skills

---

## 🎯 核心价值主张

| 传统方式 | QMD + /recall |
|----------|---------------|
| ❌ 每次从零开始 | ✅ 自动加载上下文 |
| ❌ grep 3 分钟 | ✅ 搜索 1 秒 |
| ❌ 字符串匹配 | ✅ 语义理解 |
| ❌ 决策丢失 | ✅ 700 次会话可追溯 |
| ❌ 工具依赖 | ✅ 上下文永久保留 |

> "Tools change. A month from now there are going to be new models. So what. If you have your context you can make it work in any situation."

---

## 📦 安装指南

### 1. 安装 QMD
```bash
# GitHub
git clone https://github.com/tobi/qmd
```

### 2. 安装 /recall Skill
```bash
# 下载 skill 到 .claude/skills/ 文件夹
# 或让 Claude Code 帮你安装
```

### 3. 配置索引
```bash
# 为每个 vault 文件夹创建 QMD collection
qmd index /path/to/notes
qmd index /path/to/sessions
qmd index /path/to/transcripts
```

### 4. 设置自动导出
```bash
# 在会话结束时 hook 导出
# 自动嵌入到 QMD 索引
```

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **QMD GitHub** | https://github.com/tobi/qmd |
| **完整视频** | https://youtu.be/RDoTY4_xh0s (42 分钟) |
| **作者** | @ArtemXTech |
| **QMD 作者** | @tobi (Shopify CEO) |

---

## 💡 关键洞察

1. **grep 已死** - 字符串匹配无法扩展到大规模知识库
2. **上下文是资产** - 工具会变，但上下文永久有价值
3. **语义搜索威力** - 能找到不含关键词但含义相关的内容
4. **自动化是关键** - 会话结束自动导出，索引始终新鲜
5. **跨工具通用** - Claude Code/Codex/Gemini CLI 都能用

---

## ⚠️ 注意事项

| 事项 | 说明 |
|------|------|
| **本地优先** | 所有嵌入都在本地计算机 |
| **隐私安全** | 数据不出本地 |
| **Obsidian 依赖** | 需要 Obsidian vault 结构 |
| **学习曲线** | 需要理解三种搜索模式差异 |

---

## 📌 行动建议

### 立即开始
1. 安装 QMD (`git clone https://github.com/tobi/qmd`)
2. 下载 /recall skill 到 `.claude/skills/`
3. 索引现有笔记和会话

### 持续优化
1. 设置会话结束自动导出 hook
2. 配置 Obsidian Sync 跨设备同步
3. 定期使用 `/recall` 发现未执行想法

### 高级用法
1. 为不同项目创建独立 QMD collections
2. 使用图谱可视化探索会话关联
3. 定期搜索 "未执行想法" 并行动

---

**总结生成**: KilroyContentBot  
**抓取工具**: x-fetcher  
**仓库**: https://github.com/wsj0415/kilroy-cdn  
**分类**: AI 工具/知识管理/Claude Code
