# 导包
import requests 
from pprint import pprint
import json

# URL
url = 'http://10.1.0.51:8002/query/income/charge/list'

# 请求headers
headers = {
    "Content-Type" : "application/json;charset=UTF-8",
    "x-access-token" : "3fea07eec33046da97189f72011cda57"
}

# 请求JSON
data = {
    "paging": {
        "pageNum": 1,
        "pageSize": 20
    },
    "query": {
        "comeDateBegin": "2020-08-28 00:00:00",
        "comeDateEnd": "2020-09-04 23:59:59"
    },
    "sortings": [
        {
            "asc": False,
            "field": "audit_time"
        }
    ]
}


# post请求  传json
# res = requests.post(url,json=data,headers=headers)

# post请求  传data
res = requests.post(url,data=json.dumps(data),headers=headers)

# json字符串与data字典区别，虽然长的一样，但是传入后台格式是有区别的，可以导入json包通过dumps函数将字典对象转为json字符串

# 获取响应对象
# print(res.json())
# pprint(res.json(),width=30)

# 获取响应对象 json() 与 text 区别
# json()返回的是字段，可以通过键名获取对应结果  text返回的是字符串，没有键名
res_json = res.json()
pprint(res_json)
print('res_json类型：',type(res_json))
pprint(res_json['entity']['list'])

res_text = res.text
pprint(res_text)
print('res_text类型：',type(res_text))

# 获取响应代码
print(res.status_code)


