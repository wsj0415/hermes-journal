# 🐦 X 推文总结：OpenClaw Skill 精选指南

**日期**: 2026-03-06  
**来源**: X/Twitter  
**作者**: @vista8 (向阳乔木)  
**原文链接**: https://x.com/vista8/status/2029935446810308817  
**互动数据**: 👍 5 | 🔄 1 | 👁 488 | ⭐ 10  
**价值评估**: ⭐⭐⭐⭐⭐ 高价值技能清单

---

## 📋 核心摘要

**核心观点**: "龙虾 (OpenClaw) 越火，普通人更应该沉下心打磨 Skill。否则龙虾装了也没太大用处。"

**背景**: OpenClaw 火爆，云厂商一键部署、模型厂商推 Coding Plan、甚至出现免费上门安装服务。但作者提醒：**Skill 才是灵魂**，没有 Skill 的 OpenClaw 就像没装 App 的手机。

**内容**: 按「抓取采集」「内容创作」「效率工具」三条线推荐 9 个精选 Skill，附安装指南和资源平台。

---

## 🎯 核心洞察

> "与其追热点装龙虾，不如先想清楚：你让 AI 帮你干什么？这个问题想清楚了，Skill 自然就知道怎么写了。"

**三大类别**:
| 类别 | 数量 | 核心作用 |
|------|------|----------|
| 抓取采集 | 4 个 | 给 AI 装上眼睛，喂得进东西 |
| 内容创作 | 3 个 | 从生产到分发全流程 |
| 效率工具 | 2 个 | 音乐/设计等生活场景 |

---

## 📚 一、抓取采集 Skill (4 个)

### 1. Agent Reach —— 给 AI 装上眼睛 👁️

**仓库**: https://github.com/Panniantong/Agent-Reach

**一句话**: 零 API 成本，让 AI Agent 访问整个互联网

**支持平台**:
- 网页抓取
- YouTube 字幕提取
- Twitter/X 搜索
- GitHub 访问
- Reddit 解析
- B 站、小红书、抖音
- 微信公众号
- RSS 订阅
- 语义搜索

**亮点**:
| 特性 | 说明 |
|------|------|
| ✅ 零 API 成本 | 全部免费开源后端 |
| ✅ 本地存储 | cookie/token 不外传 |
| ✅ 中文支持 | 小红书/抖音/微信 |
| ✅ 诊断工具 | `agent-reach doctor` 一键排查 |

**安装**:
```bash
# 让 AI Agent 说
"帮我安装 Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md"
```

**前置条件**:
- Python
- yt-dlp
- gh CLI
- 中文平台需 Docker 运行 MCP 服务

---

### 2. Defuddle —— 网页正文提取神器 📄

**仓库**: https://github.com/joeseesun/defuddle-skill

**一句话**: 从网页提取干净文章内容，去除广告/侧边栏

**背景**: Obsidian CEO 写的命令行工具，封装为 Skill

**功能**:
- 提取 Markdown 正文
- 元数据：标题、作者、发布日期、字数
- 自动去除广告、侧边栏等杂乱元素

**使用示例**:
```
"帮我提取这个链接的文章内容"
```

**安装**:
```bash
npx skills add joeseesun/defuddle-skill
```

---

### 3. YouTube 搜索下载 📺

**仓库**: https://github.com/joeseesun/yt-search-download

**一句话**: YouTube 全站搜索 + 视频下载 + 字幕提取，一站搞定

**功能**:
| 功能 | 说明 |
|------|------|
| 🔍 搜索 | 按日期/播放量/相关性排序 |
| 📥 下载 | 多画质 (最高 4K) |
| 🎵 音频 | MP3 提取 |
| 📝 字幕 | SRT(带时间戳) + TXT(纯文本) |
| 🌐 翻译 | 英文标题自动翻译成中文 |
| 📺 频道 | 频道浏览及频道内搜索 |

**典型用法**:
1. 搜索某个主题的最新视频
2. 下载视频并提取字幕，用于内容创作
3. 只提取音频做播客素材

**安装**:
```bash
npx skills add joeseesun/yt-search-download
```

**前置条件**:
- 免费申请 YouTube API Key
- `brew install yt-dlp`
- ⚠️ 经常更新 yt-dlp，使用纯净度高的 IP

---

### 4. Anything to NotebookLM —— 万物皆可播客 🎙️

**仓库**: https://github.com/joeseesun/anything-to-notebooklm

**一句话**: 把任何内容扔进 Google NotebookLM，自动生成播客/PPT/思维导图

**整合项目**:
- NotebookLM-py (@tenglin)
- 微软 Markitdown
- 多个开源项目

**支持输入** (15+ 格式):
- 微信公众号文章
- YouTube 视频
- PDF/EPUB
- 网页
- Office 文档
- 图片/音频

**支持输出**:
- 🎙️ 播客
- 📊 PPT
- 🗺️ 思维导图
- 📝 测验
- 📋 报告
- 🎬 视频
- 📈 信息图

**使用示例**:
```
"把这篇微信文章变成播客"
```

