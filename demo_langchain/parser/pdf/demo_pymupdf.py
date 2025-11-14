import pymupdf


class PdfParser():
    """Load pdf files.
    Args:
        file_path: Path to the file to load.
    """

    def __init__(
        self,
        file_path: str,
    ):
        """Initialize with file path."""
        self.file_path = file_path

    def parse(self) :
        """解析PDF文件为Document列表"""
        documents = []
        try:
            with pymupdf.open("/Users/marshio/Downloads/XPLORE使用手册.pdf") as docs:
                for page in docs:
                    content = page.get_text("text").strip()  # 去除空白字符
                    if not content:  # 跳过空白页
                        continue
                    print( content)
        except Exception as e:
            raise RuntimeError(f"解析PDF失败: {self.file_path}") from e

        return documents

if __name__ == '__main__':
    parser = PdfParser(file_path="")
    parser.parse()