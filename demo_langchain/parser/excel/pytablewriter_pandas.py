import pandas as pd
from pytablewriter import MarkdownTableWriter

# 读取 Excel 数据
df = pd.read_excel("demo1.xlsx")

# 初始化 Markdown 写入器
writer = MarkdownTableWriter()
writer.from_dataframe(df)  # 直接传入 DataFrame

# 输出 Markdown 表格
print(writer.dumps())