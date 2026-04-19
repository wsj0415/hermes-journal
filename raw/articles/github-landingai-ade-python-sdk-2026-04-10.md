# LandingAI ADE Python SDK — 代理文档提取库

**来源**: https://github.com/landing-ai/ade-python  
**抓取时间**: 2026-04-10 13:05 UTC  
**类型**: GitHub 仓库 / Python SDK  
**标签**: landingai, ade, python-sdk, document-extraction, mcp-server, async-processing, schema-extraction, ai-document-processing, developer-tools, api-integration

---

## 📊 一句话总结

LandingAI 推出的 Python SDK 用于 Agentic Document Extraction API，支持同步/异步客户端、大文档异步作业、自动重试、安全 API 密钥处理、无缝文件上传、基于 Schema 的数据提取、可插拔 HTTP 后端（httpx/aiohttp），带 MCP 服务器支持 AI 助手集成。

---

## 🏷️ 话题标签

#LandingAI #文档提取 #Python SDK #ADE #MCP 服务器 #异步处理 #Schema 提取 #AI 文档处理 #开发者工具 #API 集成

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Python SDK 代码风格 ⭐ 推荐

**来源**: nano-banana-pro / App / Web Design  
**参考 ID**: 171 (VS Code Extension Screenshot)  
**示例图**: https://cms-assets.youmind.com/media/1772519704150_r110r3_HCbTg1yXEAAYQy-.jpg

```prompt
VS Code style screenshot of "LandingAI ADE Python SDK" code editor.

Style: Dark theme code editor, syntax highlighted Python code, clean modern IDE aesthetic.

Code shown:

from landingai_ade import LandingAIADE

client = LandingAIADE(
    apikey=os.environ.get("VISION_AGENT_API_KEY"),
    environment="eu",
)

response = client.parse(
    document=Path("file.pdf"),
    model="dpt-2-latest",
    save_to="./output",
)

Sidebar annotations:
- ✅ "Fully-typed SDK"
- ⚡️ "Sync & Async"
- 📄 "Large Doc Jobs"
- 🔁 "Auto Retries"
- 🧩 "Schema Extraction"

Bottom status bar:
"Python 3.9+" | "PyPI: landingai-ade" | "MCP Ready"

Window title: "LandingAI ADE — Agentic Document Extraction"

Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是 Python SDK，代码编辑器截图风格直接展示实际用法，比抽象 infographic 更直观对开发者。

---

### 选项 2：SDK 架构流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Technical SDK architecture diagram for "LandingAI ADE Python SDK".

Layout: Horizontal flow from Python code → API → Output.

Color Palette:
- Python: Blue (#3776AB)
- API: Green (#10B981)
- Output: Purple (#8B5CF6)
- Background: Dark gradient

Left — Python Client:
代码块图标
"Sync Client"
"Async Client"
"Typed with Pydantic"

Center — API Endpoints:
四个 API 盒子：
1. Parse — 文档解析
2. Split — 文档分割
3. Extract — Schema 提取
4. Jobs — 异步作业

Right — Output:
输出图标：
"Chunks"
"Splits"
"Structured Data"
"Saved JSON"

Bottom — Features:
功能标签：
"Auto Retries" | "Large Docs" | "MCP Server"
"httpx/aiohttp" | "Save To" | "Error Handling"

Title: "LandingAI ADE SDK Architecture"

Style: Clean technical diagram, dark mode with neon accents
Aspect ratio: 9:16 portrait
```

---

### 选项 3：MCP 集成展示

**来源**: nano-banana-pro / App / Web Design  
**参考 ID**: 179 (Cursor MCP Integration)  
**示例图**: https://cms-assets.youmind.com/media/1772519704323_78n1qe_HCbTgkCXEAAfLqO.jpg

```prompt
Cursor/VS Code MCP integration screenshot for "LandingAI ADE MCP Server".

Style: AI IDE interface, MCP server panel visible, chat sidebar.

Main view:
MCP Server: "landingai-ade-mcp"
Status: ● Connected
Endpoints: 4 available

Chat sidebar:
User: "Parse this PDF and extract structured data"
MCP: "Using LandingAI ADE API to parse document..."
Shows: parse() call, response preview

Install buttons visible:
[Add to Cursor] [Install in VS Code]

Code snippet:
npx -y landingai-ade-mcp

Environment:
VISION_AGENT_API_KEY=***

Bottom badge:
"AI Assistants Can Now Use ADE API"

Aspect ratio: 9:16 portrait
```

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| **完全类型化 SDK** | 带 Pydantic 响应模型，自动补全和文档 |
| **同步 & 异步客户端** | `LandingAIADE` / `AsyncLandingAIADE` |
| **大文档处理** | 通过异步作业处理大文件 |
| **自动重试** | 指数退避，默认重试 2 次 |
| **安全 API 密钥** | 支持环境变量，推荐 python-dotenv |
| **无缝文件上传** | 支持 PathLike/bytes/tuple |
| **Schema 数据提取** | 基于 Pydantic 模型的结构化提取 |
| **可插拔 HTTP 后端** | httpx（默认）或 aiohttp |
| **save_to 参数** | 自动保存响应到文件夹 |

