# KNOX — AI 视频制作系统完整实施指南

**来源**: https://x.com/knoxtwts/status/2043091190007107789  
**作者**: KNOX (@knoxtwts)  
**抓取时间**: 2026-04-12 18:43 UTC  
**类型**: X 推文线程/完整教程  
**标签**: ai-video, ugc, higgsfield, nano-banana, kling, veo, seedance, elevenlabs, motion-transfer, video-production

---

## 📊 一句话总结

KNOX 分享 8 个月打磨的 AI 视频制作系统，涵盖 Higgsfield JSON 提示词结构/参考图像管道/Visionstruct 方法/多模型选择策略（Kling/Veo/Seedance）/两步声音规范化管道/反 AI 痕迹技巧/3 完整工作流/成本分析（$0.38-0.50/视频 vs 传统$300-800），生成超真实 UGC 内容规模化生产。

---

## 🏷️ 话题标签

#AI 视频 #UGC 制作 #Higgsfield #NanoBanana #Kling #Veo #Seedance #ElevenLabs #动作转移 #视频制作

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：AI 视频制作栈全景图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
AI Video Production System infographic showing complete stack.

Layout: Vertical flow showing 5 production stages.

Color Palette:
- Character Gen: Purple (#8B5CF6)
- Video Gen: Blue (#3B82F6)
- Voice: Green (#10B981)
- Editing: Orange (#F97316)
- Cost: Yellow (#FBBF24)
- Background: Dark gradient

Stage 1 — Character Generation (Higgsfield):
图标：JSON 文档
"Nano Banana 2 + JSON prompting"
"10x quality vs text prompts"
"Cost: $0.08-0.09/image"
"4-6 scene variations needed"

Stage 2 — Video Generation:
图标：多模型选择
"Kling V3 Pro — Talking head ($4.70/15s)"
"Veo 3.1 — Cinematic B-roll ($0.75/s)"
"Seedance 2.0 — Motion transfer ($0.50-0.80)"
"Max 2 shots/generation"

Stage 3 — Voice Pipeline:
图标：两步规范化
"Step 1: CapCut normalization"
"Step 2: ElevenLabs transform"
"Add room tone at -28db"
"Cost: ~$0.10/video"

Stage 4 — Anti-AI Tells:
图标：真实感技巧
"Film grain: 2-3% overlay"
"Camera shake: 2% first 1-3s"
"Filler words: um/like/you know"
"Micro-pauses: 0.3-0.5s"
"Asymmetry: flyaway hair, uneven smile"

Stage 5 — Cost Breakdown:
图标：成本对比
"30s UGC ad total: ~$10"
"At scale (200+/month): $0.38-0.50/video"
"Traditional UGC: $300-800/video"
"99% cost reduction"

Center Badge:
"8 months to figure out"
"Hyper-realistic UGC at scale"
"35-65+ demographic = 85% spending"

Bottom Badge:
"JSON prompts = blueprint"
"Reference images = color grade"
"Two-step voice = natural sound"

Style: Modern production stack, dark mode with stage colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于完整 AI 视频制作系统的教程，垂直流程图直接展示从角色生成到成本分析的全流程，比单一架构图更能传达"端到端工作流"的价值。

---

### 选项 2：多模型对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
AI Video Models comparison diagram showing strengths and use cases.

Layout: 4 model cards with specs and best uses.

Color Palette:
- Higgsfield: Purple (#8B5CF6)
- Kling: Blue (#3B82F6)
- Veo: Green (#10B981)
- Seedance: Orange (#F97316)
- Background: Dark gradient

Higgsfield (Nano Banana 2) 🟣:
"Character Generation"
"JSON prompting = 10x quality"
"Text prompts = grayscale, 4-5 colors"
"Cost: $0.08-0.09/image"
"Best for: Master character reference"
"Structure: composition/subject/lighting/color"

Kling V3 Pro 🔵:
"Talking Head Dialogue"
"Voice consistency across videos"
"Multi-shot: 2 shots (7s + 8s)"
"Cost: $4.70/generation via API"
"Best for: Presenter dialogue"
"Limit: 512 chars, 2.5 words/sec"

Veo 3.1 🟢:
"Cinematic B-roll"
"Ingredient mode locks face + product"
"First-to-last frame consistency"
"Cost: ~$0.75/second"
"Best for: Product consistency"
"Workflow: Visual-first"

Seedance 2.0 (ByteDance) 🟠:
"Motion Transfer"
"@1 image, @2 video, @3 audio"
"Up to 12 inputs total"
"Cost: ~$0.50-0.80/generation"
"Best for: Template replication"
"Output: 4-15s at 2K"

Center Insight:
"Wrong model for shot type = wasted credits"
"Kling = dialogue best"
"Veo = product consistency"
"Seedance = motion transfer"

Bottom Badge:
"Max 2 shots/Kling generation"
"Quality degrades past 2"
"Assemble in post"

Style: Clean model comparison, dark mode with model colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：成本对比风格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules comparing "AI UGC vs Traditional UGC Costs".

Color Palette:
- AI: Blue/green tones
- Traditional: Red/gray tones
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"AI 视频制作系统"
"8 个月打磨"
Icon: Video + Dollar sign

M2 — AI Costs:
"Higgsfield: $0.08-0.09/image"
"Kling: $4.70/15s generation"
"Seedance: $0.50-0.80"
"Voice: ~$0.10/video"

M3 — 30s Ad Total:
"4-6 images: ~$0.50"
"2 Kling generations: ~$9.40"
"Voice pipeline: ~$0.10"
"Total: ~$10/ad"

M4 — At Scale:
"200+ videos/month"
"Batch image = lower cost"
"Voice cloning = no per-video"
"Effective: $0.38-0.50/video"

M5 — Traditional UGC:
"Creator fees: $150-500/video"
"Editing + iteration: $300-800"
"Revision rounds included"
"Total: $300-800/video"

M6 — Savings:
"99% cost reduction"
"$10 vs $800"
"Same quality output"
"35-65+ can't detect"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心突破：JSON 提示词 vs 文本提示词

### 问题：文本提示词的局限

> **文本提示词产生灰度色彩分级。最多 4-5 种颜色。有时真实，有时垃圾。**

---

### 解决方案：JSON 作为蓝图

> **JSON 作为蓝图。它控制精确色彩分级/真实光照/视觉风格细节。输出质量提升 10 倍。**

---

### JSON 提示词结构

```json
{
  "image_type": "photograph",
  "genre": "indoor lifestyle selfie portrait",
  "orientation": "vertical",
  "aspect_ratio": "approximately 3:4",
  "composition": {
    "framing": "tight medium portrait",
    "camera_height": "slightly above eye level due to arm-extended selfie",
    "camera_angle": "subtle downward angle with head tilt",
    "subject_position": "centered with slight left bias",
    "cropping": "head, shoulders, upper torso visible",
    "depth_of_field": "shallow to moderate; subject sharply in focus, background softly receding",
    "visual_balance": "clean asymmetrical balance created by head tilt and light-shadow split",
    "leading_lines": "light edge on wall and jersey neckline guide attention to face",
    "negative_space": "minimal but effective; plain walls isolate subject"
  },
  "subject": {
    "count": 1,
    "primary_subject": {
      "gender_presentation": "female",
      "approximate_age": "young adult",
      "pose": "arm-extended selfie with head tilted slightly downward and toward camera",
      "expression": "soft, cute, subtly pouty",
      "facial_expression_details": "relaxed eyes, gentle pout lips, calm brows",
      "gaze": "direct eye contact with camera",
      "skin_tone": "light with warm sun-kissed highlights",
      "hair": {
        "color": "light blonde",
        "style": "long, straight, worn loose",
        "part": "slight side part",
        "texture": "smooth with natural volume"
      },
      "accessories": {
        "earrings": "small gold hoop earrings",
        "necklaces": "layered delicate gold chains with small pendants"
      },
      "clothing": {
        "top": {
          "type": "basketball jersey",
          "team_style": "Los Angeles Lakers style",
          "color": "purple with gold and white trim",
          "material": "mesh athletic fabric",
          "fit": "relaxed, sleeveless"
        }
      }
    }
  },
  "environment": {
    "setting": "indoor residential hallway or room",
    "background_elements": [
      "plain white wall",
      "wooden interior door",
      "soft shadow gradients"
    ],
    "surface_materials": {
      "walls": "painted drywall, matte finish",
      "door": "natural wood veneer"
    }
  },
  "lighting": {
    "type": "mixed natural and ambient indoor lighting",
    "primary_light_source": {
      "source": "direct sunlight through window",
      "direction": "left side of subject's face",
      "color_temperature": "warm daylight (~5000K)"
    },
    "lighting_pattern": "distinct light-and-shadow split across face and torso",
    "fill_light": {
      "source": "ambient room light",
      "effect": "softly lifts shadows without flattening contrast"
    },
    "shadow_quality": "defined but soft-edged",
    "contrast": "medium to high due to directional sunlight",
    "highlights": "strong highlights on cheekbone, forehead, nose bridge, and shoulder",
    "overall_mood": "intimate, warm, editorial-casual"
  },
  "color_palette": {
    "dominant_colors": [
      "purple",
      "warm skin tones",
      "white",
      "wood brown"
    ],
    "accent_colors": [
      "gold",
      "yellow",
      "black"
    ],
    "white_balance": "slightly warm",
    "saturation": "moderate with vivid jersey color emphasis"
  },
  "focus_and_clarity": {
    "focus_point": "eyes and upper facial features",
    "sharpness": "high on subject",
    "clarity": "crisp skin texture and fabric detail",
    "noise": "minimal, clean indoor exposure"
  },
  "camera_characteristics": {
    "capture_method": "handheld smartphone selfie",
    "likely_device": "modern smartphone",
    "lens_equivalent": "approximately 24–26mm wide-angle",
    "aperture_effect": "natural depth with slight background softness",
    "exposure": "biased toward highlights, preserving skin glow"
  },
  "stylistic_notes": {
    "aesthetic": "casual sporty-meets-soft portrait",
    "vibe": "cute, confident, relaxed",
    "post_processing": "minimal; slight contrast and warmth enhancement",
    "authenticity": "natural selfie with intentional light positioning"
  },
  "recreation_guidelines": {
    "pose_recreation": "arm-extended selfie, head tilted, relaxed shoulders",
    "expression_recreation": "soft pout with gentle eye contact",
    "wardrobe_recreation": "purple basketball jersey with gold trim",
    "hair_recreation": "long blonde hair worn loose with subtle side part",
    "lighting_setup": "strong side sunlight creating face split-light effect",
    "camera_setup": "smartphone at slight downward angle, close framing",
    "environment_setup": "plain indoor wall with minimal distractions",
    "color_grading": "warm highlights, moderate contrast, vivid purples preserved"
  }
}
```

**成本**: 每个角色图像$0.08-0.09

> **那是你的基础。保存它。为不同活动修改人口统计细节。结构保持不变。**

---

## 参考图像管道（解决过饱和问题）

### 问题

> **Nano Banana Pro 默认过饱和。颜色看起来不对。即使脸真实，图像看起来像 AI 艺术。**

---

### 三步骤解决方案

**Step 1: 收集参考图像**
```
去 Pinterest。搜索想要的审美。找到 5-7 张有目标色彩分级的图像。
暖光照。真实肤色。你在追求的氛围。
```

**Step 2: 用 Gemini 分析**
```json
"Analyze the color grading characteristics of these images. 
Identify hex values for shadows, midtones, highlights. 
Describe the overall tone curve."
```

**Step 3: 添加到 Higgsfield JSON**
```
将输出作为色彩指令添加到 Higgsfield JSON 提示词。
模型现在参考真实世界色彩分级模式。
```

**效果**: 图像从"明显 AI"转为"可能是真实照片"。

---

## Visionstruct 方法（多场景变体）

### 问题

> **一张主图像毫无价值。任何不想看起来像幻灯片的视频需要同一角色的 4-6 个场景变体。**

---

### Visionstruct 结构

**1. 姿势优先**
```
始终用物理位置引领。
"Woman sitting in car driver seat, left hand on steering wheel, 
right hand holding coffee cup, torso turned 15 degrees toward camera."
```

**2. 环境细节**
```
真实环境有杂物。
"Morning sunlight through windshield creating lens flare at 2 o'clock, 
takeout bag visible on passenger seat, parking garage concrete visible 
through rear window."
```

**3. 反 AI 痕迹**
```
这是业余与专业输出的区别。
"Slight undereye circles suggesting early morning, 
2-3% visible skin texture on forehead, 
one flyaway hair strand across left eyebrow, 
asymmetrical smile with left side slightly higher."
```

**总提示词长度**: 150-250 词
- 更短 = 缺乏一致性需要的具体性
- 更长 = 模型开始忽略 tokens

---

### 工作流程

```
1. 在 Higgsfield 生成主参考图像
2. 用 img2img 从主图像创建场景变体
3. 不同姿势，不同环境，相同身份
```

---

## 多模型选择策略

> **不同模型擅长不同事情。为镜头类型用错模型浪费积分且产生劣质输出。**

---

### Kling V3 Pro — 对话工作马

| 特征 | 说明 |
|------|------|
| **定位** | 对话头部对话的最佳模型 |
| **声音** | voice_ids 跨多视频保持声音一致性 |
| **多镜头** | 每视频处理 2 镜头（7s + 8s） |
| **成本** | $4.70/生成（通过 API） |
| **限制** | 512 字符硬限制 |

**有效提示词结构**:
```
Frontal medium shot of the woman, cinematic handheld. Modern kitchen, 
soft warm morning light from window. She looks at camera, slight head 
shake, sets down coffee mug. She says: "Nobody talks about this but 
your morning routine is actually destroying your sleep." Slight lean 
forward on "destroying." natural blinking, NO over-reaction, no 
exaggerated facial movements. natural hand gestures.
Voice_id: Voice_1. tone: casual tone, slightly concerned.
Frontal medium shot, cinematic handheld.
```

**强制页脚**（每条提示词必须有）:
```
"natural blinking, NO over-reaction, no exaggerated facial movements. 
natural hand gestures. Voice_id: Voice_1. tone: [modifier]. 
[Shot type], [camera movement]."
```

---

### Veo 3.1 — 电影感 B-roll

| 特征 | 说明 |
|------|------|
| **定位** | 电影感 B-roll 和产品一致性 |
| **成分模式** | 锁定角色脸和产品元素 |
| **首到尾帧** | 保持跨剪辑环境一致性 |
| **成本** | ~$0.75/秒输出 |
| **工作流** | 视觉优先 |

**Veo 工作流**:
```
1. 上传角色基础图像作为成分一
2. 上传产品照片作为成分二
3. 写描述行动的提示词
4. Veo 锁定两个元素同时生成
```

---

### Seedance 2.0 — 动作转移

| 特征 | 说明 |
|------|------|
| **定位** | ByteDance 模型，通过 Higgsfield 访问 |
| **输入** | 最多 9 图像 +3 视频 +3 音频 = 12 总输入 |
| **输出** | 4-15 秒，原生 2K 分辨率 |
| **成本** | ~$0.50-0.80/生成 |
| **@系统** | 独特功能 |

**@系统**:
```
上传图像/视频/音频。每个自动标记。
@1 = 第一帧
@2 = 相机移动
@3 = 背景音乐

然后提示词中引用它们。
```

---

### 动作转移用例

**案例 1: 舞蹈复制**
```
@1 performs the choreography from @2.
完美动作 + Higgsfield 自定义角色
```

**案例 2: 创意模板复制**
```
找到获胜 UGC 创意。下载作为参考。
@1 = 获胜创意
@2 = Higgsfield 角色
@3 = 产品照片

提示词："Replace the person in @1 with the character from @2. 
Reference @1's camera work, transitions, and editing rhythm. 
Product from @3 replaces original product."
```

**案例 3: 多语言本地化**
```
生成一个英语主视频。
对每个目标语言：
- 上传原视频到 Seedance 作为 @1
- 通过 ElevenLabs 生成目标语言音频作为 @2
- 提示词："@1 with lip sync matched to @2."

相同视觉表演，不同语言音频。
```

---

## Kling 关键规则

### 2.5 词/秒规则

| 视频长度 | 最大词数 |
|----------|----------|
| **30 秒** | 75 词 |
| **15 秒** | 38 词 |
| **10 秒** | 25 词 |

> **模型将任何长脚本压缩到你给的时序中。如果对话自然需要 15 秒说而你设 10 秒视频，唇 sync 完全破裂。**

---

### 2 镜头限制

> **关键规则：每生成最多 2 提示词。超过 2 质量显著下降。如果需要 4 场景，分成 2 个独立生成后剪辑一起。**

---

### 补充剂广告示例提示词

**提示词 1（7 秒，18 词）**:
```
Handheld camera with natural shake, woman standing in luxury apartment 
with windows and skyline. Gray sweatshirt, amber sunglasses. Says 
"Okay so these gut health gummies changed everything for me." 
Animated gestures, confident tone. Bright natural light, slight 
camera movement adds authenticity.
```

**提示词 2（8 秒，20 词）**:
```
Back to the handheld camera, a woman standing in the same apartment 
setting with windows. Removes sunglasses revealing excited eyes, 
leans toward camera. Says "My digestion, and even my skin improved 
in like two weeks. I'm obsessed." Big genuine smile, enthusiastic 
hand gestures. Natural lighting, authentic energy, slight camera 
shake continues.
```

**填充词重要**: 添加"Euuhh..."或停顿让对话听起来自然。真人说"um"和"like"和"you know"。脚本需要这些元素。

---

## 两步声音规范化管道

> **声音是大多数 AI UGC 破裂的地方。节奏太均匀。呼吸太完美。重音模式可预测。**

---

### Step 1: CapCut 声音规范化

```
1. 导入视频到 CapCut
2. 识别角色说话的每个部分
3. 用 CapCut 的"Voice Change"功能
4. 从库中选任何随机基础声音
5. 应用到所有说话部分
```

**作用**:
- 移除奇怪口音
- 移除不一致
- 移除机器人伪影
- 规范化为干净一致的基础

---

### Step 2: ElevenLabs 声音转换

```
1. 从 CapCut 获取规范化音频
2. 上传到 ElevenLabs
3. 用声音转换
4. 应用一个真实声音 profile
```

**结果**: 听起来像真人在像样设备上录制。

---

### 关键：顺序重要

> **CapCut 创建干净基础。ElevenLabs 转换那基础为特定角色声音。跳过第一步，ElevenLabs 输出听起来不一致因为源音频已经不匹配。**

---

### 房间音调层

```
导出最终音频前，在 -28db 添加环境房间噪音。
这填充短语间的沉默，让音频感觉像在真实空间录制。
```

---

## 反 AI 痕迹技巧

### 目标人群

> **35-65+ 人群控制 85% 家庭支出，当正确制作时功能上零能力检测 AI 生成内容。年轻人群正在发展检测本能。**

---

### 6 个反 AI 痕迹

| 技巧 | 参数 | 作用 |
|------|------|------|
| **Film grain** | 2-3% 叠加 | AI 视频太干净。真实手机相机有传感器噪音 |
| **Camera shake** | 2% 移动前 1-3 秒 | 模仿真人"拿起相机"时刻。然后稳定 |
| **Filler words** | "um"/"like"/"you know" | AI 生成脚本有不自然完美流畅 |
| **Room tone** | -28db 环境噪音 | AI 音频短语间沉默太干净 |
| **Micro-pauses** | 0.3-0.5 秒停顿 | 真人说话不是完美流 |
| **Asymmetry** | 一根飞出发丝/不均匀微笑/可见毛孔纹理 | AI 趋向完美对称 |

---

## 3 完整工作流

### 工作流 1: 独奏演讲者 UGC（30 秒，4 场景）

```
1. Higgsfield + Nano Banana 2
   - 用 JSON 结构生成主角色参考
   - 1 图像，优化一致性

2. 生成 4 场景变体
   - 用 img2img 从主图像
   - 不同姿势，不同环境，相同身份

3. 写脚本
   - 2.5 词/秒
   - 30 秒 = 75 词总
   - 包括填充词

4. Kling V3 Pro
   - 视频 1: 场景 1-2（15s, 2 镜头）
   - 视频 2: 场景 3-4（15s, 2 镜头）

5. CapCut 组装
   - 添加 film grain
   - 添加 camera shake 到开场帧
   - 运行声音管道
```

---

### 工作流 2: 动作转移广告（模板复制）

```
1. 在 TikTok/Instagram 找到获胜创意
2. 下载它

3. Higgsfield 生成匹配目标人群的角色

4. 上传到 Seedance
   - @1 = 获胜创意
   - @2 = Higgsfield 角色
   - @3 = 产品照片

5. 提示词:
   "Replace the person in @1 with @2. Reference @1's camera work 
   and editing rhythm. @3 replaces the original product."

6. 生成。运行声音管道。
```

---

### 工作流 3: 多语言活动

```
1. 用工作流 1 生成英语主视频

2. 对每个目标语言:
   - 上传原视频到 Seedance 作为 @1
   - 通过 ElevenLabs 生成目标语言音频作为 @2
   - 提示词："@1 with lip sync matched to @2."

3. 相同视觉表演，不同语言音频
```

---

## 常见错误

| 错误 | 后果 | 解决方案 |
|------|------|----------|
| **每场景相同锚角色图** | 观众注意到。读起来像幻灯片即使有动作 | 始终在 Higgsfield 生成 4-6 姿势变体 |
| **超过 2 镜头/Kling 生成** | 质量显著下降 | 在限制内工作，后期组装 |
| **超过 10 秒唇 sync** | 开始搞砸唇 sync | 不要生成超过 10 秒 |
| **完美音频** | 无填充词/停顿/呼吸 | 手动添加这些 |
| **缺失房间音调** | 短语间沉默太干净 | 在 -28db 层环境房间噪音 |
| **过度提示词** |  hitting 512 字符限制 = 试图控制太多 | 每镜头聚焦一个主要行动 |
| **跳过两步声音管道** | ElevenLabs 单独 + AI 源音频 = 机器人 | CapCut 规范化先 |
| **跨不相关场景用相同背景** | 观众模式匹配重复环境 | 可能时变化设置 |

---

## 成本分析

### 单视频成本

| 项目 | 成本 |
|------|------|
| Higgsfield Nano Banana Pro 图像 | $0.08-0.09/张 |
| Kling V3 Pro 15 秒生成 | $4.70（包括多镜头） |
| Seedance 生成 | ~$0.50-0.80（根据复杂度） |
| Veo 3.1 | ~$0.75/秒输出 |

**标准 30 秒 UGC 广告总计**:
- 4-6 角色图像：~$0.50
- 2 Kling V3 Pro 生成：~$9.40
- 声音管道：~$0.10
- **总计：~$10/成品广告**

---

### 规模化成本（200+ 视频/月）

| 优化 | 效果 |
|------|------|
| 批量图像生成 | 降低每图像成本 |
| 声音克隆 | 消除每视频声音成本 |
| **有效成本** | **$0.38-0.50/视频** |

---

### vs 传统 UGC

| 类型 | 成本 |
|------|------|
| **传统 UGC** | $300-800/成品（创作者费用 + 编辑 + 迭代 + 修订） |
| **AI UGC** | $0.38-0.50/视频（API 成本） |
| **节省** | **99% 成本降低** |

---

## 提示词模板

### 基础动作转移
```
@1 performs the choreography from @2. Modern studio setting. 
Cinematic 4K quality.
```

### 模板复制
```
Replace the person in @1 with the character from @2. Reference @1's 
camera work, transitions, and editing rhythm. [Product from @3] 
replaces [original product]. Keep the same energy and pacing.
```

### 多镜头叙事
```
@1 is the main character. Reference @2 for camera movement. Use @3 
for rhythm. 

Shot 1 (00-05s): Wide establishing shot, character intro, first action
Shot 2 (05-10s): Close-up tracking shot, peak action, camera movement
Shot 3 (10-15s): Climax reveal, dramatic camera, final impact
```

### 一镜到底连续性
```
@1 through @3, one continuous tracking shot following the subject 
up stairs, through corridors, ending with an overhead view.
```

---

### 相机移动术语

| 术语 | 效果 | 提示词示例 |
|------|------|-----------|
| **Dolly push-in** | 亲密/紧张 | "slow dolly push-in toward her face" |
| **Tracking shot** | 跟随主体 | "camera tracks alongside as she walks" |
| **Whip-pan** | 能量/惊喜 | "whip-pan to reveal the door" |
| **Crash zoom** | 震惊/强调 | "sudden crash zoom on the object" |
| **Rack focus** | 转移注意力 | "rack focus from foreground hand to background figure" |
| **Handheld shoulder-cam** | 原始/纪录片 | "handheld shoulder-cam with subtle sway" |
| **Static tripod** | 构图 | "locked-off static tripod, wide shot" |

---

## 人群特定提示词调整

### 年长女性（健康产品 targeting 50+）

```json
{
  "age": "55-65",
  "hair.color": "salt and pepper 或 silver grey",
  "skin.texture": "age lines, sun spots, natural aging",
  "environment.location": "kitchen with morning coffee, pill bottles on counter",
  "pose": "less selfie, more 'caught on camera' natural"
}
```

---

### 健身房男性（健身补充剂）

```json
{
  "gender": "male",
  "age": "28-35",
  "hair.style": "short, slightly sweaty",
  "skin.texture": "flushed from exercise, slight sweat",
  "environment.location": "gym locker room 或 home gym",
  "clothing": "fitted tank top, visible fitness"
}
```

---

### 专业男性（金融/科技）

```json
{
  "gender": "male",
  "age": "30-45",
  "hair.style": "clean cut, professional",
  "environment.location": "home office with monitor, clean desk",
  "camera.device": "webcam for video-call aesthetic"
}
```

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Higgsfield 图像成本 | $0.08-0.09/张 |
| Kling 生成成本 | $4.70/15 秒 |
| Seedance 成本 | $0.50-0.80/生成 |
| Veo 成本 | $0.75/秒 |
| 30 秒广告总成本 | ~$10 |
| 规模化成本 | $0.38-0.50/视频 |
| 传统 UGC 成本 | $300-800/视频 |
| 成本节省 | 99% |
| 目标人群 | 35-65+（控制 85% 支出） |
| 开发时间 | 8 个月 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "JSON acts as blueprint" | JSON 提示词价值 |
| "Multiplies output quality by 10x" | JSON vs 文本 |
| "One master image is worthless" | 需要 4-6 变体 |
| "CapCut creates clean foundation" | 两步声音管道 |
| "35-65+ controls 85% spending" | 目标人群洞察 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **JSON 提示词结构** — 精确控制色彩/光照/风格
2. **参考图像管道** — 用真实图像分析色彩分级
3. **多模型策略** — 根据镜头类型选最佳模型
4. **两步声音规范化** — CapCut + ElevenLabs
5. **反 AI 痕迹** — film grain/camera shake/filler words
6. **成本优化** — 规模化$0.38-0.50/视频

### 可实施
- 为视频内容创建 JSON 提示词模板
- 建立参考图像库用于色彩分级
- 根据内容类型选择最佳生成模型
- 实施两步声音处理管道
- 添加反 AI 痕迹到视频输出
- 优化规模化内容生产成本

---

## 相关资源

| 资源 | 链接 |
|------|------|
| KNOX 原文 | https://x.com/knoxtwts/status/2043091190007107789 |
| Higgsfield | 通过 Higgsfield 访问 |
| Kling V3 Pro | API 访问 |
| Veo 3.1 | Google Veo |
| Seedance 2.0 | ByteDance 模型 |

---

*原始来源：https://x.com/knoxtwts/status/2043091190007107789*
