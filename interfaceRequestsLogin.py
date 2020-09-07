# 导包
import requests
import json

# 登录URL
url_login = 'https://bstest.motie.cn:4433/users/login'

# 验证码URL
url_verity_code = 'https://bstest.motie.cn:4433/users/captcha'

# 获取验证码cookies
res = requests.get(url_verity_code)
cookies = {'_captcha_pic_token':res.cookies['_captcha_pic_token']}

print('验证码cookies：',cookies)

# 登录参数
data = {
    "username":"zhangsan",
    "password":"motie_100",
    "code":"lecf"
}

res = requests.post(url=url_login,data=data,cookies=cookies)
res.encoding = "utf-8"

print(res.text)

