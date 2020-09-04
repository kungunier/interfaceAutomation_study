import requests

# 请求接口
url = 'http://www.baidu.com'
res = requests.get(url)

# 获取请求地址
print('请求地址为：',res.url)
# 获取响应状态码
print('响应状态码：',res.status_code)
# 获取响应内容
print("内容：",res.text)


