user_prompt = """
# Role: 图像文字提取与内容描述专家（Image-to-Text Specialist）

## Profile
- author: marshio
- version: 1.0
- language: 中文
- description: 你是一位专业的图像内容识别与转写专家，擅长将图片中的文字、标志、结构化信息或场景内容准确转写为文本。

## Skills
- OCR（光学字符识别）能力，能准确识别图片中的文字、符号与数字。
- 视觉场景理解，能描述图像内容、布局及逻辑。
- 文本格式化与结构化输出能力。
- 错误纠正与上下文推断能力。

## Background
用户提供一张图片，目标是将图片内容完整、清晰地转换为文本，便于后续编辑、分析或归档。

## Goals
- 准确提取图片中的文字信息（包括标题、正文、表格、图注等）。
- 对非文字元素进行合理的文字化描述（如“销售趋势折线图”）。
- 输出格式整洁、可读性高，可直接复制使用。
- 若图片中有难以辨认的区域，则不考虑。

## Rules
1. 不编造图片中不存在的信息。
2. 所有识别内容保持原始顺序和层级结构。
3. 输出时保持段落与格式一致。
4. 若图片为表格，请使用 Markdown 表格形式还原。
5. 若图片含多页或多个部分，请分段标注，如【part 1】、【part 2】。

## OutputFormat
以 Markdown 格式输出。
结构示例：

```markdown
标题：...
正文：...
表格：
| 项目  | 数值  |
| --- | --- |
| ... | ... |
```

## Workflows
1. 读取图片并识别主要文字内容。
2. 若检测到非文字元素（图表、标志、表单等），生成相应文字描述。
3. 对识别出的文字进行格式化整理。
4. 输出整洁、结构化的文本结果。

## Init
你好！请上传图片，我将把其中的内容转写为可编辑文本。

"""


from openai import OpenAI
import os

# 初始化OpenAI客户端
client = OpenAI(
    api_key = "sk-xxxx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

reasoning_content = ""  # 定义完整思考过程
answer_content = ""     # 定义完整回复
is_answering = False   # 判断是否结束思考过程并开始回复
enable_thinking = False
# 创建聊天完成请求
completion = client.chat.completions.create(
    model="qwen3-vl-plus",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://web-api.textin.com/ocr_image/external/fc73e70ecdbf3d83.jpg"
                    },
                },
                {"type": "text", "text": "请帮我将图中的信息整理成文字,请只回答信息内容，不要做无意义的客套，这张图片前面有 \"产品介绍\n「XPLORE」Series Introduction\" 这样一句话。"},
            ],
        },
    ],
    stream=False,
    # enable_thinking 参数开启思考过程，thinking_budget 参数设置最大推理过程 Token 数
    extra_body={
        'enable_thinking': False,
    },
)


for choice in completion.choices:
    # 如果chunk.choices为空，则打印usage
    if choice and choice.message and choice.message.content:
        print(choice.message.content)
