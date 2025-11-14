import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag


logger = logging.getLogger(__name__)


@dataclass
class Chunk:
    text: str
    html: str
    sheet_name: str


@dataclass
class DolingExtractResult:
    sheet_name: str
    page_no: int
    html_content: str
    md_content: str


class HtmlExcelParser():
    """Load Excel files.


    Args:
        file_path: Path to the file to load.
    """

    # 类变量，用于存储导入的类型引用
    DocumentConverter: type[Any] | None = None
    DocItem: type[Any] | None = None
    GroupItem: type[Any] | None = None
    ImageRefMode: type[Any] | None = None

    def __init__(self, file_path: str, max_workers: int = 5, **kwargs):
        """Initialize with file path."""
        from docling.document_converter import DocumentConverter  # noqa
        from docling_core.types.doc import DocItem, GroupItem  # noqa
        from docling_core.types.doc.document import ImageRefMode  # noqa

        # 将导入的类型保存到类变量中
        HtmlExcelParser.DocumentConverter = DocumentConverter
        HtmlExcelParser.DocItem = DocItem
        HtmlExcelParser.GroupItem = GroupItem
        HtmlExcelParser.ImageRefMode = ImageRefMode

        self._file_path = file_path
        self.converter = DocumentConverter()
        self.max_workers = max_workers
        self.document_name = kwargs.get("document_name", "default_document_name")

    def parse(self):
        document_list = []

        conv_res = self.converter.convert(Path(self._file_path))
        doc = conv_res.document
        sheet_info_list: list[DolingExtractResult] = self._get_sheet_info_map(doc)

        for sheet_info in sheet_info_list:
            html_content = strip_html_styles(sheet_info.html_content)
            print(html_content)

        return document_list

    def _get_sheet_info_map(self, doc) -> list[DolingExtractResult]:
        sheet_info_list: list[DolingExtractResult] = []

        if doc.body:
            for group_ref in doc.body.children:
                group_item = group_ref.resolve(doc)
                if (
                    isinstance(group_item, HtmlExcelParser.GroupItem)
                    and group_item.name
                    and group_item.name.startswith("sheet: ")
                ):
                    # MsExcelDocumentBackend 将工作表组命名为 "sheet: {实际工作表名}"
                    parsed_sheet_name = group_item.name.split("sheet: ", 1)[1]

                    # 查找此工作表组对应的页码
                    # 通常，工作表组的直接子项或孙子项的 ProvenanceItem 会包含 page_no
                    page_no_for_group = None

                    # 使用广度优先搜索（BFS）查找第一项的 ProvenanceItem 会包含 page_no
                    queue = list(group_item.children)
                    visited_refs = {group_item.self_ref}  # 防止循环（尽管在Excel结构中不太可能）

                    while queue:
                        current_ref = queue.pop(0)
                        if current_ref.cref in visited_refs:
                            continue
                        visited_refs.add(current_ref.cref)

                        current_item = current_ref.resolve(doc)
                        if isinstance(current_item, HtmlExcelParser.DocItem) and current_item.prov:
                            page_no_for_group = current_item.prov[0].page_no
                            break
                        elif isinstance(current_item, HtmlExcelParser.GroupItem):
                            # 如果子项也是组，将其子项加入队列
                            queue.extend(current_item.children)

                    if page_no_for_group is not None:
                        html_content = doc.export_to_html(
                            page_no=page_no_for_group,
                            image_mode=HtmlExcelParser.ImageRefMode.PLACEHOLDER,
                        )
                        md_content = doc.export_to_markdown(
                            page_no=page_no_for_group,
                            image_mode=HtmlExcelParser.ImageRefMode.PLACEHOLDER,
                        )
                        sheet_info_list.append(
                            DolingExtractResult(
                                sheet_name=parsed_sheet_name,
                                page_no=page_no_for_group,
                                html_content=html_content,
                                md_content=md_content,
                            )
                        )

        return sheet_info_list


def strip_html_styles(html_content: str) -> str:
    """
    Removes styling elements (style tags, style attributes, class attributes)
    from an HTML string, preserving the core content and structure.

    Args:
        html_content: The input HTML string.

    Returns:
        A new HTML string with styles removed.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Remove all <style> tags
    for style_tag in soup.find_all("style"):
        style_tag.decompose()  # .decompose() removes the tag and its contents

    # 2. Remove 'style' and 'class' attributes from all tags
    # Iterate through all tags found in the soup
    for tag in soup.find_all(True):  # True matches all tags
        if isinstance(tag, Tag):  # Ensure it's a tag object
            if "style" in tag.attrs:
                del tag["style"]
            if "class" in tag.attrs:
                del tag["class"]

    # 3. Optionally, remove specific meta tags that are not core content
    # For example, the generator meta tag
    generator_meta = soup.find("meta", {"name": "generator"})
    if generator_meta:
        generator_meta.decompose()

    # Return the cleaned HTML string
    # .prettify() formats the output nicely, but you can also use str(soup)
    return soup.prettify()




if __name__ == '__main__':
    parser = HtmlExcelParser("demo1.xlsx")
    parser.parse()