# Cocoon-AI/architecture-diagram-generator 仓库分析报告

**分析日期**: 2026-04-14  
**来源**: https://github.com/Cocoon-AI/architecture-diagram-generator

---

## 📋 一句话总结

这是一个专为 Claude AI 设计的技能工具，能够根据文字描述自动生成精美的深色主题系统架构图，输出为独立的 HTML/SVG 文件，无需任何设计技能即可创建专业的技术架构图。

---

## 🏷️ 话题标签

`#ClaudeAI` `#ArchitectureDiagram` `#SystemDesign` `#DeveloperTools` `#AIAutomation` `#TechVisualization` `#CLASkills` `#SVGGraphics` `#WebDevelopment` `#DarkTheme`

---

## 📖 仓库功能和用途

### 核心价值
- **零设计门槛**: 只需用英文描述你的系统架构，AI 就能生成专业级别的架构图
- **快速迭代**: 通过对话让 Claude 实时修改、调整布局、更新样式
- **易于分享**: 输出是单个 HTML 文件，可在任何浏览器打开，无需特殊软件

### 适用场景
1. **Web 应用架构**: React 前端 + Node.js API + PostgreSQL + Redis
2. **AWS 无服务器架构**: CloudFront + API Gateway + Lambda + DynamoDB + S3
3. **微服务系统**: 多语言服务 + 多数据库 + Kafka + Kubernetes

### 输出特性
- 深色主题 (Slate-950 背景 + 微妙网格图案)
- 语义化颜色编码 (前端 - 青色、后端 - 翡翠绿、数据库 - 紫色、云/AWS-琥珀色、安全 - 玫瑰色)
- 自包含 HTML 文件 (嵌入式 CSS + 内联 SVG)
- 无依赖 (任何现代浏览器均可打开)
- 专业排版 (JetBrains Mono 字体)
- 智能分层 (箭头在组件框下方渲染)

---

## 🛠️ 核心技术栈和依赖

| 技术 | 用途 | 版本/说明 |
|------|------|-----------|
| **Claude AI Skills** | AI 技能框架 | 需要 Claude Pro/Max/Team/Enterprise |
| **HTML5** | 输出格式 | 独立 HTML 文件 |
| **CSS3** | 样式系统 | 嵌入式，深色主题设计系统 |
| **SVG** | 图形渲染 | 内联 SVG，响应式 viewBox |
| **Google Fonts** | 字体加载 | JetBrains Mono |
| **JavaScript** | 无运行时依赖 | 纯静态 HTML |

### 设计系统颜色规范

