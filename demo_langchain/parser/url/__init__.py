import requests
from bs4 import BeautifulSoup
import re
import html2text

headers = {
   'pragma': 'no-cache',
   'priority': 'u=0, i',
   'upgrade-insecure-requests': '1',
   # 'Cookie': 'passport_web_did=7443792028678373395; passport_trace_id=7443792028682633220; QXV0aHpDb250ZXh0=6a1b5db47f9348b59ba4a012afd237cc; lang=zh; trust_browser_id=8aeffe69-cf1f-4d86-a558-83c9b470b107; __tea__ug__uid=8051101751859406263; _gcl_au=1.1.1038833402.1753692693; is_anonymous_session=; fid=1c4dc072-181c-41b9-8b24-b97e08ee6a71; i18n_locale=zh-CN; et=b338227c9f18dd10b583c913d450571a; landing_url=https://www.feishu.cn/accounts/page/ug_register?redirect_uri=https%253A%252F%252Fqcndnvg22a4q.feishu.cn%252Fwiki%252FTpWqwoOeViSdz6kUbtJcMVXLn1b&app_id=2; Hm_lvt_a79616d9322d81f12a92402ac6ae32ea=1754019342,1755052533; _uetvid=9987b1c06e8811f0a1cd1914af7c19e8; _ga=GA1.2.913314615.1733142893; _ga_VPYRHN104D=GS2.1.s1755496031$o13$g1$t1755496032$j59$l0$h0; locale=zh-CN; session=XN0YXJ0-558k88cf-ff6f-4d32-aaad-5bc2bb86b174-WVuZA; session_list=XN0YXJ0-558k88cf-ff6f-4d32-aaad-5bc2bb86b174-WVuZA_XN0YXJ0-294sdbfc-0412-40d2-bf4c-f1a026e8f006-WVuZA_XN0YXJ0-558k88cf-ff6f-4d32-aaad-5bc2bb86b174-WVuZA; help_center_session=551dae12-4341-4b63-b8a9-a0c3c70fd139; _uuid_hera_ab_path_1=7553847649045987329; _csrf_token=5709535a767cece103278721e850966b38bb0dae-1759975194; js_version=1; ccm_cdn_host=//lf-package-cn.feishucdn.com/obj/feishu-static; ssrLocalKey=cf2f637c08aa0035b6afa596d13779353dd75422585600aebcf4d68d69c9fbff; _tea_utm_cache_592346=undefined; bitable_tableId_viewId_history=%7B%22SykubPjhwaM5LpsZ2rEcCSD3nKh%22%3A%7B%22tableId%22%3A%22tblXxWbWZF325EPX%22%2C%22viewId%22%3A%22vewV0DpLue%22%7D%2C%22MXWBbW4WAaKlsws3L1xcywAQnig%22%3A%7B%22tableId%22%3A%22tbl1cM7z7XuSRPKu%22%2C%22viewId%22%3A%22vewPi9GQY4%22%7D%2C%22ON93bMSUFa4wLGsLxs8c2bprndw%22%3A%7B%22tableId%22%3A%22tblYUW2AMRWOtW3g%22%2C%22viewId%22%3A%22vewxhnhix0%22%7D%7D; passport_app_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjEwNzIzNDQsInVuaXQiOiJldV9uYyIsInJhdyI6eyJtX2FjY2Vzc19pbmZvIjp7IjIiOnsiaWF0IjoxNzYxMDI5MTQwLCJhY2Nlc3MiOnRydWV9LCIxNDMiOnsiaWF0IjoxNzYxMDI5MTQ0LCJhY2Nlc3MiOnRydWV9LCIxNiI6eyJpYXQiOjE3NjEwMjkxNDIsImFjY2VzcyI6dHJ1ZX0sIjEwMCI6eyJpYXQiOjE3NjEwMjkxNDQsImFjY2VzcyI6dHJ1ZX0sIjI5Ijp7ImlhdCI6MTc2MTAyOTE0MywiYWNjZXNzIjp0cnVlfSwiMTQxIjp7ImlhdCI6MTc2MTAyOTE0MywiYWNjZXNzIjp0cnVlfX0sInN1bSI6IjgyYmNlZjdjMzg0ZTNkZmExZjI3ZWEzYWVkMmZlZWZmZDdmZTU5NDJjM2RkMTAwNjM0NTAyNWM2YWI2ZmVlYzMifX0.5OqqgyG40rKlE49zrCTr8VHNic8W0SmA0AfGxE3OFMoTaU3j5stkJSxjxa8HVC3J21OpGhRK6eUAbHeAbenusQ; sl_session=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjEwNzQ5NzksInVuaXQiOiJldV9uYyIsInJhdyI6eyJtZXRhIjoiQVdpSFFSOEhsTUFUYUljN3E5M3p3Qk5uVGFscFEwSkFFMmROcVdsRFFrQVRhSWRDVGhMOGdCTUNLZ0VBUVVGQlFVRkJRVUZCUVVKdmFEQktUMGgzWWtGQ1FUMDkiLCJpZGMiOlsxLDJdLCJzdW0iOiI4MmJjZWY3YzM4NGUzZGZhMWYyN2VhM2FlZDJmZWVmZmQ3ZmU1OTQyYzNkZDEwMDYzNDUwMjVjNmFiNmZlZWMzIiwibG9jIjoiemhfY24iLCJhcGMiOiIiLCJpYXQiOjE3NjEwMzE3NzksInNhYyI6eyJVc2VyU3RhZmZTdGF0dXMiOiIxIiwiVXNlclR5cGUiOiI0MiJ9LCJsb2QiOm51bGwsIm5zIjoibGFyayIsIm5zX3VpZCI6Ijc1MzIwNjA1MDMzMjc0MjQ1MzEiLCJuc190aWQiOiI3NTMyMDU0NTExMTQ5NjI5NDU5Iiwib3QiOjMsImN0IjoxNzUzNjk0Nzk4LCJydCI6MTc2MTAxNDIxOX19.0KLc_vupXNHIly6kwV9zyCb62nhlQfcvRog48aDG6uKXkaYhZBApkXKKjqZ32lBPSCXRypTeNFVpaTF6WKmlLw; swp_csrf_token=648a7920-0755-4d5f-b842-8e47ffe412f0; t_beda37=0ddcdfca7dbc9eb82128f58bc2eba65ae976544d66e764e2bd9a02180d7f7f94',
   'Connection': 'keep-alive'
}

