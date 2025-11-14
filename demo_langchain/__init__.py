from typing import Optional, Literal
from pydantic import BaseModel, Field
from langchain_core.documents import Document


class VectorDocument(Document):
    """
    文档模型
    Document 包含 page_content、metadata、id
    """

    vector: Optional[list[float]] = None
    # 覆盖父类的 type，父类只支持 Document
    type: Literal["text", "image"] = "text"


if __name__ == '__main__':
    doc = VectorDocument(page_content="hello world", metadata={"source": "test.txt"}, vector=[1, 2, 3])
    print(doc.model_dump())