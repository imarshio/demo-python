from pathlib import Path
from docling.document_converter import DocumentConverter

# Change this to a local path or another URL if desired.
# Note: using the default URL requires network access; if offline, provide a
# local file path (e.g., Path("/path/to/file.pdf")).
source = "https://arxiv.org/pdf/2408.09869"
# source = Path("/Users/marshio/Downloads/asr 结果.pdf")

converter = DocumentConverter()
result = converter.convert(source)

# Print Markdown to stdout.
print(result.document.export_to_markdown())