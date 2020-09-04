import requests

url = 'http://www.baidu.com'

# 第一种传参方式：
# params = {"id" : 1001}

# 第二种传参方式：
# params = {"id" : "1001,1002"}   # %2C 是ASCI值中逗号

# 第三种传参方式：
params = {"id" : 1001,"kw" : "北京"}

# res = requests.get(url,params='id=1001')  # 用字符串传参不推荐
res = requests.get(url,params=params)

print(res.url)
print(res.status_code)
print(res.text)