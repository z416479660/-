import json

import requests

headers = {"Accept": "application/json"}
data = {"username": "admin", "password": "admin"}
# 获取token的接口
res = requests.post('http://localhost:8002/api/token/', headers=headers, json=data)

# 保存token放入到后面的http请求
access = res.json()
print(type(access))
print(access.keys())
print(json.dumps(res.json()))

# 构造请求
# headers = {"Authorization": f"Bearer {access}"}
# # 查询users表的数据
# res = requests.get('http://127.0.0.1:8002/users/', headers=headers)
# print(res.json())
# # output:
# '''
# {'count': 1, 'next': None, 'previous': None, 'results': [{'url': 'http://127.0.0.1:8000/users/1/', 'username': 'admin', 'email': 'admin@example.com', 'groups': []}]}
# '''
#
# # 尝试不放入token, 直接请求
# print(requests.get('http://127.0.0.1:8000/users/'))
# # output: '{"detail":"Authentication credentials were not provided."}'