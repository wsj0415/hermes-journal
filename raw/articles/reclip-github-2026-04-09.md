# ReClip — 自托管视频下载器

**来源**: https://github.com/averygan/reclip  
**抓取时间**: 2026-04-09 14:04 UTC  
**类型**: GitHub 项目  
**标签**: video-downloader, yt-dlp, self-hosted, open-source, python, flask

---

## 核心数据

| 指标 | 数值 |
|------|------|
| Stars | 2.2k |
| Forks | 363 |
| 后端代码 | ~150 行 Python |
| 依赖 | 2 个（Flask, yt-dlp） |
| 支持网站 | 1000+ |
| 许可证 | MIT |

---

## 功能

- ✅ 下载 1000+ 网站视频（基于 yt-dlp）
- ✅ MP4 视频或 MP3 音频提取
- ✅ 质量/分辨率选择器
- ✅ 批量下载 — 一次粘贴多个 URL
- ✅ 自动 URL 去重
- ✅ 简洁响应式 UI — 无框架、无构建
- ✅ 单文件后端（~150 行 Python）

---

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Python + Flask (~150 行) |
| 前端 | Vanilla HTML/CSS/JS (单文件) |
| 下载引擎 | yt-dlp + ffmpeg |
| 依赖 | Flask, yt-dlp |

---

## 快速开始

### 本地运行
```bash
brew install yt-dlp ffmpeg
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```
访问：http://localhost:8899

### Docker
```bash
docker build -t reclip . && docker run -p 8899:8899 reclip
```

---

## 支持平台

YouTube, TikTok, Instagram, Twitter/X, Reddit, Facebook, Vimeo, Twitch, Dailymotion, SoundCloud, Loom, Streamable, Pinterest, Tumblr, Threads, LinkedIn 等 1000+ 网站。

---

## 对内容创作的价值

1. **批量下载对标视频** → 本地分析 → 提取爆款模式
2. **下载竞争对手内容** → AI 分析结构 → 生成改进建议
3. **建立视频素材库** → 分类存储 → AI 学习节奏/钩子

---

## 工作流集成

```
ReClip 下载 → raw/videos/
         ↓
yt-dlp 提取字幕 → raw/youtube/
         ↓
AI 分析脚本结构 → wiki/concepts/
         ↓
生成改编建议 → reports/content/
```

---

*原始来源：https://github.com/averygan/reclip*