**安装**:
```bash
git clone https://github.com/joeseesun/anything-to-notebooklm.git
cd anything-to-notebooklm
./install.sh
```

---

## ✍️ 二、内容创作 Skill (3 个)

### 5. 宝玉老师 Skill 合集 —— 内容工厂 🏭

**仓库**: https://github.com/jimliu/baoyu-skills

**一句话**: 一个人的内容工厂，从生产到分发全包

**作者**: 宝玉老师 (@dotey)

### 视觉内容生成

| Skill | 功能 |
|-------|------|
| **小红书信息图** | 多种风格 × 多种布局定制 |
| **通用信息图生成器** | 20 种布局 + 17 种视觉风格 |
| **封面图工具** | 5 维度设计系统 (类型/配色/渲染/纹理/排版) |
| **幻灯片创建器** | 14+ 风格预设 |
| **漫画生成** | 文章插图生成 |

### 社交媒体发布

| 平台 | 支持 |
|------|------|
| X (Twitter) | ✅ 自动发布 |
| 微信公众号 | ✅ 自动发布 |
| 小红书 | ✅ 自动发布 |

### 内容处理工具

- Markdown 格式化与转换
- 图片压缩 (WebP/PNG)
- DeepL 翻译
- URL 转 Markdown

**安装**:
```bash
npx skills add jimliu/baoyu-skills
```

**适用人群**: 做自媒体的朋友，一个 Skill 包解决全部需求

---

### 6. Markdown 一键发 X 长文 📝

**仓库**: https://github.com/joeseesun/qiaomu-x-article-publisher

**一句话**: 写好 Markdown，一键发布为 X (Twitter) Articles 草稿

**支持格式**:
- ✅ 标题
- ✅ 加粗/斜体
- ✅ 列表
- ✅ 引用
- ✅ 代码块
- ✅ 链接
- ✅ 图片

**亮点**:
- 自动处理图片上传
- 7 天免重复认证

**安装**:
```bash
git clone https://github.com/joeseesun/qiaomu-x-article-publisher.git ~/.claude/skills/qiaomu-x-article-publisher
pip install Pillow pyobjc-framework-Cocoa patchright
python auth_manager.py setup
```

---

### 7. Knowledge Site Creator —— 一句话生成学习网站 🌐

**仓库**: https://github.com/joeseesun/knowledge-site-creator

**一句话**: 告诉 AI 你想学什么，自动生成完整学习网站并部署上线

**使用示例**:
```
"帮我创建一个学习进化心理学的网站"
```

**自动完成**:
1. 主题分析
2. 内容创作
3. 页面设计
4. Vercel 部署

**学习模式**:
- 📇 闪卡
- 📈 渐进学习
- ❓ 测验
- 📑 索引
- 📊 进度追踪

**技术特点**:
| 特性 | 说明 |
|------|------|
| ✅ PWA 支持 | 离线也能用 |
| ✅ SEO 优化 | 自带 Meta 标签和站点地图 |
| ✅ 零依赖 | 原生 HTML/CSS/JS |
| ✅ 极简设计 | 干净清爽黄色主题 |

**安装**:
```bash
npx skills add joeseesun/knowledge-site-creator
```

---

## 🛠️ 三、效率工具 Skill (2 个)

### 8. Spotify 音乐播放器 🎵

**仓库**: https://github.com/joeseesun/qiaomu-music-player-spotify

**一句话**: 用自然语言控制 Spotify，内置 5947 种音乐风格数据库

**使用示例**:
```
"放点适合写代码的音乐"
"来首 Bohemian Rhapsody"
```

**功能**:
- 🔍 搜索
- ▶️ 播放/暂停/跳曲
- 🔊 音量调节
- 📋 队列管理
- 🎯 场景/情绪推荐

**亮点**:
| 特性 | 说明 |
|------|------|
| 🎼 5,947 种风格 | 分层组织音乐风格 |
| ⚡ 30+ 快捷播放 | 快速选择常用风格 |
| 🗣️ 自然语言 | 描述映射到具体风格 |
| 🔧 零外部依赖 | 纯 Python 标准库 |
| 🔄 自动刷新 | OAuth token 自动更新 |

**安装**:
```bash
npx skills add joeseesun/qiaomu-music-player-spotify
```

**前置条件**:
- Spotify Premium 账号 (淘宝约 150 元/年)

---

### 9. Design Advisor —— 乔布斯式设计顾问 🎨

**仓库**: https://github.com/joeseesun/qiaomu-design-advisor

**一句话**: 融合乔布斯产品直觉 + Rams 功能纯粹主义的 UI/UX 设计顾问

**设计理念**:
- 深入挖掘表面需求背后的真实用户需要
- 审视每个细节 (间距/色温/动画时序)
- 提供三个层级解决方案

**触发词**:
- "重新设计"
- "redesign"
- "review UI"
- "优化交互体验"

**解决方案层级**:
1. 渐进改进
2. 结构重设计
3. 理想方案

**特点**: 透明展示权衡，不是敷衍的"这里颜色改一下"