---

## 🔌 MCP 服务器

**用途**: 让 AI 助手能够与 ADE API 交互，探索端点、测试请求、帮助集成 SDK。

### 安装方式

**Cursor**:
```bash
# 点击"Add to Cursor"按钮
# 或手动配置 MCP
```

**VS Code**:
```bash
# 点击"Install in VS Code"按钮
```

**手动配置**:
```json
{
  "mcpServers": {
    "landingai-ade-mcp": {
      "command": "npx",
      "args": ["-y", "landingai-ade-mcp"],
      "env": {
        "VISION_AGENT_API_KEY": "Your API Key"
      }
    }
  }
}
```

---

## 📦 安装

```bash
# 从 PyPI 安装
pip install landingai-ade

# 带 aiohttp 后端
pip install landingai-ade[aiohttp]
```

---

## 💻 使用示例

### Parse（解析文档）

```python
import os
from pathlib import Path
from landingai_ade import LandingAIADE

client = LandingAIADE(
    apikey=os.environ.get("VISION_AGENT_API_KEY"),
    environment="eu",  # 或 "production"
)

response = client.parse(
    document=Path("path/to/file"),  # 本地文件
    # document_url="https://...",  # 或远程 URL
    model="dpt-2-latest",
    save_to="./output_folder",  # 可选：保存为 {input}_parse_output.json
)
print(response.chunks)
```

---

### Split（分割文档）

```python
import json
from pathlib import Path
from landingai_ade import LandingAIADE

client = LandingAIADE()

# 先解析文档
parse_response = client.parse(
    document=Path("/path/to/document.pdf"),
    model="dpt-2-latest"
)

# 定义分割规则
split_class = [
    {
        "name": "Bank Statement",
        "description": "Document from a bank that summarizes all account activity."
    },
    {
        "name": "Pay Stub",
        "description": "Document that details an employee's earnings.",
        "identifier": "Pay Stub Date"
    }
]

# 使用解析的 Markdown 进行分割
split_response = client.split(
    split_class=json.dumps(split_class),
    markdown=parse_response.markdown,
    model="split-latest"
)

# 访问分割结果
for split in split_response.splits:
    print(f"Classification: {split.classification}")
    print(f"Identifier: {split.identifier}")
    print(f"Pages: {split.pages}")
```

---

### Parse Jobs（异步作业）

```python
from pathlib import Path
from landingai_ade import LandingAIADE

client = LandingAIADE()

# 创建异步解析作业
job = client.parse_jobs.create(
    document=Path("path/to/large_file.pdf"),
    model="dpt-2-latest",
)
print(f"Job created with ID: {job.job_id}")

# 获取作业状态
job_status = client.parse_jobs.get(job.job_id)
print(f"Status: {job_status.status}")

# 列出所有作业（可选过滤）
response = client.parse_jobs.list(
    status="completed",
    page=0,
    page_size=10,
)
for job in response.jobs:
    print(f"Job {job.job_id}: {job.status}")
```

---

### Extract（Schema 提取）

```python
from pathlib import Path
from landingai_ade import LandingAIADE
from landingai_ade.lib import pydantic_to_json_schema
from pydantic import BaseModel, Field

# 定义 Schema
class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")

# 转换为 JSON Schema
schema = pydantic_to_json_schema(Person)

# 使用 SDK
client = LandingAIADE()
response = client.extract(
    schema=schema,
    markdown=Path("path/to/file.md"),
    save_to="./output_folder",
)
```

---

### 异步用法

```python
import asyncio
from pathlib import Path
from landingai_ade import AsyncLandingAIADE

client = AsyncLandingAIADE(
    apikey=os.environ.get("VISION_AGENT_API_KEY"),
)

async def main() -> None:
    response = await client.parse(
        document=Path("path/to/file"),
        model="dpt-2-latest",
    )
    print(response.chunks)

asyncio.run(main())
```

---

### 使用 aiohttp 后端

```python
import asyncio
from pathlib import Path
from landingai_ade import DefaultAioHttpClient, AsyncLandingAIADE

async def main() -> None:
    async with AsyncLandingAIADE(
        apikey=os.environ.get("VISION_AGENT_API_KEY"),
        http_client=DefaultAioHttpClient(),  # 使用 aiohttp
    ) as client:
        response = await client.parse(
            document=Path("path/to/file"),
            model="dpt-2-latest",
        )
        print(response.chunks)

asyncio.run(main())
```

---

## ⚠️ 错误处理

