# 📱 小红书笔记：AI Agent 工程化最佳实践

---

## 📊 内容元数据

| 字段 | 值 |
|------|------|
| **内容 ID** | xhs-20260305-001 |
| **创建时间** | 2026-03-05 |
| **平台** | 小红书 |
| **类型** | 图文笔记 |
| **状态** | 待发布 |
| **来源** | X @systematicls |
| **原文链接** | https://x.com/systematicls/status/2028814227004395561 |

---

## 🎨 封面文案

**主标题**：用了 3 个月 AI Agent，我悟了
**副标题**：99% 的人都在过度配置｜7 条核心原则

**视觉建议**：
- 左侧：杂乱的配置截图 (CLAUDE.md 26000 行、各种插件图标)
- 右侧：简洁的 CLI 界面
- 中间：大箭头 + "Less is More"

---

## ✍️ 标题 (选 1 个)

1. **3 个月 AI Agent 实战｜从过度配置到极简工作流**
2. **AI Agent 工程化避坑指南｜这 7 条原则让我效率翻倍**
3. **别再装插件了｜世界级 Agent 工程师的极简心法**

---

## 📝 正文内容

### 😫 痛点开场

你是不是也这样？
- CLAUDE.md 写了 26000 行，Agent 还是听不懂人话
- 装了各种 harness、插件、技能包，越用越乱
- 看别人用 Agent 造火箭，自己连两块石头都堆不起来

**真相是：你的 enthusiasm 正在害你** 📉

---

### 💡 7 条核心原则 (亲测有效)

#### 1️⃣ Less is More
> "不需要最新 harness，不需要百万插件，不需要读百万文章"

- 基础 CLI (Claude Code / Codex) 就够了
- 真正有用的功能，官方会吸收进产品
- 前沿公司员工才是最大用户——他们用原生 CLI

**行动**：卸载多余插件，更新 CLI 到最新版 ✅

---

#### 2️⃣ Context Is Everything
> "上下文膨胀是最大敌人"

❌ 错误：给 Agent 塞 26000 行配置 + 历史记忆
✅ 正确：只给完成任务所需的最少信息

**技巧**：分离研究任务和实现任务
- 先让 Agent A 调研方案
- 再让 Agent B (fresh context) 实现

---

#### 3️⃣ 精准提示词设计
> "Agent 想取悦你，所以会硬造答案"

❌ "找个 bug" → Agent 会 engineering 一个 bug
✅ "遍历代码逻辑，报告所有发现" → 中性提示词

**高级玩法**：多 Agent 对抗机制
- Agent A (发现者): +1 分/小 bug, +10 分/致命 bug
- Agent B (反驳者): disproves 一个 bug 得该 bug 分数
- Agent C (裁判): 评分，准确率决定输赢

---

#### 4️⃣ 定义任务结束条件
> "Agent 知道如何开始，但不知道如何结束"

**解决方案**：
- ✅ 测试通过 (X 个测试全部 pass)
- ✅ 截图验证 (设计/行为符合预期)
- ✅ 创建 `{TASK}_CONTRACT.md` 明确验收标准

**Pro Tip**：用 stophook 防止 Agent 提前结束 session

---

#### 5️⃣ 别用 24 小时长运行
> "长 session = 上下文膨胀 = 性能下降"

❌ 一个 session 跑 24 小时
✅ 每个合同一个新 session，编排层管理

**效果**：性能提升 10 倍 +，漂移问题消失

---

#### 6️⃣ Rules + Skills 构建偏好
> "CLAUDE.md 应该是目录，不是百科全书"

**CLAUDE.md 结构**：
```
如果 coding → 读 coding-rules.md
如果 writing tests → 读 coding-test-rules.md
如果 tests failing → 读 coding-test-failing-rules.md
```

**定期清理**：让 Agent 整理合并规则，删除矛盾

---

#### 7️⃣ Own The Outcome
> "Agent 不完美，人需要对结果负责"

- 可以 delegate 设计和实现
- 但最终验收必须人来把关
- Keep it simple, stay mindful

---

### 🎁 资源包

**推荐工具**：
- Claude Code (官方 CLI)
- Codex CLI (OpenAI 官方)

**必读文档**：
- CLAUDE.md 最佳实践
- Skills 编写指南

**我的配置**：
- CLAUDE.md: ~200 行 (只有 IF-ELSE 目录)
- Rules: 12 条 (按场景分类)
- Skills: 8 个 (常用任务模板)

---

### 💬 互动引导

**问题**：你的 CLAUDE.md 写了多少行？评论区聊聊 👇

**收藏**：这篇值得反复看，建议⭐️收藏

**关注**：更多 AI Agent 实战干货，下期讲《如何用多 Agent 工厂自动化开发》

---

## 🏷️ 标签

#AIAgent #ClaudeCode #AI 工程化 #程序员成长 #AI 副业 #效率工具 #AI 开发 #大模型应用 #自动化 #干货分享

---

## 📊 预期数据

| 指标 | 目标 |
|------|------|
| 点击率 | >15% |
| 收藏率 | >20% |
| 互动率 | >10% |

---

## 🔗 相关链接

- **Notion 笔记**: https://www.notion.so/AI-Agent-7-31a49e5eec0f813c87fac6d14b4fe6b7
- **GitHub 备份**: https://github.com/wsj0415/openclaw-backup/blob/main/matrix/output/xiaohongshu_agent_engineering.md
- **原始 X 内容**: https://x.com/systematicls/status/2028814227004395561

---

## 🎨 封面图提示词 (Nano Banana Pro)

```
A split-screen social media cover image, vertical 4:5 aspect ratio:

LEFT SIDE - CHAOS:
Messy developer workspace, tangled cables everywhere,
100+ browser tabs on multiple monitors, stacks of documentation 
papers flying around, stressed person with head in hands, 
dark red and orange color scheme, sense of chaos and anxiety

RIGHT SIDE - ZEN:
Clean minimalist desk setup, single sleek laptop showing 
simple terminal CLI interface, calm focused atmosphere, 
soft blue and white lighting, zen-like simplicity, 
one coffee cup, small plant, maximum negative space

CENTER: Bold white arrow pointing from left to right,
"LESS IS MORE" text overlay in modern sans-serif font

STYLE:
Professional tech illustration, high contrast, 
social media optimized, vibrant colors, clean composition, 
8k resolution

--ar 4:5 --style raw --q 2
```

---

*内容来源：X @systematicls《How To Be A World-Class Agentic Engineer》*
*改编：KilroyContentBot | 2026-03-05*
*同步到 kilroy-cdn: 2026-03-05*
