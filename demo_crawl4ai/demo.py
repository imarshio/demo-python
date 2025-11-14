import asyncio
from crawl4ai import *
# downloaded to /Users/marshio/Library/Caches/ms-playwright
async def main():
    async with AsyncWebCrawler() as crawler:
        # url = "https://www.nbcnews.com/business"
        # url = "https://mp.weixin.qq.com/s/9r321s0NJ0X0TyOBE0ThIw"
        url = "https://qcndnvg22a4q.feishu.cn/wiki/R6tzw7fFwiq7rgkA1IocqGQXnhc?from=from_copylink"
        # url = "https://news.qq.com/rain/a/20251103A03MQ400?shareto=moments&devid=CED81F77-B201-4072-9D7D-AAA582B046BA&qimei=3ba4f0a7-b87c-4c15-b9a3-a16a0107520b&uid=102376183375&qs_signature=0002015504030f7ca7a2bbb6000e253e537899dab72e9fd90111dbc729f793e038e1bb8a1d6f456500ed6cc60000000000000000&appver=18.6.2_qqnews_7.8.01&share_pos=4&QIMEI36=fakeced81f77b20140729d7daaa582b046ba&suid=&media_id="
        result = await crawler.arun(
            url=url,
        )
        with open("result.md", "w") as f:
            f.write(result.markdown)
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())