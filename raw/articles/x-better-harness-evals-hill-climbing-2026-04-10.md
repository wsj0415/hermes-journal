# Better Harness — 用 Evals 驱动 Agent 自主进化

**来源**: https://x.com/vtrivedy10/status/2041927488918413589  
**抓取时间**: 2026-04-10 01:36 UTC  
**类型**: X Article 长文  
**标签**: ai-agent, harness-engineering, evals, autonomous-evolution, machine-learning, overfitting-prevention, trace-analysis, regression-testing, tdd-for-agents, deep-agents

---

## 📊 一句话总结

Better-Harness 是一个原型系统，通过迭代来源和改进 harness，用 evals 作为"训练数据"来驱动 agent 自主进化。核心类比：传统 ML 用 training data + gradient descent 改进模型，Agent 用 evals + harness engineering 改进 agent。6 步流程：来源标记→拆分优化/保留集→基线→优化→验证→人工审查。

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:Harness 爬山流程图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a clean technical flowchart for "Better Harness — 6-Step Hill-Climbing with Evals".

Title: "Better Harness"
Subtitle: "用 Evals 驱动 Agent 自主进化"

Layout: Vertical 6-step pipeline with feedback loop.

Color Palette:
- Steps: Blue (#3B82F6)
- Validation: Green (#10B981)
- Warning: Yellow (#FBBF24)
- Background: Dark gradient (#0F172A to #1E293B)
- Text: White

6 Steps (top to bottom):

S1 — Source & Tag Evals:
图标：数据来源
内容：手写 + 生产 Trace + 外部数据集
标签："Tag 行为类别"

S2 — Split Data:
图标：拆分数据集
内容：Optimization Set | Holdout Set
警告："防止过拟合关键"

S3 — Run Baseline:
图标：基线测试
内容：优化集 + 保留集前测
标签："Ground all updates"

S4 — Optimize:
图标：自主优化
内容：诊断错误→实验 harness 变更
标签："一次一个变更"

S5 — Validate:
图标：验证检查
内容：新 evals 通过 + 无回归
标签："检查泛化能力"

S6 — Human Review:
图标：人工审查
内容：检查过拟合指令 + 浪费 token
标签："最终闸门"

Feedback Loop (右侧):
"Trace → Eval → Better Harness"
"更多使用 → 更多 Trace → 更多 Evals"

Bottom Section - Analogy:

传统 ML:
model + training data + gradient descent → better model

Agent Harness:
harness + evals + harness engineering → better agent

Badge:
"泛化而非过拟合"
"6 步自主爬山"
"Trace 是金矿"

Style: Clean technical flowchart, dark mode with neon blue/green accents
Aspect ratio: 9:16 portrait
```

---

### 选项 2：Evals 来源对比

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules for "Evals as Training Data for Harness Engineering".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Green (#10B981)
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Evals = Harness 的训练数据"
"质量 > 数量"
Icon: Brain + data

M2 — Evals 来源:
手写（高价值难扩展）
生产 Trace（高杠杆）
外部数据集（需策展）

M3 — 过拟合问题:
"Agent 是著名作弊者"
"Reward Hacking"
"Make number go up"

M4 — 解决方案:
"Holdout Set"
"人工审查"
"半自动系统"

M5 — 6 步流程:
Source → Split → Baseline
Optimize → Validate → Review

M6 — Flywheel:
"更多使用 → 更多 Trace"
"更多 Evals → 更好 Harness"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心类比

### 传统机器学习
```
model + training data + gradient descent → better model
```

### Agent Harness 工程
```
harness + evals + harness engineering → better agent
```

**Evals 编码了我们希望 agent 在生产中表现的行为**。每个 eval 案例贡献一个信号："agent 是否采取了正确的行动"或"产生了正确的结果？"这个信号指导下一个 harness 编辑提案。

---

## Evals 来源方式

### 1. 手写策划 (Hand-curated)
- **优点**: 高价值，精准捕获预期行为
- **缺点**: 难以规模化生成
- **适用**: 关键任务场景

### 2. 生产 Trace (Production traces)
- **来源**: 每个 agent 交互生成 trace，失败成为 eval 案例
- **杠杆**: 高吞吐量，持续改进
- **推荐**: Dogfooding agent，在 Slack 直接分享反馈和 Trace 链接

### 3. 外部数据集 (External datasets)
- **用途**: 有用但需手动策展
- **调整**: 确保测试案例反映期望行为

### 4. Tag 一切
- **行为类别**: "tool selection", "multi-step reasoning" 等
- **好处**: 
  - 支持有意义的保留集
  - 针对性实验
  - 节省成本（可运行子集）

---

## 泛化 vs 过拟合

### 理想结果
学习系统的理想结果是**泛化**：输入信号捕获我们想要的行为分布，系统拟合后在未见输入上"just works"。

### 明显问题
**数据有限** — 我们没有无限数据

**解决方案**: 将重要行为编码到策划的 evals 中。**质量 > 数量**，一小套精心标记覆盖关键行为的 evals 胜过数千个噪音但高覆盖的 evals。

### 隐蔽问题
**Agent 是著名作弊者** — 任何学习系统都倾向于 reward hacking，agent 会过拟合其结构以通过现有 evals。

**原因**: 循环只想"make number go up"，不知道泛化。

**解决方案**: 
1. **Holdout sets** — 作为真正泛化的代理
2. **人工审查** — 作为第二信号
3. **半自动系统** — 改进分数的同时避免我们不想要的生产行为

---

## 6 步自主爬山流程

### Step 1: 来源和标记 Evals
```
来源混合：
- 手写 evals
- 从生产 Trace 挖掘
- 使用/调整外部数据集

标记：
- 行为类别（如 multi-step retrieval）
- 定期移除饱和或不再有用的 evals
```

### Step 2: 拆分数据
```
按类别拆分：
- Optimization Set（优化集）
- Holdout Set（保留集）

关键：
- 自主爬山倾向于过拟合任务
- Holdout 确保学习优化在未见数据上有效
- 一般分布应匹配现有 evals
```

### Step 3: 运行基线
```
在任何编辑前：
- 在优化集和保留集上运行基线实验
- 将所有更新基于此基础
```

### Step 4: 优化
```
每次迭代自主运行（可选人工审查）：

1. 从 Trace 诊断错误
2. 实验针对性 harness 变更
3. 范围限定为一次一个变更（避免混淆）
4. 可能同时更新提示词和工具（系统协同工作）
```

### Step 5: 验证
```
每步检查：
- 拟议变更是否帮助通过新 evals
- 避免现有通过案例的回归

常见情况：
- 某些变更导致净分数增益但有回归
- agent 获得这些回归的上下文
- 下次更新尝试修复而不损失现有增益
```

### Step 6: 人工审查
```
手动审查：
- 变更和边缘情况（指标可能遗漏）
- 过拟合到优化集的指令
- 虽不伤害泛化但浪费 token

作用：
- 额外健全检查
- 防止过拟合的闸门
```

---

## Harness 变更类型

### 1. 提示词和指令更新（最常见）
**问题**: agent 持续误解工具输出格式，或过于激进调用工具而非先问澄清问题

**修复**: 针对性指令更新
```
"当查询多个具有依赖信息的文件时，
将信息卸载到文件系统并在给出最终答案前重新聚合"
```

### 2. 添加或更新工具/工具描述
**问题**: agent 在何时使用新工具时失败

**编辑包括**:
- 如何使用示例
- 如何链接此工具
- 更新工具描述
- 编辑整体工具套件以消除相似工具的歧义

---

## 实验结果

### 测试设置
- **模型**: Claude Sonnet 4.6 + GLM-5
- **数据**: 现有 eval 类别的小代表性样本
- **拆分**: 爬山集 + Holdout 集评估泛化
- **建议**: 大/贵 eval 集用代表性/分层采样

### 主要目标
发现并修复 evals 上的失败模式，将提高 eval 性能的通用变更移植回 harness。

### 观察的失败模式
- 过度询问后续问题
- 链接新工具时的错误

### 结果
两个模型在两个类别上都表现强劲：
- **tool_selection**: 几乎完全泛化到保留集
- **followup_quality**: 几乎完全泛化到保留集

**关键**: 保留集用完全未见案例覆盖相同能力。

### 具体发现
许多收益来自对发现失败模式的更明确指令。

**示例**: 对于注入新工具（如 search-then-email）的 evals，循环发现了更好的工具使用和组合描述。

**前景**: 对创建跨领域垂直 agent 的构建者有希望，因为优化循环能很好地适应上下文中的任务细节。

---

## 防止回归

### Eval 作为回归测试
```
一旦 agent 正确处理案例 → 不想失去收益
Eval 成为回归测试
类似传统软件工程的 TDD（Test Driven Development）
```

### 回归检测
```
某些回归注定会随时间发生
选择我们总是想通过的 eval 子集
如果这些突然失败 → 可疑地查看运行
```

### Eval 清理
```
Eval 套件不应单调增长
定期评估 eval 是否仍有用：
- 更智能的模型
- 不同的期望行为

Spring cleaning of evals is good!
```

---

## Trace 的价值

### Trace 提供密集反馈信号

**Evals 受益于 Trace**:
- 跨版本比较
- 数值化衡量哪些变更贡献更好分数
- 更好分数的代理是更好用户体验

### 用 Trace 做什么

1. **自动派生错误**
   - 持续监控生产中的 agent Trace
   - 分类和聚类失败

2. **从生产生成 Evals**
   - agent 犯错的 Trace = eval 案例
   - 用户纠正 agent 的 Trace 更好
   - **Flywheel**: 更多使用 → 更多 Trace → 更多 Evals → 更好 Harness

3. **比较 Harness 版本**
   - 并排 Trace 比较显示 harness 中什么变更导致新行为

### 日志记录
所有 agent 运行都记录到 **Langfuse**（或其他 Trace 工具），包含完整 Trace。

**用途**:
- Trace 级别诊断（优化循环）
- 生产监控（回归检测）
- Trace 挖掘（eval 生成）

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Eval 来源 | 3 种（手写/Trace/外部） |
| 流程步骤 | 6 步 |
| 测试模型 | 2 个（Sonnet 4.6, GLM-5） |
| 评估类别 | 2 个（tool_selection, followup_quality） |
| 泛化结果 | 几乎完全泛化到保留集 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Evals 是自主 harness 工程的训练数据" | 核心类比 |
| "Agent 是著名作弊者" | 过拟合风险 |
| "质量 > 数量" | Eval 策展原则 |
| "Holdout Set 是泛化代理" | 防止过拟合 |
| "更多使用 → 更多 Trace → 更多 Evals" | 飞轮效应 |
| "Spring cleaning of evals is good" | 定期清理 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Evals 作为训练数据** — 内容创作也可建立 evals
2. **6 步流程** — 可用于工作流优化
3. **Holdout Set** — 防止过拟合到特定内容类型
4. **Trace 分析** — 记录每次会话用于改进
5. **回归测试** — 确保改进不破坏现有功能

### 可实施
- 建立内容创作 evals（标题吸引力、结构完整性、平台适配度）
- 拆分优化/保留集测试新工作流
- 记录每次会话到 Trace 系统
- 定期清理不再有用的 evals
- 用生产 Trace 挖掘新 evals

---

*原始来源：https://x.com/vtrivedy10/status/2041927488918413589*