| 组件类型 | 颜色 | 用途 |
|----------|------|------|
| Frontend | Cyan (#06b6d4) | 客户端应用、UI、边缘设备 |
| Backend | Emerald (#10b981) | 服务器、API、服务 |
| Database | Violet (#8b5cf6) | 数据库、存储、AI/ML |
| Cloud/AWS | Amber (#f59e0b) | 云服务、基础设施 |
| Security | Rose (#f43f5e) | 认证、安全组、加密 |
| External | Slate (#64748b) | 通用、外部系统 |

---

## 📦 安装和使用方法

### 前置要求
⚠️ **需要 Claude Pro、Max、Team 或 Enterprise 计划**

### 安装步骤

#### 方法 1: 通过 Claude.ai 界面
1. 下载 `architecture-diagram.zip`
2. 访问 [claude.ai](https://claude.ai)
3. 进入 Settings → Capabilities → Skills
4. 点击 + Add 并上传 zip 文件
5. 开启技能开关

#### 方法 2: 命令行安装
```bash
# 全局技能
unzip architecture-diagram.zip -d ~/.claude/skills/

# 或项目本地
unzip architecture-diagram.zip -d ./.claude/skills/
```

### 使用方法

#### 步骤 1: 准备架构描述
有三种方式获取架构描述：

**选项 A: 让 AI 分析代码库**
```
分析这个代码库并描述架构。包括所有主要组件、
它们如何连接、使用什么技术，以及任何云服务或集成。
格式化为架构图列表。
```

**选项 B: 自己编写**
```
- React 前端与 Node.js API 通信
- PostgreSQL 数据库
- Redis 缓存
- 托管在 AWS 上，使用 CloudFront CDN
```

**选项 C: 询问典型架构**
```
SaaS 应用的典型架构是什么？
```

#### 步骤 2: 在 Claude 中生成
```
使用你的架构图技能，根据以下描述创建架构图：

[粘贴你的架构描述]
```

#### 步骤 3: 迭代优化
通过对话让 Claude 修改：
- "请更新 XYZ 组件"
- "添加一个负载均衡器"
- "改变布局为水平排列"
- "修复箭头连接问题"

### 输出文件结构
```html
<!DOCTYPE html>
<html>
  <head>
    <!-- 嵌入式样式，Google Fonts -->
  </head>
  <body>
    <div class="container">
      <div class="header"><!-- 标题 --></div>
      <div class="diagram-container">
        <svg><!-- 架构图 --></svg>
      </div>
      <div class="cards"><!-- 摘要卡片 --></div>
      <p class="footer"><!-- 元数据 --></p>
    </div>
  </body>
</html>
```

### 输出用途
- 直接在浏览器中打开
- 与团队成员分享 (直接发送文件)
- 包含在文档中
- 打印或导出为 PDF
- 托管在任何静态网站上

---

## 🎨 封面图提示词推荐 (来自 nano-banana-pro)

基于仓库的技术可视化特性，推荐以下提示词用于生成封面图：

### 推荐 1: Technical Blueprint Drawing
**适用场景**: 技术感强的封面，展现系统架构的精密性

```
Iphone, technical blueprint drawing, orthographic view, front view + side view + top view, 
white vector line art, thin construction lines, precise measurements, annotation labels, 
dimension arrows, grid background, deep blue background, minimal design, engineering 
schematic style, high detail
```

### 推荐 2: Technical Infographic Cutaway
**适用场景**: 展示系统内部结构的剖面图风格

```
Create a high-resolution professional infographic of [SYSTEM NAME].
Display the object in a clean, semi-realistic technical illustration style. 
Include both external structure and internal components using a cutaway view, 
cross-section, or exploded layout where appropriate.
Automatically detect and label all major structural, mechanical, electronic, 
or functional components using accurate technical terminology.
```

### 推荐 3: Exploded View Infographic Diagram
**适用场景**: 爆炸视图，展示组件关系

```
product design, [SYSTEM COMPONENT], exploded view diagram, white background, 
three-dimensional, highly detailed internal components, studio lighting, 
product photography, best quality
```

---

## 📊 仓库元数据

| 项目 | 值 |
|------|-----|
| 仓库名称 | architecture-diagram-generator |
| 组织 | Cocoon-AI |
| 版本 | 1.0 |
| 许可证 | MIT |
| 主要用途 | Claude AI Skill for Architecture Diagrams |
| 输出格式 | HTML/SVG |
| 设计主题 | Dark Theme (Slate-950) |

---

## 💡 使用建议

### 最佳实践
1. **描述要具体**: 包含所有主要组件、连接方式、技术栈
2. **迭代要耐心**: 通过多轮对话逐步完善图表
3. **保存多版本**: 每次重大修改后保存 HTML 文件
4. **颜色一致性**: 遵循设计系统的颜色编码规范

### 常见用例模板

**Web 应用**:
```
Create an architecture diagram for a web application with:
- React frontend
- Node.js/Express API
- PostgreSQL database
- Redis cache
- JWT authentication
```

**AWS 无服务器**:
```
Create an architecture diagram showing:
- CloudFront CDN
- API Gateway
- Lambda functions (Node.js)
- DynamoDB
- S3 for static assets
- Cognito for auth
```

**微服务**:
```
Create an architecture diagram for a microservices system with:
- React web app and mobile clients
- Kong API Gateway
- User Service (Go), Order Service (Java), Product Service (Python)
- PostgreSQL, MongoDB, and Elasticsearch databases
- Kafka for event streaming
- Kubernetes orchestration
```

---

## 🔗 相关资源

- **官方安装指南**: https://support.claude.com/en/articles/12512180-using-skills-in-claude
- **Cocoon AI**: https://cocoon-ai.com
- **联系**: hello@cocoon-ai.com

---

## 📝 归档信息

- **归档路径**: `/root/.openclaw/agents/content/raw/articles/github-cocoon-ai-architecture-diagram-generator-2026-04-14.md`
- **归档时间**: 2026-04-14T04:52 UTC
- **分析工具**: OpenClaw Agent (李四)
- **GitHub 归档**: 待推送

---

*本报告由 Kilroy 内容运营专员 李四 自动生成 | v1.0*
