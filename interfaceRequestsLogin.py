# 导包
import requests
import json
import time

# 登录URL
url_login = 'https://bstest.motie.cn:4433/users/login'

# 时间戳
time_stamp = str(round(time.time() * 1000))
print(time_stamp)
# 验证码URL
url_verity_code = 'https://bstest.motie.cn:4433/users/captcha?' + time_stamp  # ?时间戳
print(url_verity_code)

# 获取验证码cookies
res = requests.get(url_verity_code)
# cookies = {'_captcha_pic_token':res.cookies['_captcha_pic_token']}
cookies = {'_captcha_pic_token':'cc5e531a46da407da390854a3b8f30a5'}

print('验证码cookies：',cookies)

# 登录参数
data = {
    "username":"zhangsan",
    "password":"motie_100",
    "code":"zabx"
}

res = requests.post(url=url_login,data=data,cookies=cookies)
res.encoding = "utf-8"

print(res.text)

