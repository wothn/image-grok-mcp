# image-grok-mcp

实现生成图片的 Model Context Protocol (MCP)的 python 服务器。

## 功能特点

- 基于x.ai的Grok-2-image模型
- 支持多图片生成
- 支持URL和Base64两种返回格式

## API

### 工具

- `generate_image_tool`: 生成图片
  - prompt: 生成图片的提示词
  - n: 生成图片的数量
  - response_format: 返回格式，支持URL和Base64两种格式

## 使用
```
    "image-grok-mcp": {
        "command": "uv",
        "args": [
        "--directory",
        "D:\\Fold\\image-grok-mcp",
        "run",
        "image.py"
        ],
        "env": {
        "XAI_API_KEY":"Your API Key"
        }
    }

```