**安装**:
```bash
npx skills add joeseesun/qiaomu-design-advisor
```

---

## 📦 四、Skill 管理与发现

### Skill Publisher —— 发布你的 Skill

**仓库**: https://github.com/joeseesun/skill-publisher

**功能**: 自动完成 Skill 发布流程

**流程**:
```
验证 SKILL.md 元数据 → 创建 GitHub 仓库 → 推送代码 → 验证可安装
```

**安装**:
```bash
npx skills add joeseesun/skill-publisher
```

**前置条件**: GitHub CLI (gh) 已安装并认证

---

## 🔍 去哪找更多 Skill?

### 1. Skills.sh —— Vercel 官方目录 🏆

**链接**: https://skills.sh/

**特点**:
- Vercel 打造的开源 Skills 目录
- 收录 **86,000+** 个 Skills
- 支持 20+ 平台 (Claude Code/GitHub Copilot/Cursor/Cline/Gemini 等)
- 可按热度、趋势筛选

---

### 2. Find Skills —— 用 Skill 找 Skill 🔎

**链接**: https://skills.sh/vercel-labs/skills/find-skills

**一句话**: "元 Skill"，在终端搜索和安装其他 Skill

**安装**:
```bash
npx skills add vercel-labs/skills/find-skills
```

**使用**:
```bash
npx skills find react performance
```

---

### 3. SkillsMP —— 最大 Skill 集市 🛒

**链接**: https://skillsmp.com/zh

**特点**:
- 社区驱动的 Skills 聚合平台
- 收录 **380,000+** 个 Skills
- 支持中文界面
- 从 GitHub 公开仓库自动抓取
- 质量过滤 (最低 2 stars 门槛)

---

## 💡 核心洞察

### 1. Skill 是灵魂
> "没有 Skill 的龙虾，就像一台没装 App 的手机。"

### 2. 先想清楚需求
> "与其追热点装龙虾，不如先想清楚：你让 AI 帮你干什么？"

### 3. 三类核心能力
| 类别 | 作用 | 代表 Skill |
|------|------|------------|
| 抓取采集 | 喂得进东西 | Agent Reach |
| 内容创作 | 生产 + 分发 | 宝玉合集 |
| 效率工具 | 生活场景 | Spotify/Design |

### 4. 生态成熟度
- **86,000+** Skills (Skills.sh)
- **380,000+** Skills (SkillsMP)
- 完整工具链：发现→安装→发布

---

## ⚠️ 注意事项

| Skill | 注意事项 |
|-------|----------|
| Agent Reach | 中文平台需 Docker |
| yt-search-download | 需 YouTube API Key，常更新 yt-dlp |
| Spotify Player | 需 Premium 账号 |
| Skill Publisher | 需 GitHub CLI 认证 |

---

## 📌 行动建议

### 新手入门 (必装 3 个)
1. **Agent Reach** - 信息抓取基础
2. **Defuddle** - 网页内容提取
3. **宝玉合集** - 内容创作全家桶

### 进阶配置
1. **Anything to NotebookLM** - 内容二次创作
2. **Knowledge Site Creator** - 知识可视化
3. **Design Advisor** - UI/UX 优化

### 高级玩法
1. 用 **Skill Publisher** 发布自己的 Skill
2. 用 **Find Skills** 发现更多工具
3. 在 **SkillsMP** 分享作品

---

## 🔗 资源汇总

| 类型 | 平台 | 链接 |
|------|------|------|
| **综合目录** | Skills.sh | https://skills.sh/ |
| **中文集市** | SkillsMP | https://skillsmp.com/zh |
| **元搜索** | Find Skills | `npx skills add vercel-labs/find-skills` |
| **作者主页** | @vista8 | https://x.com/vista8 |

---

## 📊 Skill 清单速查

| # | 名称 | 类别 | 安装命令 |
|---|------|------|----------|
| 1 | Agent Reach | 抓取 | `npx skills add Panniantong/agent-reach` |
| 2 | Defuddle | 抓取 | `npx skills add joeseesun/defuddle-skill` |
| 3 | yt-search-download | 抓取 | `npx skills add joeseesun/yt-search-download` |
| 4 | anything-to-notebooklm | 抓取 | `git clone + ./install.sh` |
| 5 | baoyu-skills | 创作 | `npx skills add jimliu/baoyu-skills` |
| 6 | qiaomu-x-article-publisher | 创作 | `git clone + pip install` |
| 7 | knowledge-site-creator | 创作 | `npx skills add joeseesun/knowledge-site-creator` |
| 8 | qiaomu-music-player-spotify | 效率 | `npx skills add joeseesun/qiaomu-music-player-spotify` |
| 9 | qiaomu-design-advisor | 效率 | `npx skills add joeseesun/qiaomu-design-advisor` |

---

**总结生成**: KilroyContentBot  
**抓取工具**: x-fetcher  
**仓库**: https://github.com/wsj0415/kilroy-cdn  
**分类**: OpenClaw/Skills 推荐/实战指南
