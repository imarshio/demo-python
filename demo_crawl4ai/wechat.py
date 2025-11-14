from playwright.sync_api import sync_playwright  # 直接从顶层导入 sync_playwright
import time


def get_wechat_article_content(url):
    with sync_playwright() as p:  # 直接使用导入的 sync_playwright
        browser = p.chromium.launch(
            headless=True,  # 无头模式
            args=[
                "--disable-gpu",
                "--no-sandbox",
            ]
        )
        # 创建上下文并禁用自动化特征
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        try:
            # 访问网页
            page.goto(url)
            # 等待数据加载完成
            # page.wait_for_load_state("load")
            # 等待标题加载（10秒超时）
            title_selector = "h1#activity-name"
            page.wait_for_selector(title_selector, timeout=10000)

            # 延迟确保内容加载
            time.sleep(2)

            # 获取数据（逻辑不变）
            title = page.locator(title_selector).text_content().strip()
            publish_time = page.locator("em#publish_time").text_content().strip()
            content = page.locator("div#js_content").text_content().strip()
            author = page.locator("a#js_name").text_content().strip()

            return {
                "title": title,
                "publish_time": publish_time,
                "content": content,
                "url": url
            }
        except Exception as e:
            print(f"爬取失败: {str(e)}")
            return None
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    article_url = "https://mp.weixin.qq.com/s/9r321s0NJ0X0TyOBE0ThIw"
    result = get_wechat_article_content(article_url)

    if result:
        print(f"标题: {result['title']}")
        print(f"发布时间: {result['publish_time']}")
        print("\n内容预览:")
        print(result['content'][:500] + "...")