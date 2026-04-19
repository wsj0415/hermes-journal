# 网页分析：Prompt Caching 第一性原理 — 降低 90% 成本的技术详解

**来源**: lossfn.com  
**链接**: https://lossfn.com/blog/prompt-caching/  
**类型**: 技术博客  
**抓取时间**: 2026-04-08 10:44 UTC

---

## 📊 核心洞察

**一句话总结**: Prompt Caching 通过复用稳定前缀的计算状态，实现输入成本降低 10 倍、延迟降低 80%，核心原理是因果注意力机制中后续 token 无法改变已计算的前缀状态。

---

## 🎯 完整翻译

### 引言

在 [Summation](https://www.summansion.com/) 应用中，每个 LLM 请求都从相同的大前缀开始：一个系统提示加上客户端特定的语义层，包含表结构、列描述和业务规则。这个前缀可能长达数千 token，且数小时不变。而用户的实际问题通常只有一句话。

我们一直在为重新计算这个相同的前缀支付全价。首 token 时间主要由我们已经做过的工作主导。

**Prompt caching 解决了经济性问题**。对于稳定的前缀，输入成本下降了约 **10 倍**，缓存的请求响应速度明显更快。

但大多数解释停留在"相同前缀变得更便宜"。它们没有解释什么被复用、为什么空格会破坏命中、为什么温度不重要。

这篇文章从第一性原理构建机制。我们将追踪一个提示通过 transformer 流水线，隔离确定性部分，并展示为什么提供商可以在请求间复用它们。

---

## 🏭 流水线

当你发送文本到 LLM 时，它经过四个阶段。把它想象成流水线：文本从一端进入，预测的 token 从另一端出来。

让我们追踪一个真实提示 "May the force" 通过每个阶段。

---

### Stage 1: Tokens（Token 化）

LLM 不操作原始文本。它们操作数字，所以第一步是将文本转换为整数序列。

这就是 **tokenizer**（分词器）的作用。它将文本切成 tokens，通常使用学习到的子词词汇，而不是整词或单字符。

```
输入文本：May the force
Token IDs（整数）: [7108, 262, 3081]
```

`"May the force"` 变成 `[7108, 262, 3081]`。三个整数。单词 "May" 映射到 7108。总是如此。无论你设置什么温度。这是一个确定性查找。

**关键属性**: 给定一个 tokenizer，相同的文本总是产生相同的 token IDs。这是纯查找，无随机性，无模型权重参与。**记住这一点。这是使缓存成为可能的基础。**

一些 token 整洁地映射到单词。其他映射到片段。对缓存来说重要的不是边界落在哪里，而是相同的文本产生相同的 token IDs。

---

### Stage 2: Embeddings（嵌入）

Token IDs 只是标签。**embedding**（嵌入）阶段将每个 token ID 映射到模型可以计算的稠密向量中。

嵌入后，每个 token 变成稠密向量：

```
Token 1 ("May"):   [0.12, -0.84, 0.33, 0.07, ...]  ← 3,072 个数字
Token 2 ("the"):   [0.56,  0.21, -0.17, 0.91, ...]
Token 3 ("force"): [-0.03, 0.67, 0.44, -0.22, ...]
```

逐行堆叠这些，得到一个矩阵。3 行（每个 token 一行）× 3,072 列（每个维度一列）。称这个矩阵为 **E**。

模型还注入位置信息。在简化图中，你可以将其视为将每个 token 嵌入与位置向量组合。无论实现使用加法嵌入、旋转编码还是其他，关键事实相同：位置 2 的 token `"the"` 与位置 5 的 token `"the"` 不是相同的状态。

这就是模型如何区分 `"dog bites man"` 和 `"man bites dog"`。相同 token，不同位置，不同输入状态。

**关键属性**: 相同 token 在相同位置总是产生相同输入状态。相同提示 + 相同模型 = 相同的起始表示。

---

### Stage 3: Attention（注意力）

这是 transformer 的核心。这是模型从孤立的 token 表示走向上下文理解的地方。

这是注意力回答的根本问题：

> **对于每个 token，它应该多关心之前的 token？**

"May" 本身是模糊的。它是月份吗？情态动词吗？愿望吗？

但 `"May the force"` 已经不那么模糊了。注意力是连接这些关系的机制。

#### Q、K、V 框架

模型学习三个投影：

- **Q (Query)**: 这个 token 在寻找什么
- **K (Key)**: 这个 token 提供什么
- **V (Value)**: 被混合到结果中的内容

我个人喜欢图书馆类比：

你带着问题走进来（你的 _Query_）。书架上的每本书在书脊上都有标签（它的 _Key_）。当你的问题匹配标签时，你抽出那本书并阅读其内容（它的 _Value_）。

简写形式：

```
Q = E × W_Q
K = E × W_K
V = E × W_V
```

这些投影在每个 transformer 层从该层的当前隐藏状态重新计算。对于 prompt 缓存，重要的部分更简单：对于固定前缀，模型每次都会计算相同的 K 和 V。

#### 注意力计算

现在看机制。

取我们提示中的最后一个 token：`"force"`。模型为 `"force"` 构建一个 **query**，并将其与它被允许看到的每个 token 的 **keys** 进行比较。分数越高，相关性越高。

换句话说：将当前 token 与每个早期 token 比较，并评分每个的相关性。但有一个约束。token 只能向左看。模型应用一个 **causal mask**（因果掩码），阻止每个 token 看到它之后的任何内容。

```
        May   the   force
May     ✓     ✗     ✗
the     ✓     ✓     ✗
force   ✓     ✓     ✓
```

`"May"` 只看到自己。`"the"` 看到 `"May"` 和自己。`"force"` 看到全部三个。早期行从不依赖后期 token。

掩码后，这些行仍然是原始相关性分数。模型接下来将每行归一化为注意力权重，使用 **softmax** 使权重加起来为 1。然后使用这些权重混合 **values**：分数较高的 token 贡献更多，分数较低的 token 贡献更少。结果是每个位置的新表示，被之前的 token 丰富。

**Softmax，用通俗英语解释**: 取一行分数，将其转化为一组加起来为 1 的份额，使模型可以将它们视为"多少注意力分配给每个 token"。

现在这是关键可视化。当我们追加 `"be"` 时会发生什么？

网格增长一行一列，但前三行不变。`"May"`、`"the"` 和 `"force"` 仍然看到它们之前看到的相同内容。追加新 token 只为该 token 的行创建新工作。

**这就是 prompt 缓存依赖的事实**。一旦模型计算了早期位置的注意力状态，后期 token 无法使其无效。

这在每个注意力层发生。你不需要每个实现细节来理解 prompt 缓存。你只需要这个结果：早期 token 的结果在追加后期 token 时不改变。

但我们只处理了输入。模型如何将这转化为实际的词？

---

### Stage 4: Prediction（预测）

在最终注意力层后，每个位置持有上下文感知的表示。但对于 next-token 预测，我们只关心 _最后_ 位置。

模型将最终向量投影到词汇大小的 logits：

```
logits = final_embedding × W_out
probs  = softmax(logits)
```

这就是 **temperature**（温度）进入的地方。温度在 softmax 之前缩放 logits。它改变模型如何从分布中采样，但不改变 token 化、嵌入、K 或 V。

这个细节很重要，因为它解释了一个常见困惑：改变温度可以改变输出，但不使 prompt 缓存无效。

模型从这个分布中采样，产生单个 token：`"be"`。

现在呢？我们需要生成 _剩余_ 的响应。

---

## 🔄 生成循环

LLM **一次一个 token** 生成文本。在通过所有阶段运行我们的 3-token 提示后，模型预测 `"be"`。要获得下一个词，它追加那个 token 并继续 `"May the force be"`。

需要注意的重要事情不是模型添加一个新 token。而是，天真地，它必须重新访问整个前缀来做这件事。

在 `"May the force"` 之后是 `"be"`，然后可能是 `"with"`，然后是 `"you"`。在每一步，可见上下文增长：

- `"May the force"`
- `"May the force be"`
- `"May the force be with"`
- `"May the force be with you"`

没有缓存，模型不断重新计算早期 token 的注意力状态，一次又一次。`"May"` 在每个解码步骤被处理。`"the"` 也是。`"force"` 也是。

**这就是浪费。**

对于玩具提示，这看起来无害。对于真实应用，不是。如果你的系统提示长 2,000 token，你生成 100 个输出 token，模型必须不断拖着那个长前缀通过循环。输入最昂贵的部分也是变化最少的部分：根本没有变化。

这是缓存首先付费的地方。实际上有两个独立的机会：

- **KV caching** 在 _单个请求内_ 解码期间保存重复工作
- **Prompt caching** 在 _多个请求间_ 共享前缀保存重复预填充工作

---

## 💾 KV Caching

**核心洞察**: 对于因果 transformer，位置 _i_ 的计算状态仅依赖于到位置 _i_ 的前缀和模型的权重。追加 token _i + 1_ 无法追溯改变它。

这正是 KV caching 利用的。

模型存储它已处理 token 的 K 和 V 张量。在下一个生成步骤，它只为新 token 计算新鲜的 Q、K 和 V，追加新的 K 和 V 行，并复用其余部分。

动画中需要注意的重要模式：

- **无 KV cache**: 模型不断重新计算旧行
- **有 KV cache**: 模型只计算一个新行并复用历史

我们缓存 K 和 V，因为它们是重的可复用历史。Q 仅需要当前 token。

---

## 🚀 Prompt Caching：跨请求应用

KV caching 在一个 API 调用内工作。Prompt caching 将相同思想应用到跨调用。

如果每个请求从相同的 2,000-token 系统提示开始，每个请求否则将从头重新计算相同的前缀状态，然后在结束时丢弃它。Prompt caching 保持那个可复用前缀周围，使下一个请求可以从缓存状态开始，而不是再次支付完整预填充成本。

这是一个具体例子。你在构建一个客服机器人。每个请求从相同的 2,000-token 系统提示开始（你的指令、角色、格式规则）。然后是用户的问题，每次不同：

```
请求 1:  [系统提示]  +  "如何重置密码？"
请求 2:  [系统提示]  +  "你们的营业时间是什么？"
请求 3:  [系统提示]  +  "我可以退款吗？"
```

共享的系统提示每次产生相同的 token、相同的位置，因此相同的可复用前缀状态。只有用户后缀变化。

有 prompt caching，提供商在第一次请求后存储那个前缀状态，并为后续请求复用。

**这就是为什么经济性这么好**。OpenAI 文档记录缓存命中时输入成本降低高达 90%，延迟降低高达 80%。Anthropic 定价缓存读取为基础输入费率的 0.1 倍，并允许你用 `cache_control` 显式标记可复用前缀。

### 相同机制，不同 API

底层思想在提供商间相同：如果前缀精确匹配，它们可以复用缓存的前缀状态。变化的主要是 API 形状。

**OpenAI** 倾向自动。在支持的模型上，精确前缀匹配可以缓存，无需你显式标记边界。

**Anthropic** 直接暴露该边界。你用 `cache_control` 标记可复用前缀，给你更多控制什么被缓存。

不同的人体工程学，相同规则：精确前缀匹配。如果前缀保持稳定，你赢。如果漂移，你输。

### 什么影响缓存

此时，实际问题很简单：请求间什么变化实际破坏复用？

决定缓存命中的是前缀本身，不是采样旋钮。Temperature、`top_p` 和 `top_k` 仅影响最终采样步骤，在前缀状态已计算之后。

**什么使缓存无效？**

改变前缀，即使一个 token，缓存从该点向前不再匹配。稳定内容属于前面。可变内容属于最后。

这就是为什么 prompt caching 是 **前缀形状** 的。提供商可以复用共享的提示开头，不是中间的任意片段。

如果你在构建应用，实用规则简单：保持提示前面稳定。

---

## 📋 缓存命中的实用技巧

理解理论是一回事。在生产中获得一致的缓存命中是另一回事。

**1. 把稳定内容放前面**。系统提示、格式规则、示例、工具 schema、长文档。可变内容属于末尾。

**2. 保持上下文追加式**。如果你在构建多轮对话，追加新轮次。不要重写或重新洗牌早期轮次，除非你愿意失去缓存。

**3. 确定性序列化**。如果你的提示包含 JSON 或结构化数据，保持键顺序和格式稳定。语义相同的 JSON 仍然可以不同地 token 化。

**4. 固定工具定义**。许多框架重新生成工具 schema，带有微小的顺序或空格变化。将工具定义视为不可变前缀内容。

**5. 监控你的缓存指标**。如果缓存 token 计数突然下降，将其视为提示回归。大多数缓存缺失由提示变化引起，不是提供商神秘问题。

---

## 🎯 完整图景

完全放大：

1. **文本确定性 token 化**
2. **这些 token 在位置固定后变成确定性输入状态**
3. **因果注意力意味着后期 token 无法改变计算的前缀状态**
4. **所以提供商可以存储那个前缀状态，并在相同前缀再次出现时复用**

一旦你看到那条链，prompt caching 停止感觉神奇。它变成提示设计约束。

**把可复用的东西放前面。保持稳定。将任何用户特定的东西移到末尾。**

这就是真正的回报。更低的成本和更快的首 token 时间不是幸运的副作用。它们是你的提示保持前缀时应该期待的。

---

## 📚 推荐深入阅读

- Sebastian Raschka 的 [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)
- Andrej Karpathy 的 [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) 系列
- Georgia Tech 的 [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) 交互式可视化
- Sankalp 的 [How Prompt Caching Works](https://sankalp.bearblog.dev/how-prompt-caching-works/)（实现侧：paged attention、vLLM 内部、块级哈希）

---

## 💡 实践建议

### 对 AI 应用开发者

| 场景 | 优化策略 | 预期收益 |
|------|----------|----------|
| 系统提示固定 | 将系统提示放最前，用户问题放最后 | 成本↓90%，延迟↓80% |
| 多轮对话 | 追加新轮次，不重写早期 | 保持缓存命中 |
| 工具定义 | 固定 schema 顺序和格式 | 避免缓存失效 |
| JSON 数据 | 保持键顺序稳定 | 语义相同≠token 相同 |

### 对 OpenClaw 用户的启示

当前 KilroyContentBot 的配置：
- ✅ SOUL.md/USER.md 作为系统提示（稳定前缀）
- ⚠️ 每次会话重新加载，未利用缓存
- ❌ 无 `cache_control` 标记

**可优化点**:
1. 将 SOUL.md + USER.md + TOOLS.md 合并为固定前缀
2. 在支持缓存的模型上使用 `cache_control` 标记
3. 保持记忆文件追加式更新，不重写

---

## 📈 关键数据

| 指标 | 数值 | 来源 |
|------|------|------|
| 输入成本降低 | 10 倍（90%） | OpenAI 文档 |
| 延迟降低 | 80% | OpenAI 文档 |
| 缓存读取价格 | 0.1x 基础费率 | Anthropic |
| 缓存失效原因 | 前缀变化（即使 1 token） | 本文分析 |

---

## 🎨 封面图提示词

### 选项 1：四层流水线架构图 ⭐ 推荐

```prompt
Create a vertical infographic for "Prompt Caching — 4 Stage Pipeline".

Title: "Prompt Caching 第一性原理"
Subtitle: "成本降低 90% 的技术详解"
Credit: "lossfn.com"

Layout: Vertical flow showing 4 stages with cache mechanism.

Color Palette:
- Tokenization: Blue (#3B82F6)
- Embeddings: Green (#10B981)
- Attention: Purple (#8B5CF6)
- Prediction: Orange (#F97316)
- Cache: Gold (#FBBF24)
- Background: Dark gradient (#0F172A to #1E293B)
- Text: White and light gray

4 Stages (top to bottom):

[Stage 1 - Tokenization] 🔵
图标：文本→数字
输入："May the force"
输出：[7108, 262, 3081]
关键："确定性查找"

[Stage 2 - Embeddings] 🟢
图标：数字→向量
输出：3×3072 矩阵
关键："相同 token+ 位置=相同状态"

[Stage 3 - Attention] 🟣
图标：Q/K/V 图书馆类比
可视化：因果掩码矩阵
关键："后期 token 无法改变前缀"

[Stage 4 - Prediction] 🟠
图标：logits→probs→token
输出："be"
关键："温度不影响缓存"

Cache Mechanism (bottom):

[KV Cache] 💰
图标：存储 K 和 V
收益：
- 输入成本↓90%
- 延迟↓80%
- 缓存读取 0.1x 价格

实用规则：
✅ 稳定内容放前面
✅ 可变内容放末尾
✅ 追加式更新
✅ 固定 JSON 顺序

成果徽章：
"10x 成本降低"
"80% 延迟降低"
"前缀形状缓存"

行动号召：
"探索完整机制"
"完整文章 →"

Style:
- 现代技术信息图
- 暗黑模式配霓虹阶段
- 清晰流水线可视化
- 专业 AI 工程美学

Technical:
- Aspect ratio: 9:16 portrait (1080x1920)
- Resolution: Ultra HD
- Style: 四层流水线信息图，暗黑模式
- Mobile/social media optimized

Output: 1 image, 9:16 vertical, Prompt Caching 4-stage pipeline with cache mechanism, dark mode with colorful stages.
```

**适用场景**: 小红书、抖音、技术社区、GitHub

---

### 选项 2：缓存命中对比风格

```prompt
Create a vertical before/after comparison "Without Cache vs With Cache".

Title: "Prompt Caching 对比"
Subtitle: "90% 成本如何节省"
Credit: "lossfn.com"

Layout: Split comparison - left (without) vs right (with).

Color Palette:
- Without: Red/gray (#EF4444)
- With: Green/gold (#10B981)
- Background: Dark gradient
- Text: White

Without Cache (Left - Red):

标题：❌ 无缓存

问题：
每次请求重新计算 2000 token 前缀

可视化：
请求 1: [████████████] 全计算
请求 2: [████████████] 全计算
请求 3: [████████████] 全计算
请求 4: [████████████] 全计算

浪费：
- 重复工作 100%
- 成本 100%
- 延迟 100%

With Cache (Right - Green):

标题：✅ 有缓存

方案：
第一次计算，后续复用

可视化：
请求 1: [████████████] 计算 + 缓存
请求 2: [░░░░░░████] 复用 + 新计算
请求 3: [░░░░░░████] 复用 + 新计算
请求 4: [░░░░░░████] 复用 + 新计算

收益：
- 输入成本↓90%
- 延迟↓80%
- 缓存读取 0.1x 价格

底部对比：

成本对比：
无缓存：$10/百万 token
有缓存：$1/百万 token

延迟对比：
无缓存：2000ms
有缓存：400ms

行动号召：
"探索缓存机制"
"完整文章 →"

Style:
- 清晰前后对比
- 左红右绿
- 问题→解决方案视觉
- 专业开发者工具美学

Technical:
- Aspect ratio: 9:16 portrait (1080x1920)
- Resolution: Ultra HD
- Style: 缓存对比图，暗黑模式
- Mobile/social media optimized

Output: 1 image, 9:16 vertical, Without Cache vs With Cache comparison, dark mode with red/green contrast.
```

**适用场景**: 成本优化说明、技术对比、工程分享

---

### 选项 3：因果掩码可视化风格

```prompt
Create a vertical attention mask diagram "Causal Attention — Why Caching Works".

Title: "因果注意力"
Subtitle: "为什么缓存有效"
Credit: "Transformer Explainer"

Layout: Vertical matrix showing attention mask growth.

Color Palette:
- Visible: Green (#10B981)
- Masked: Red (#EF4444)
- New token: Blue (#3B82F6)
- Background: Dark gradient
- Text: White

Attention Matrix (top):

标题：因果掩码规则

矩阵可视化（3 token）：
```
        May   the   force
May     ✓     ✗     ✗
the     ✓     ✓     ✗
force   ✓     ✓     ✓
```

图例：
✓ = 可见（绿色）
✗ = 掩码（红色）

规则：
"Token 只能向左看"
"早期行不依赖后期"

Growth Animation (middle):

标题：追加 "be" 时

旧状态（3 token）：
```
May   the   force   be
May    ✓     ✗     ✗     ✗
the    ✓     ✓     ✗     ✗
force  ✓     ✓     ✓     ✗
```

新状态（4 token）：
```
May    ✓     ✗     ✗     ✗    ← 不变
the    ✓     ✓     ✗     ✗    ← 不变
force  ✓     ✓     ✓     ✗    ← 不变
be     ✓     ✓     ✓     ✓    ← 新计算
```

关键洞察：
"前三行不变"
"只计算新行"
"缓存复用旧状态"

Bottom Section:

缓存原理：
✅ Token 化确定性
✅ 嵌入 + 位置=固定状态
✅ 因果注意力=前缀不变
✅ 存储 K/V 复用

实用规则：
"稳定内容放前面"
"可变内容放末尾"

行动号召：
"探索完整机制"
"完整文章 →"

Style:
- 清晰矩阵可视化
- 暗黑模式配彩色掩码
- 专业技术架构美学

Technical:
- Aspect ratio: 9:16 portrait (1080x1920)
- Resolution: Ultra HD
- Style: 因果注意力矩阵图，暗黑模式
- Mobile/social media optimized

Output: 1 image, 9:16 vertical, causal attention mask matrix showing why caching works, dark mode with green/red mask.
```

**适用场景**: 技术深度分享、原理说明、教学材料

---

## 🔧 实施检查清单

### 对 AI 应用开发者

- [ ] 系统提示放最前
- [ ] 用户输入放最后
- [ ] 固定工具 schema 顺序
- [ ] JSON 键顺序稳定
- [ ] 对话追加式更新
- [ ] 监控缓存命中率
- [ ] 使用 `cache_control`（如支持）

### 对 OpenClaw 用户

- [ ] 合并 SOUL.md + USER.md + TOOLS.md 为固定前缀
- [ ] 记忆文件追加式更新
- [ ] 避免重写早期会话记录
- [ ] 选择支持缓存的模型

---

*分析完成 | 下一步：询问用户是否需要改编为多平台内容*
