import json
import requests
import base64
import re
import uuid

class OCRClient:
    def __init__(self, app_id: str, secret_code: str):
        self.app_id = app_id
        self.secret_code = secret_code

    def recognize(self, file_content: bytes, options: dict) -> str:
        # 构建请求参数
        params = {}
        for key, value in options.items():
            params[key] = str(value)

        # 设置请求头
        headers = {
            "x-ti-app-id": self.app_id,
            "x-ti-secret-code": self.secret_code,
            # 方式一：读取本地文件
            "Content-Type": "application/octet-stream"
            # 方式二：使用URL方式
            # "Content-Type": "text/plain"
        }

        # 发送请求
        response = requests.post(
            f"https://api.textin.com/ai/service/v1/pdf_to_markdown",
            params=params,
            headers=headers,
            data=file_content
        )

        # 检查响应状态
        response.raise_for_status()
        return response.text


def md_clean( con):
    # 处理url的图片
    img_chunks = re.findall(r"\!\[.*?\]\(http.*?\)", con)
    # print(img_chunks)
    for i in img_chunks:
        img_url = re.findall(r"\!\[.*?\]\((http.*?)\)", i)[0].split()[0]
        if len(re.findall(r"\!\[.*?\]\((http.*?)\)", i)[0].split()) > 1:
            img_title = re.findall(r"\!\[.*?\]\((http.*?)\)", i)[0].split()[1]
        else:
            img_title = ""
        new_img_description = ""

        if img_title:
            new_img_chunk = f"![{new_img_description}]({img_url} {img_title})"
        else:
            new_img_chunk = f"![{new_img_description}]({img_url})"
        con = con.replace(i, new_img_chunk)
    # 处理base64的图片

    img_chunks = re.findall(
        r"\!\[.*?\]\(data:image/.*?;base64,.*?\)", con, re.DOTALL
    )

    for img_chunk in img_chunks:
        img_type = re.findall(
            r"\!\[.*?\]\(data:image/(.*?);base64,.*?\)", img_chunk, re.DOTALL
        )[0]
        img_title = uuid.uuid4().hex

        img_base64 = re.findall(
            r"\!\[.*?\]\(data:image/.*?;base64,(.*)?\)", img_chunk, re.DOTALL
        )[0]
        try:
            image_data = base64.b64decode(img_base64)
        except (TypeError, ValueError) as e:
            image_data = ""
            continue

        img_file_name = f"{img_title}.{img_type}"
        # img_url = self.save_img(img_file_name, image_data, self.document_id)
        # new_img_chunk = f"![img]({img_url}) \n\n new_img_description"
        # con = con.replace(img_chunk, img_chunk)

    return con


def main():
    # 创建客户端实例，需替换你的API Key
    client = OCRClient("de7a48f2d9411511100b6f3ded0105b2", "67fbe01d14a6ad533d818c56bb13e205")

    # 在main函数中插入
    # 读取本地文件
    with open("/Users/marshio/Downloads/XPLORE使用手册.pdf", "rb") as f:
        file_content = f.read()

    # 设置URL参数，可按需设置，这里已为你默认设置了一些参数
    options = {
            # https://docs.textin.com/xparse/parse-quickstart#url%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E
            "char_details": 0,
            "page_details": 0,
            "catalog_details": 0,
            "dpi": 144,
            "page_start": 1,
            "page_count": 1000,
            "apply_document_tree": 1,
            "markdown_details": 1,
            "table_flavor": "md",
            "get_image": "objects",
            "image_output_type": "default",
            "parse_mode": "scan",
            "get_excel": 0,
            "remove_watermark": 0,
            "paratext_mode": "none",
            "apply_merge": 0,
            "apply_chart": 1,
    }
    # dict(
    #     dpi=144,
    #     get_image="objects",
    #     markdown_details=1,
    #     page_count=10,
    #     parse_mode="auto",
    #     table_flavor="html"
    # )

    try:
        # response = client.recognize(file_content, options)

        # 解析JSON响应以提取markdown内容
        # json_response = json.loads(response)
        # if "result" in json_response and "markdown" in json_response["result"]:
        #     markdown_content = json_response["result"]["markdown"]
        #     with open("result.md", "w", encoding="utf-8") as f:
        #         f.write(markdown_content)

        with open("result.md", "r", encoding="utf-8") as f:
            text = f.read()
            print(text)
            # print(md_clean(text))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()