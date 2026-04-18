---
title: Karpathy 的 AI 工程理念
created: 2026-04-18
updated: 2026-04-18
type: entity
tags: [person, ai-trends, agent-design, best-practice]
sources: [raw/articles/ai-influence-weekly-report-001-2026-04-17.md]
reviewed: false
confidence: high
confidence_reason: 基于多期周报中 karpathy 推文的综合提炼
---

## 编译知识

Andrej Karpathy 是 AI 工程化和 LLM 辅助编程的核心布道者。他的理念强调**流程优于技巧**。

**核心主张:**

### 1. Flow > Prompt
- 从"prompt:answer"范式转向"flow"范式
- 用 prompt 定义 I/O 设备规范、工具规格、认知循环
- 将数据分页进出上下文窗口，然后 `.run()` 执行
- 传统 prompt 是一次性交易，flow 是持续性流程

### 2. LLM 知识库模式
- 为大型代码库建立专属"AI 搜索引擎"
- 避免每次查询都读取整个代码库
- 随着 repo 增长自动扩展索引
- 支持合成数据生成

### 3. 最优 LLM 辅助编码体验
- 定义清晰的 agent 迭代边界
- prompt 定义训练代码的 I/O 规范
- AI agent 在边界内自主迭代训练代码
- 目标是让 agent 以最快的速度推进研究

**相关项目:**
- [[llm-wiki-karpathy]] - Karpathy 风格的 LLM Wiki 模式
- [[ai-engineering-from-scratch]] - AI Engineering 从零开始课程

---

## 时间线

- 2026-04-17: 从第一期 AI 影响力周报中提取核心理念，创建本页面
