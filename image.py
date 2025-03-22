from typing import Any
import os

from openai import OpenAI
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("image")

## constants
XAI_API_BASE = "https://api.x.ai/v1"
XAI_API_KEY = os.getenv("XAI_API_KEY")

client = OpenAI(base_url=XAI_API_BASE, api_key=XAI_API_KEY)

def generate_image(prompt: str, n: int, response_format: str) -> Any:
    try:
        response = client.images.generate(
            model="grok-2-image",
            prompt=prompt,
            n=n,
            response_format=response_format,
        )
        return response
    except Exception as e:
        return None

@mcp.tool()
def generate_image_tool(prompt: str, n: int, response_format: str) -> Any:
    """生成图片

    Args:
        prompt (str): 图片描述，required
        n (int): 生成图片的数量，默认为1
        response_format (str): 返回图片的格式，"url" or "b64_json"
    """
    data = generate_image(prompt, n, response_format)
    if data is None:
        return "生成图片失败"
    
    result = []
    for image in data.data:
        image_data = {
            "revised_prompt": image.revised_prompt
        }
        if response_format == "url":
            image_data["url"] = image.url
        else:
            image_data["b64_json"] = image.b64_json
        result.append(image_data)
    
    return result if len(result) > 1 else result[0]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')