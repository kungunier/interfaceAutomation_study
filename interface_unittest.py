# 导包
import unittest
import requests

# 新建类，继承unittest.TestCase类
class TPShopLogin(unittest.TestCase):
    # setUp
    def setUp(self):
        # 获取session
        self.session = requests.session()
        # 验证码URL
        self.url_verify_code = "https://bstest.motie.cn:4433/users/captcha"
        # 登录URL
        self.url_login = "https://bstest.motie.cn:4433/users/login"

    # tearDown
    def tearDown(self):
        # 关闭会话session
        self.session.close()

    # 登录成功
    def test_login_success(self):
        # 参数
        data = {
            "username": "zhangsan",
            "password": "motie_100",
            "code": "lecf"
        }
        # 请求验证码接口
        self.session.get(self.url_verify_code)
        # 请求登录接口
        res = self.session.post(self.url_login,data=data)
        # 断言
        try:
            self.assertEqual("登录成功",res.json()['msg'])
        except AssertionError as e:
            print(e)

    # 账户名不存在
    def test_username_not_exits(self):
        # 参数
        data = {
            "username": "zhangsan11",
            "password": "motie_100",
            "code": "lecf"
        }
        # 请求验证码接口
        self.session.get(self.url_verify_code)
        # 请求登录接口
        res = self.session.post(self.url_login,data=data)
        # 断言
        try:
            self.assertEqual("用户名不存在",res.json()['msg'])
        except AssertionError as e:
            print(e)

    # 密码错误
    def test_password_error(self):
        # 参数
        data = {
            "username": "zhangsan",
            "password": "motie_10011",
            "code": "lecf"
        }
        # 请求验证码接口
        self.session.get(self.url_verify_code)
        # 请求登录接口
        res = self.session.post(self.url_login,data=data)
        # 断言
        try:
            self.assertEqual("密码错误",res.json()['msg'])
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
