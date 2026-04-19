---
title: Claude Code 最佳实践
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [skills, best-practice, workflow, agent-design]
sources: [raw/articles/ai-influence-weekly-report-001-2026-04-17.md]
reviewed: false
confidence: high
confidence_reason: 基于 Anthropic 团队成员 @trq212 的官方分享
---

## 编译知识

Claude Code 是 Anthropic 的终端编码代理。以下是来自 Anthropic 团队成员的官方最佳实践。

### 会话管理与 1M 上下文

**上下文窗口包含:**
- 系统 prompt
- 对话历史
- 所有工具调用及输出
- 已读取文件

**五个决策点:**
1. **Continue** - 继续当前任务
2. **Rewind** - 回退到之前的状态
3. **Clear** - 清空上下文重新开始
4. **Compact** - 压缩当前上下文
5. **Subagents** - 派生子代理处理独立任务

**关键洞察:**
- 坏压缩的原因：模型在压缩时无法预测你下一步要做什么
- 主动管理上下文比被动等待压缩效果更好
- 在任务转折点主动 `/compact` 并说明下一步方向，可避免关键信息丢失

### Prompt Hooks 实践

**用途:**
- 基于 prompt 的停止钩子，让 Claude 工作更长时间
- 自动完成清理工作：删除多余文件、编写测试、更新文档
- 在任务完成前不中断，保证输出完整性

**解决的问题:**
AI"做一半就跑"的问题。设置完成钩子让 AI 自动收尾，产出可直接使用的结果而非半成品。

### /insights 命令

- 总结你的项目和使用 Claude Code 的方式
- 提供改进工作流的建议
- 帮助识别低效模式

**相关页面:**
- [[hermes-system-prompt-structure]] - Hermes Agent 系统提示词结构
- [[agent-memory-architecture]] - Agent Memory 架构演进

---

## 时间线

- 2026-04-17: 从第一期 AI 影响力周报中提取最佳实践
- 2026-04-18: 创建本页面，整合 Claude Code 使用策略
