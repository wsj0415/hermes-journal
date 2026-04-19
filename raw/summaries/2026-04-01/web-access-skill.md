# Web-Access Skill — 给 Claude Code 装上完整联网能力

> **项目作者：** 一泽 Eze (@eze-is)  
> **翻译时间：** 2026-04-01  
> **项目链接：** https://github.com/eze-is/web-access  
> **详细介绍：** https://mp.weixin.qq.com/s/rps5YVB6TchT9npAaIWKCw

---

## 🎯 项目概述

**给 Claude Code 装上完整联网能力的 skill。**

Claude Code 原本有 WebSearch、WebFetch，但缺少调度策略和浏览器自动化能力。这个 skill 补上的是：**联网策略 + CDP 浏览器操作 + 站点经验积累**。

---

## 📊 核心能力

| 能力 | 说明 |
|------|------|
| **联网工具自动选择** | WebSearch / WebFetch / curl / Jina / CDP，按场景自主判断，可任意组合 |
| **CDP Proxy 浏览器操作** | 直连用户日常 Chrome，天然携带登录态，支持动态页面、交互操作、视频截帧 |
| **三种点击方式** | /click（JS click）、/clickAt（CDP 真实鼠标事件）、/setFiles（文件上传） |
| **并行分治** | 多目标时分发子 Agent 并行执行，共享一个 Proxy，tab 级隔离 |
| **站点经验积累** | 按域名存储操作经验（URL 模式、平台特征、已知陷阱），跨 session 复用 |
| **媒体提取** | 从 DOM 直取图片/视频 URL，或对视频任意时间点截帧分析 |

---

## 📋 版本更新

### v2.4.1 更新（跨平台支持）

- ✅ **跨平台支持** — 脚本从 bash 迁移到 Node.js，Windows / Linux / macOS 均可使用
- ✅ **DOM 边界穿透** — 新增技术事实：eval 递归遍历可穿透 Shadow DOM、iframe 等选择器不可跨越的边界

### v2.4 更新

- ✅ **站点内 URL 可靠性** — 新增事实说明：站点生成的链接自带完整上下文，手动构造的 URL 可能缺失隐式必要参数
- ✅ **平台错误提示不可信** — 新增技术事实：平台返回的"内容不存在"等提示可能是访问方式问题而非内容本身问题
- ✅ **小红书站点经验增强** — xsec_token 机制、创作者平台状态校验、暂存草稿流程

### v2.3 更新

- ✅ **浏览哲学重构** — 更清晰的「像人一样思考」框架，强调目标驱动而非步骤驱动
- ✅ **Jina 积极推荐** — 明确鼓励在合适场景主动使用 Jina 节省 token
- ✅ **子 Agent prompt 指引优化** — 明确加载写法，增加避免动词暗示执行方式的说明

---

## 🛠️ 安装方式

### 方式一：让 Claude 自动安装 ⭐ 推荐

```text
帮我安装这个 skill：https://github.com/eze-is/web-access
```

---

### 方式二：Plugin 安装

```bash
# 添加到 plugin marketplace
claude plugin marketplace add https://github.com/eze-is/web-access

# 安装
claude plugin install web-access@web-access --scope user
```

---

### 方式三：手动安装

```bash
git clone https://github.com/eze-is/web-access ~/.claude/skills/web-access
```

---

## ⚙️ CDP 模式配置

### 系统要求

| 要求 | 说明 |
|------|------|
| **Node.js** | 22+ |
| **Chrome** | 开启远程调试 |
| **平台** | Windows / Linux / macOS（v2.4.1+） |

---

### Chrome 配置

1. **Chrome 地址栏打开：**
   ```
   chrome://inspect/#remote-debugging
   ```

2. **勾选：**
   ```
   ☑ Allow remote debugging for this browser instance
   ```
   （可能需要重启浏览器）

---

### 环境检查

```bash
# Agent 运行时会自动完成前置检查，无需手动执行
node "$CLAUDE_SKILL_DIR/scripts/check-deps.mjs"

# $CLAUDE_SKILL_DIR 是 skill 加载时自动设置的环境变量
# 手动运行请替换为实际路径，如 ~/.claude/skills/web-access
```

---

## 🌐 CDP Proxy API

Proxy 通过 WebSocket 直连 Chrome（兼容 chrome://inspect 方式，无需命令行参数启动），提供 HTTP API：

### 启动 Proxy

```bash
# Agent 会自动管理 Proxy 生命周期，无需手动启动
node "$CLAUDE_SKILL_DIR/scripts/cdp-proxy.mjs" &
```

---

### API 端点

