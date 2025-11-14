# python 基础练习
import time
from datetime import datetime
import uuid

print(datetime.now().strftime("%Y%m%d"))

print(time.time())


print(uuid.uuid4().hex)
content = "偷偷用！看看谁还在辛苦“扒录音”？最近元宝上了一款能读心的“AI录音笔“，无需购买硬件，用元宝就能清晰准确地录音转写，不仅可以实时读写还能读懂内心戏，以下这7个功能，你可别错过！1，实时转写：边录边出文字，点哪段听哪段，不落一字。2，内心OS（元宝说）：解读发言弦外之音，防跑偏、快对齐。3，AI总结：每 2 分钟自动提炼要点，会后一键生成纪要与框架。4，实时提问：不用停录，随时在对话框发问，当场搞懂。5，实时翻译：外语内容秒译为熟悉语言，双语同屏更易理解。7，分组管理：录完随手按周会/讲座等分组，查找一目了然。8，发言人区分（即将上线）：自动拆分多人发言，回看清楚是谁说了什么。你还希望元宝上线什么功能？关闭更多名称已清空微信扫一扫赞赏作者喜欢作者其它金额赞赏后展示我的头像文章暂无文章喜欢作者其它金额¥最低赞赏 ¥0确定返回其它金额更多赞赏金额¥最低赞赏 ¥01234567890.广东,2025年11月3日 17:41"

index = content.find("\n")
title = content[:index] if index != -1 else content

# 处理无中文句号的情况
if len(title) > 100:
    dot_pos = title.find("。|！|？")
    if dot_pos != -1:
        title = title[:dot_pos]

# 处理无英文句号的情况
if len(title) > 100:
    dot_en_pos = title.find(".")
    if dot_en_pos != -1:
        title = title[:dot_en_pos]

# 最终确保不超过100字符
if len(title) > 100:
    title = title[:100]
print(title)