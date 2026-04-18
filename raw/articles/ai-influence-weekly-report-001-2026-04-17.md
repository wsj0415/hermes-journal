# AI 影响力周报 第 1 期

**收集时间:** 2026-04-17T01:08:30
**扫描账号:** 20 个 AI 领域影响力账号
**候选推文:** 87 条
**精选数量:** 8 条 (9%)

---

## 本期摘要

本周精选 8 条高价值内容，涵盖 Claude Code 会话管理、Gemini 3 应用开发、Prompt Engineering 最新实践、LLM 研究工具等方向。

**核心趋势:**
- Agent 工作流优化成为焦点（Claude Code 1M 上下文、prompt hooks）
- 多模态生成进入实用阶段（Gemini 3 单 prompt 构建完整应用）
- Prompt Engineering 从"技巧"转向"流程工程"

---

## 可复用方法

### 1. Claude Code 会话管理与 1M 上下文使用策略
**来源:** @trq212 (Anthropic 团队成员)
**链接:** https://x.com/trq212/status/2044873898572001376

**核心内容:**
- 上下文窗口包含：系统 prompt、对话历史、所有工具调用及输出、已读取文件
- 五个决策点：Continue / Rewind / Clear / Compact / Subagents
- 坏压缩的原因：模型在压缩时无法预测你下一步要做什么

**为什么有用:**
使用 1M 上下文时，主动管理上下文比被动等待压缩效果更好。在任务转折点主动 `/compact` 并说明下一步方向，可避免关键信息丢失。

---

### 2. LLM 辅助 Coding 的 Prompt 优化模式
**来源:** @karpathy
**链接:** https://x.com/karpathy/status/1642598890573819905

**核心内容:**
- 从"prompt:answer"范式转向"flow"范式
- 使用 prompt 定义 I/O 设备规范、工具规格、认知循环
- 将数据分页进出上下文窗口，然后 `.run()` 执行

**为什么有用:**
传统 prompt 是一次性交易，flow 是持续性流程。定义清晰的输入输出规范和工具接口，让 AI 在边界内自主迭代，产出质量更稳定。

---

### 3. OpenAI GPT-4.1 Agent 构建 Prompt 指南（带实测数据）
**来源:** @swyx
**链接:** https://x.com/swyx/status/1911849229188022278

**核心内容:**
- 告诉模型保持 persistent（+20% 任务完成率）
- 明确的工具调用规范比模糊指令效果好 3 倍
- 深研报告 prompt 重写器开源可用

**为什么有用:**
这是 OpenAI 官方发布的 Agent 构建最佳实践，附带 A/B 测试数据。直接复用这些 prompt 模式可显著提升 Agent 任务完成率。

---

## 工作流优化

### 4. Gemini 3 单 Prompt 构建完整 Web 应用
**来源:** @GoogleDeepMind
**链接:** https://x.com/GoogleDeepMind/status/1990812981878235253

**核心内容:**
- 单个 prompt 可生成可交互的 Web 应用、游戏、模拟器
- 支持从多张图片中提取元素并融合
- 理解设计意图而非机械执行指令

**为什么有用:**
快速原型验证的神器。用自然语言描述需求，30 秒内生成可交互 demo，适合产品概念验证和内部演示。

---

### 5. Claude Code Prompt Hooks 实践
**来源:** @trq212
**链接:** https://x.com/trq212/status/1986121725487251894

**核心内容:**
- 基于 prompt 的停止钩子，让 Claude 工作更长时间
- 自动完成清理工作：删除多余文件、编写测试、更新文档
- 在任务完成前不中断，保证输出完整性

**为什么有用:**
解决 AI"做一半就跑"的问题。设置完成钩子让 AI 自动收尾，产出可直接使用的结果而非半成品。

---

### 6. 教师使用 ChatGPT 课堂指南
**来源:** @OpenAI
**链接:** https://x.com/OpenAI/status/1697295029763715166

**核心内容:**
- 建议的 prompt 模板（解释概念、生成练习题、反馈作文）
- ChatGPT 工作原理说明（帮助学生理解局限性）
- 课堂活动设计示例

**为什么有用:**
这是教育场景的标准化 prompt 库。即使非教育行业，这些 prompt 模板也可迁移到培训、onboarding 等场景。

---

## 新工具

### 7. Gemini 3.1 文本转语音模型 Prompt 指南
**来源:** @demishassabis
**链接:** https://x.com/demishassabis/status/2044609360299426263

**核心内容:**
- 用 prompt 控制语音情感、语速、停顿
- 支持多语言混合输出
- 可生成播客级质量的音频

**为什么有用:**
内容创作者可直接用文本生成配音，无需录音设备。适合视频旁白、课程音频、播客草稿。

---

### 8. LLM 知识库研究工具
**来源:** @karpathy
**链接:** https://x.com/karpathy/status/2039805659525644595

**核心内容:**
- 用知识库管理大型代码库的 LLM 查询
- 支持合成数据生成
- 随着 repo 增长自动扩展索引

**为什么有用:**
大项目专属的"AI 搜索引擎"。避免每次查询都读取整个代码库，显著提升响应速度和准确性。

---

## 数据来源

- 原始候选数据：`~/.hermes/output/ai-influence-digest/candidates.json`
- 扫描账号列表：65 个 AI 领域影响力账号
- 生成技能：ai-influence-digest