| 端点 | 方法 | 说明 | 示例 |
|------|------|------|------|
| **/new** | GET | 新建 tab | `curl -s "http://localhost:3456/new?url=https://example.com"` |
| **/eval** | POST | 执行 JS | `curl -s -X POST "http://localhost:3456/eval?target=ID" -d 'document.title'` |
| **/click** | POST | JS 点击 | `curl -s -X POST "http://localhost:3456/click?target=ID" -d 'button.submit'` |
| **/clickAt** | POST | 真实鼠标点击 | `curl -s -X POST "http://localhost:3456/clickAt?target=ID" -d '.upload-btn'` |
| **/setFiles** | POST | 文件上传 | `curl -s -X POST "http://localhost:3456/setFiles?target=ID" -d '{"selector":"input[type=file]","files":["/path/to/file.png"]}'` |
| **/screenshot** | GET | 截图 | `curl -s "http://localhost:3456/screenshot?target=ID&file=/tmp/shot.png"` |
| **/scroll** | GET | 滚动 | `curl -s "http://localhost:3456/scroll?target=ID&direction=bottom"` |
| **/close** | GET | 关闭 tab | `curl -s "http://localhost:3456/close?target=ID"` |

---

## 📝 使用示例

安装后直接让 Agent 执行联网任务，skill 自动接管：

```text
# 搜索任务
"帮我搜索 xxx 最新进展"

# 页面读取
"读一下这个页面：[URL]"

# 社交媒体
"去小红书搜索 xxx 的账号"

# 内容发布
"帮我在创作者平台发一篇图文"

# 并行调研
"同时调研这 5 个产品的官网，给我对比摘要"
```

---

## 🧠 浏览哲学

**Skill = 哲学 + 技术事实，不是操作手册。** 讲清 tradeoff 让 AI 自己选，不替它推理。

### 核心理念

1. **目标驱动而非步骤驱动** — 像人一样思考
2. **工具自主选择** — 按场景判断使用 WebSearch/WebFetch/curl/Jina/CDP
3. **经验积累复用** — 按域名存储操作经验，跨 session 使用
4. **并行分治** — 多目标时分发子 Agent 并行执行

### 技术事实

| 事实 | 说明 |
|------|------|
| **DOM 边界穿透** | eval 递归遍历可穿透 Shadow DOM、iframe 等选择器不可跨越的边界 |
| **站点内 URL 可靠性** | 站点生成的链接自带完整上下文，手动构造的 URL 可能缺失隐式必要参数 |
| **平台错误提示不可信** | 平台返回的"内容不存在"等提示可能是访问方式问题而非内容本身问题 |
| **Jina 节省 token** | 在合适场景主动使用 Jina 可节省大量 token |

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **项目仓库** | https://github.com/eze-is/web-access |
| **详细介绍** | https://mp.weixin.qq.com/s/rps5YVB6TchT9npAaIWKCw |
| **SKILL.md** | https://github.com/eze-is/web-access/blob/main/SKILL.md |
| **Star History** | https://star-history.com/#eze-is/web-access&Date |

---

## 📊 项目统计

![Star History](https://private-user-images.githubusercontent.com/53331888/567502979-2afa25c2-3730-413e-b40f-94e52567249d.png)

---

## 🎯 核心价值

### 解决的问题

| 问题 | Web-Access 解决方案 |
|------|-------------------|
| **缺少调度策略** | 联网工具自动选择，按场景判断 |
| **缺少浏览器自动化** | CDP Proxy 直连 Chrome，支持交互操作 |
| **无法携带登录态** | 使用用户日常 Chrome，天然携带 Cookie |
| **无法处理动态页面** | CDP 支持 JavaScript 渲染页面 |
| **无法跨 session 学习** | 站点经验积累，按域名存储复用 |
| **多目标效率低** | 并行分治，子 Agent 并行执行 |

---

## 💡 使用建议

### ✅ 推荐场景

1. **需要登录的网站** — 小红书、知乎、GitHub 等
2. **动态页面** — 单页应用、JavaScript 渲染内容
3. **交互操作** — 点击、填写表单、文件上传
4. **媒体提取** — 图片、视频 URL 提取、视频截帧
5. **多目标调研** — 并行分治，同时调研多个网站

### ❌ 不适用场景

1. **简单静态页面** — 使用 WebFetch 或 Jina 更节省
2. **纯文本搜索** — 使用 WebSearch 更快速
3. **无需交互的 API** — 直接使用 API 更高效

---

## 🔧 技术架构

```
┌─────────────────┐
│   Claude Code   │
│    (Agent)      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Web-Access     │
│     Skill       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ↓         ↓
┌────────┐ ┌──────────┐
│ Web    │ │   CDP    │
│Search  │ │  Proxy   │
│WebFetch│ │ (Chrome) │
│ curl   │ │          │
│ Jina   │ │          │
└────────┘ └──────────┘
```

---

## 📝 授权协议

**MIT License** · 作者：[一泽 Eze](https://github.com/eze-is)

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-01 |
| **项目作者** | 一泽 Eze (@eze-is) |
| **项目平台** | GitHub |
| **翻译状态** | ✅ 完整翻译 + 使用指南 |

---

*翻译完成时间：2026-04-01 | 版本：v1.0*
