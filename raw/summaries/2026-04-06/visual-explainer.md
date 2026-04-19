# Visual Explainer — 终结编码代理中的 ASCII 艺术图表

> **项目作者：** Nico Bailon (@nicobailon)  
> **翻译时间：** 2026-04-06  
> **项目链接：** https://github.com/nicobailon/visual-explainer  
> **GitHub Stars：** 4.4K  
> **许可证：** MIT  
> **推文来源：** @aiwithjainam

---

## 📊 项目概览

| 指标 | 数值 |
|------|------|
| **GitHub Stars** | 4.4K |
| **许可证** | MIT |
| **开源状态** | 100% 开源 |
| **定位** | 代理技能，生成富 HTML 页面/幻灯片 |
| **支持代理** | Claude Code / Pi / OpenAI Codex |

---

## 🎯 核心问题

**每个编码代理默认使用 ASCII 艺术当你要求图表时：**

```
框线字符 + 等宽对齐技巧 + 文本箭头
```

**问题：**
- ❌ 适用于简单情况（3 框流程图）
- ❌ 超出简单情况 → 变成不可读混乱
- ❌ 表格更糟：15 个需求对比计划 → 管道和破折号墙
- ❌ 数据在那里但阅读痛苦

**终端输出示例：**
```
┌─────────────┐    ┌─────────────┐
│   User      │───>│   Auth      │
└─────────────┘    └─────────────┘
      │                   │
      ▼                   ▼
┌─────────────┐    ┌─────────────┐
│   Login     │<───│   Token     │
└─────────────┘    └─────────────┘
```
（在终端中换行、断裂、不可读）

---

## 💡 解决方案

**Visual Explainer 技能：**
- ✅ 真实排版
- ✅ 深色/浅色主题
- ✅ 交互式 Mermaid 图表（缩放 + 平移）
- ✅ 杂志质量幻灯片
- ✅ 针对真实代码事实检查
- ✅ 无需构建步骤，仅需浏览器

**输出：**
```
自包含 HTML 页面 → 在浏览器中打开
```

---

## 🚀 安装方式

### 方式 1：Claude Code（市场）

```bash
# 添加到市场
/plugin marketplace add nicobailon/visual-explainer

# 安装
/plugin install visual-explainer@visual-explainer-marketplace
```

**注意：** Claude Code 插件命名空间命令为 `/visual-explainer:command-name`

---

### 方式 2：Pi

```bash
# 一键安装
curl -fsSL https://raw.githubusercontent.com/nicobailon/visual-explainer/main/install-pi.sh | bash

# 或克隆运行
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git
cd visual-explainer && ./install-pi.sh
```

---

### 方式 3：OpenAI Codex

```bash
# 克隆到临时目录
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git /tmp/visual-explainer

# 安装技能
cp -r /tmp/visual-explainer/plugins/visual-explainer ~/.agents/skills/visual-explainer

# 可选：安装斜杠命令（已弃用但仍可用）
mkdir -p ~/.codex/prompts
cp /tmp/visual-explainer/plugins/visual-explainer/commands/*.md ~/.codex/prompts/

rm -rf /tmp/visual-explainer
```

**使用：** `$visual-explainer` 或让 Codex 隐式激活

**安装提示后：** `/prompts:diff-review`、`/prompts:plan-review` 等

---

## 📋 可用命令

| 命令 | 功能 |
|------|------|
| **/generate-web-diagram** | 为任何主题生成 HTML 图表 |
| **/generate-visual-plan** | 为功能或扩展生成视觉实施计划 |
| **/generate-slides** | 生成杂志质量幻灯片 |
| **/diff-review** | 视觉 diff 审查 + 架构比较 + 代码审查 |
| **/plan-review** | 对比代码库中的计划 + 风险评估 |
| **/project-recap** | 心智模型快照（用于切换回项目） |
| **/fact-check** | 针对实际代码验证文档准确性 |
| **/share** | 部署 HTML 页面到 Vercel 获取实时 URL |

---

## 🎬 自动触发

**代理自动触发 HTML 渲染当：**
- 即将在终端倾倒复杂表格时
- 条件：4+ 行 或 3+ 列
- 结果：渲染 HTML 而非 ASCII

