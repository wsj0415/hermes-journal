# 10 个 Claude MCP 插件 — 让 Claude 变成 AI 操作系统

**来源**: https://x.com/suryanshti777/status/2041879621940211924  
**抓取时间**: 2026-04-09 14:28 UTC  
**类型**: X Article 长文  
**标签**: claude, mcp, ai-plugins, automation, ai-os

---

## 核心洞察

**一句话总结**: Claude + MCP 插件 = 从被动回答问题的聊天机器人 → 主动执行任务的自主 AI 工作者

**关键转变**:
- **Before**: Chat → Thinking（被动思考）
- **After**: Plugins → Actions（主动行动）

**大事件**: 2026 年 2 月 24 日，Anthropic 推出私有插件市场，社区发布 1000+ MCP 服务器

---

## 10 个关键插件

### 1. Feature-Dev — Claude 变成资深工程师
- **功能**: 完整工程流程（需求→分析→架构→实现→测试→审查→文档）
- **命令**: `/feature-dev build user onboarding`
- **输出**: 完整功能，不只是代码

### 2. Frontend-Design — 修复"AI 外观"
- **问题**: 通用间距、安全字体、可预测布局
- **解决**: 不对称布局、有意约束、字体层次、视觉差异化、动效思考
- **结果**: 别人以为你雇了设计师

### 3. Context7 — 无幻觉文档
- **问题**: 过时文档导致幻觉
- **解决**: 版本特定文档、实时 API 参考、精确框架行为
- **结果**: Claude 停止猜测，开始引用

### 4. GitHub MCP — Claude 读取代码库
- **功能**: 搜索仓库、读取文件、找 bug、写修复、开 PR
- **命令**: "分析 auth 系统并修复 issue #42"
- **结果**: 代码库原生 agent

### 5. PostgreSQL MCP — 自然语言数据查询
- **功能**: 无需 SQL，自然语言查询
- **命令**: "上个月按收入排名的顶级用户"
- **流程**: 检查 schema → 写 SQL → 执行 → 返回结果

### 6. Playwright MCP — Claude 控制浏览器
- **功能**: 打开 Chrome、导航网站、填写表单、提交支付、验证成功
- **命令**: "测试结账流程"
- **结果**: 自主测试应用

### 7. Brave Search — 实时互联网访问
- **功能**: 当前事件、最新发布、实时文档、事实核查
- **解决**: 知识截止问题
- **结果**: Claude 变成实时研究员

### 8. Google Workspace — Claude 运行你的工作
- **功能**: 读取 Gmail、更新 Sheets、创建 Docs、管理日历、搜索 Drive
- **命令**: "检查邮件、回复、更新指标、创建截止日期"
- **结果**: 一键完整工作流

### 9. Slack MCP — Claude 加入团队
- **功能**: 读取频道、总结线程、起草消息、发布更新
- **命令**: "总结过去 2 天"
- **结果**: 无消息过载

### 10. Memory Bank — Claude 记住一切
- **功能**: 持久记忆、项目上下文、编码标准、偏好、决策
- **解决**: LLM 遗忘问题
- **结果**: 从聊天机器人 → 长期 AI 协作者

---

## 🎨 封面图提示词（来自 nano-banana-pro 技能库）

### 选项 1：Bento Grid 信息图风格 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Input Variable: 10 Claude MCP Plugins
Language: Chinese

System Instruction:
Create an image of premium liquid glass Bento grid product infographic with 8 modules for "10 Claude MCP Plugins — AI Operating System".

1) Product Analysis:
→ Hero color: Purple (#8B5CF6) — AI/tech dominant
→ Category: TECH / AI Software

2) Color Palette (derived from hero):
→ Product + accents: Full saturation purple
→ Icons, borders: Muted purple (30-40% saturation, never black)
→ Additional: Blue (#3B82F6) for contrast

3) Visual Style:
→ Hero: Stylized Claude brain icon + plugin arms
→ Cards: Apple liquid glass (85-90% transparent)
→ Background: Ethereal abstract glow, dark gradient
→ Add subtle motion effect
→ Asymmetric Bento grid, 9:16 portrait
→ Hero card: 28-30% | Info modules: 70-72%

