import requests

proxy = {
    "http": "socks5://user:pass@xx.xx.xx.xx:1080",
    "https": "socks5://user:pass@xx.xx.xx.xx:1080"
}

try:
    response = requests.get("https://httpbin.org/ip", proxies=proxy)
    data = response.json()
    origin_ip = data.get("origin")

    if origin_ip:
        print(f"检测到的IP是：{origin_ip}")
        print("这很可能是一个高匿名代理")
    else:
        print("检测结果不明确，可能是低匿名或不可用代理")

except Exception as e:
    print(f"发生错误：{e}")