---

## 📊 幻灯片模式

**任何产生可滚动页面的命令支持 `--slides` 生成幻灯片：**

```bash
# Diff 审查幻灯片
/diff-review --slides

# 项目回顾幻灯片（2 周）
/project-recap --slides 2w
```

**输出：** 杂志质量幻灯片，带过渡和预设

---

## 📁 项目结构

```
.claude-plugin/
├── plugin.json              ← 市场身份
└── marketplace.json         ← 插件目录

plugins/
└── visual-explainer/
    ├── .claude-plugin/
    │   └── plugin.json      ← 插件清单
    ├── SKILL.md             ← 工作流 + 设计原则
    ├── commands/            ← 斜杠命令
    ├── references/          ← 代理生成前读取
    │   ├── css-patterns.md  （布局、动画、主题）
    │   ├── libraries.md     （Mermaid、Chart.js、字体）
    │   ├── responsive-nav.md（多部分页面粘性 TOC）
    │   └── slide-patterns.md（幻灯片引擎、过渡、预设）
    ├── templates/           ← 带不同调色板的参考模板
    │   ├── architecture.html
    │   ├── mermaid-flowchart.html
    │   ├── data-table.html
    │   └── slide-deck.html
    └── scripts/
        └── share.sh         ← 部署 HTML 到 Vercel 分享

输出：~/.agent/diagrams/filename.html → 在浏览器中打开
```

---

## 🎨 渲染引擎

**技能自动路由到正确方法：**

| 内容类型 | 渲染引擎 | 用途 |
|----------|----------|------|
| **流程图/图表** | Mermaid | 系统架构、认证流 |
| **架构概览** | CSS Grid | 多组件系统 |
| **数据表** | HTML 表格 | 需求对比、功能矩阵 |
| **仪表板** | Chart.js | 数据可视化、指标 |

---

## 💡 核心洞察

### 洞察 1：ASCII 艺术的局限

**问题场景：**
```
3 框流程图 → ASCII 可行
10+ 框架构图 → ASCII 不可读
15 行数据表 → ASCII 痛苦
```

**Visual Explainer 解决：**
- ✅ 真实排版（非等宽 hack）
- ✅ 交互式（缩放 + 平移）
- ✅ 主题支持（深色/浅色）
- ✅ 可分享（Vercel 部署）

---

### 洞察 2：自动触发智能

**智能检测：**
```
if (表格行数 >= 4 || 列数 >= 3) {
    渲染 HTML 而非 ASCII
}
```

**好处：**
- ✅ 无需用户思考
- ✅ 一致体验
- ✅ 渐进增强

---

### 洞察 3：幻灯片模式

**任何命令 + `--slides` = 幻灯片：**

```bash
# 从 diff 审查生成幻灯片
/diff-review --slides

# 从项目回顾生成幻灯片
/project-recap --slides 2w
```

**输出：** 杂志质量幻灯片，带过渡和预设

---

## ⚠️ 已知限制

| 限制 | 说明 | 变通方法 |
|------|------|----------|
| **需要浏览器查看** | 输出是 HTML 文件 | 自动在浏览器中打开 |
| **切换 OS 主题** | Mermaid SVG 需要刷新页面 | 刷新一次 |
| **模型能力差异** | 结果因模型而异 | 使用更强模型获得更好结果 |

---

## 🔗 灵感来源

**借鉴思想来自：**
- [Anthropic 的 frontend-design 技能](https://github.com/anthropics/skills)
- [interface-design](https://github.com/Dammyjay93/interface-design)

---

## 📄 许可证

**MIT License** - 完全开源，可自由使用和修改。

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/nicobailon/visual-explainer |
| **推文来源** | https://x.com/aiwithjainam/status/2041092240752464180 |
| **Anthropic Skills** | https://github.com/anthropics/skills |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-06 |
| **项目作者** | Nico Bailon |
| **项目平台** | GitHub |
| **翻译状态** | ✅ 完整翻译 + 使用指南 |

---

*翻译完成时间：2026-04-06 | 版本：v1.0*