```python
import landingai_ade
from landingai_ade import LandingAIADE

client = LandingAIADE()

try:
    client.parse()
except landingai_ade.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # 底层异常，可能在 httpx 内
except landingai_ade.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except landingai_ade.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

### 错误代码表

| 状态码 | 错误类型 |
|--------|----------|
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| ≥500 | `InternalServerError` |
| N/A | `APIConnectionError` |

---

## ⚙️ 配置选项

### 重试 (Retries)

```python
# 全局配置（默认 2 次）
client = LandingAIADE(max_retries=0)

# 单次请求配置
client.with_options(max_retries=5).parse()
```

**自动重试的错误**: 连接错误、408 Request Timeout、409 Conflict、429 Rate Limit、≥500 Internal errors

---

### 超时 (Timeouts)

```python
# 全局配置（默认 8 分钟）
client = LandingAIADE(timeout=20.0)  # 20 秒

# 细粒度控制
client = LandingAIADE(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# 单次请求配置
client.with_options(timeout=5.0).parse()
```

---

### 日志 (Logging)

```bash
# 设置环境变量
export LANDINGAI_ADE_LOG=info
# 或 debug 获取更详细日志
```

---

## 🔧 高级用法

### 访问原始响应数据

```python
# 访问响应头
response = client.with_raw_response.parse()
print(response.headers.get('X-My-Header'))

# 获取解析对象
client = response.parse()
print(client.chunks)
```

---

### 流式响应

```python
# 使用上下文管理器流式读取
with client.with_streaming_response.parse() as response:
    print(response.headers.get("X-My-Header"))
    
    for line in response.iter_lines():
        print(line)
```

---

### 自定义/未文档化的请求

```python
import httpx

# 未文档化的端点
response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

# 未文档化的参数
client.parse(
    extra_query={"custom_param": "value"},
    extra_body={"custom_body": "data"},
    extra_headers={"X-Custom-Header": "value"},
)

# 未文档化的响应属性
response.unknown_prop  # 访问额外字段
response.model_extra   # 获取所有额外字段为 dict
```

---

### 配置 HTTP 客户端

```python
import httpx
from landingai_ade import LandingAIADE, DefaultHttpxClient

client = LandingAIADE(
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)

# 单次请求配置
client.with_options(http_client=DefaultHttpxClient(...))
```

---

### 管理 HTTP 资源

```python
# 使用上下文管理器自动关闭
with LandingAIADE() as client:
    # make requests here
    ...
# HTTP client is now closed

# 或手动关闭
client.close()
```

---

## 📋 类型系统

### Pydantic 模型

响应是 Pydantic 模型，提供辅助方法：
- `model.to_json()` — 序列化为 JSON
- `model.to_dict()` — 转换为字典

### TypedDict

嵌套请求参数是 TypedDict，提供自动补全和文档。

### 区分 null 和缺失

```python
if response.my_field is None:
    if 'my_field' not in response.model_fields_set:
        print('字段完全缺失')
    else:
        print('字段值为 null')
```

---

## 📦 版本控制

遵循 SemVer，但某些向后不兼容的变更可能作为 minor 版本发布：
1. 仅影响静态类型，不影响运行时行为
2. 库内部实现变更（非公开 API）
3. 预计不影响绝大多数用户的变更

**查看版本**:
```python
import landingai_ade
print(landingai_ade.__version__)
```

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| REST API 文档 | https://docs.landing.ai/ |
| 完整 API | https://github.com/landing-ai/ade-python/blob/main/api.md |
| PyPI | https://pypi.org/project/landingai-ade/ |
| GitHub | https://github.com/landing-ai/ade-python |
| 贡献指南 | https://github.com/landing-ai/ade-python/blob/main/CONTRIBUTING.md |

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Python 版本 | 3.9+ |
| 默认重试 | 2 次 |
| 默认超时 | 8 分钟 |
| HTTP 后端 | httpx / aiohttp |
| API 端点 | 4 个（Parse/Split/Extract/Jobs） |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Fully-typed SDK with Pydantic" | 类型安全 |
| "Sync & Async clients" | 双客户端支持 |
| "Large document processing via async jobs" | 大文档支持 |
| "Built-in retries with exponential backoff" | 自动重试 |
| "Schema-based data extraction" | 结构化提取 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Schema 提取** — 结构化数据提取可用于内容分析
2. **异步作业** — 大文档处理模式可参考
3. **MCP 集成** — AI 助手可直接调用 API
4. **自动重试** — 错误处理最佳实践
5. **类型化 SDK** — 自动补全和文档

### 可实施
- 用 Schema 提取结构化内容数据
- 实现异步处理长文档/视频转录
- 探索 MCP 服务器集成可能性
- 改进错误处理和重试逻辑
- 添加类型提示改善开发体验

---

*原始来源：https://github.com/landing-ai/ade-python*
