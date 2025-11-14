import requests
import json


APPID = "xxx"
refresh_token = "xxxx-xxxx-xxx"


response = requests.get(f"https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={APPID}&grant_type=refresh_token&refresh_token={refresh_token}")
resp = response.json()
openid = resp.get("openid")
access_token = resp.get("access_token")


response = requests.get(f"https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}")

print(response.encoding)

print(response.json())