# path = "https://qcndnvg22a4q.feishu.cn/wiki/VJKMw1ZHnisH44kllrzcCMZCnEe?from=from_copylink"
path = "https://mp.weixin.qq.com/s/lLrmJERG2lqPmk-S4VAwXw"
# path = "https://36kr.com/p/3518738339011715"

response = requests.get(path, headers=headers, data={})

response.raise_for_status()  # 检查请求是否成功
response.encoding = response.apparent_encoding  # 自动处理编码

# print(response.text)

print("="*20)
converter = html2text.HTML2Text()
markdown = converter.handle(response.text)

print(markdown)
#
# # 用 BeautifulSoup 解析 HTML
# soup = BeautifulSoup(response.text, 'lxml')
#
# # 去除所有 HTML 标签，获取纯文本
# raw_text = soup.get_text()
#
# # 清洗文本：去除多余空行、空格和特殊字符
# # 1. 用正则替换多个换行/空格为单个换行
# clean_text = re.sub(r'\s+', '\n', raw_text).strip()
#
# # return clean_text
#
# # print(clean_text)
#
# # 定位主要内容区域（飞书文档通常在特定容器内）
# content = soup.body
#
# # 移除脚本、样式标签
# for tag in soup(["script", "style", "nav", "footer"]):
#     tag.decompose()
#
# # 处理文本格式的函数
# def format_element(element):
#     text_parts = []
#     for child in element.children:
#         # 处理标签节点
#         if child.name:
#             # 标题标签（h1-h6）
#             if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
#                 level = int(child.name[1])
#                 text = format_element(child).strip()
#                 if text:
#                     text_parts.append(f"\n{'#' * level} {text}\n")
#
#             # 段落标签
#             elif child.name == 'p':
#                 text = format_element(child).strip()
#                 if text:
#                     text_parts.append(f"{text}\n")
#
#             # 列表标签
#             elif child.name in ['ul', 'ol']:
#                 # 列表项处理
#                 for li in child.find_all('li', recursive=False):
#                     marker = '- ' if child.name == 'ul' else '1. '
#                     li_text = format_element(li).strip()
#                     if li_text:
#                         text_parts.append(f"  {marker}{li_text}\n")
#                 text_parts.append("\n")  # 列表结束后加空行
#
#             # 表格标签
#             elif child.name == 'table':
#                 # 简单处理表格（按行输出）
#                 text_parts.append("\n[表格开始]\n")
#                 for row in child.find_all('tr'):
#                     cells = [format_element(cell).strip() for cell in row.find_all(['th', 'td'])]
#                     text_parts.append("  | ".join(cells) + "\n")
#                 text_parts.append("[表格结束]\n\n")
#
#             # 换行标签
#             elif child.name == 'br':
#                 text_parts.append("\n")
#
#             # 其他标签递归处理
#             else:
#                 text_parts.append(format_element(child))
#
#         # 处理文本节点
#         else:
#             text = str(child).strip()
#             if text:
#                 text_parts.append(text)
#
#     return ''.join(text_parts)
#
#
# # 生成格式化文本
# formatted_text = format_element(content)
#
# # 清理多余空行（保留合理的段落分隔）
# # formatted_text = re.sub(r'\n{3,}', '\n\n', formatted_text).strip()
#
# print(formatted_text)