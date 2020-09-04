# 导包
import requests

# URL
url = 'http://www.baidu.com'

# get请求
res = requests.get(url)

print(res.text)

# 响应对象方法：status_code 获取响应状态码
print(res.status_code)

# 响应对象方法：url 获取请求url地址
print(res.url)

# 响应对象方法：encoding
#   1、获取默认请求编码格式
#   2、设置响应编码格式
print(res.encoding)
res.encoding = "UTF-8"
print(res.text)


# 响应对象方法：headers 获取响应对象头信息
print(res.headers)


# 响应对象方法：cookies 获取响应cookies信息
print(res.cookies)
# 通过键名获取cookies值
print(res.cookies['BDORZ'])

# 响应对象方法：content 以字节码形式获取响应信息（图片、视频。。多媒体格式）
url_img = 'https://www.baidu.com/img/bd_logo1.png?where=super'
res2 = requests.get(url_img)

# 响应对象方法：text 以文本形式获取响应信息
print(res2.text)    #乱码
print(res2.content) #字节码

# 讲图片写入当前目录
with open("./baidu.png","wb") as f:
    f.write(res2.content)


# 响应对象方法：json() 以字典形式获取响应信息
