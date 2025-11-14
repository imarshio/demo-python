from langchain_text_splitters.markdown import MarkdownTextSplitter
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
headers_to_split_on = [
    ("#", "chapter"),       # 一级标题 -> metadata 中的 "chapter" 字段
]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on, False,False)
with open("../parser/pdf/result.md", "r", encoding="utf-8") as f:
    text = f.read()
    strs = splitter.split_text(text)
    for s in strs:
        print("=" * 20 , "\n")
        print(s)
        print("=" * 20, "\n")