4) Module Content (8 Cards):

M1 — Hero:
"10 个 Claude 插件"
"从聊天机器人 → AI 操作系统"
Icon: Brain + plugin arms

M2 — Before/After:
Before ❌: "Chat → Thinking"
After ✅: "Plugins → Actions"

M3 — Top Plugins (3 cards):
Feature-Dev | Frontend-Design | Memory Bank
"Senior Engineer" | "Fixes AI Look" | "持久记忆"

M4 — Key Metrics:
"1000+ MCP Servers"
"351K+ Agent Skills"
"Millions of Installs"

M5 — Capabilities:
"执行代码" | "查询数据库"
"控制浏览器" | "读取 Slack"

M6 — Who It's For:
✅ Developers
✅ Data Analysts
✅ Content Creators
⚠️ Not for basic chat users

M7 — Quick Reference:
Chat → Thinking
Plugins → Actions
Memory → Context

M8 — Did You Know:
"2026-02-24 Launch"
"1000+ servers in 2 weeks"
"Gap is getting bigger"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

### 选项 2：爆炸视图风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11270 (Exploded View Infographic)  
**示例图**: https://cms-assets.youmind.com/media/1772519703684_klovml_HCbTfBgXQAAtlhh.jpg

```prompt
product design, Claude MCP Plugins Architecture, exploded view diagram, white background, three-dimensional, highly detailed showing Claude brain in center with 10 plugin arms radiating outward, studio lighting, product photography, best quality, aspect ratio 9:16

Center: Claude Brain icon with "MCP" label

10 Plugin Arms (环绕):
1. Feature-Dev — Code icon
2. Frontend-Design — Paint brush icon
3. Context7 — Document icon
4. GitHub — GitHub logo
5. PostgreSQL — Database icon
6. Playwright — Browser icon
7. Brave Search — Search icon
8. Google Workspace — G Suite icons
9. Slack — Slack logo
10. Memory Bank — Memory chip icon

Bottom Badge:
"1000+ MCP Servers"
"351K+ Agent Skills"
"AI Operating System"

Style: Clean technical illustration, minimal labels, professional educational infographic
```

---

## 新心智模型

| 组件 | 功能 |
|------|------|
| Chat | Thinking（思考） |
| Plugins | Actions（行动） |
| Memory | Context（上下文） |
| Browser | Execution（执行） |
| Database | Data（数据） |
| Workspace | Productivity（生产力） |
| GitHub | Building（构建） |
| Slack | Communication（沟通） |

**组合起来**: Claude 变成 AI 操作系统

---

## 完整工作流示例

```
1. 读取需求
2. 检查文档（Context7）
3. 编写代码（Feature-Dev）
4. 测试 UI（Frontend-Design + Playwright）
5. 查询数据库（PostgreSQL）
6. 更新表格（Google Workspace）
7. 通知团队（Slack）
8. 部署功能（GitHub）

全部在一个工作流中完成。
```

---

## 关键数据

| 指标 | 数值 |
|------|------|
| MCP 服务器 | 1000+ |
| Agent Skills | 351K+ |
| 安装量 | 数百万 |
| 官方连接器 | 数十个 |
| 发布日期 | 2026-02-24 |

---

## 人群分层

| 层级 | 行为 |
|------|------|
| 大多数用户 | 还在写提示 |
| 高级用户 | 构建工作流 |
| 超级用户 | 安装插件栈 |
| 最快团队 | 把 Claude 当基础设施运行 |

**差距正在快速扩大。**

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Claude 没有插件 = 智能助手" | 基础能力 |
| "Claude 有插件 = 自主工作者" | 完整能力 |
| "这不是提示，这是编排" | 新范式 |
| "差距正在快速扩大" | 紧迫性 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **MCP 架构** — 标准化连接协议
2. **插件思维** — 能力扩展而非提示优化
3. **Memory Bank** — 持久记忆解决遗忘
4. **工作流编排** — 多工具协同

### 可实施
- 评估 MCP for Obsidian 集成
- 添加 Memory Bank 到 wiki 系统
- 构建内容创作插件栈

---

*原始来源：https://x.com/suryanshti777/status/2041879621940211924*
