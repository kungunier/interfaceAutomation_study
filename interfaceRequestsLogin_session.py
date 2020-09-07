# 导包
import requests

# 登录URL
url_login = 'https://bstest.motie.cn:4433/users/login'

# 验证码URL
url_verify_code = 'https://bstest.motie.cn:4433/users/captcha'

# 获取验证码cookies
session = requests.session()
res = session.get(url_verify_code)

print(res.cookies)

# 登录参数
data = {
    "username":"zhangsan",
    "password":"motie_100",
    "code":"lecf"
}

res = session.post(url=url_login,data=data)

print(res.text)