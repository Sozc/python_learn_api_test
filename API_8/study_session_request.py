# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 15:26
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : study_session_request.py
# @Software: PyCharm

import requests
"""
两种传递cookie的方式
1、单独的session，把上一个请求的返回cookie，指定传递到下一个请求的入参cookie当中
2、使用同一个session，就会自动传递cookie
"""

method = 'post'
url = 'http://baiyou-pre.api.jgcmgs.com/v1/site/login'
data = {'mobile': '18356522530', 'password': '123456'}

session = requests.sessions.session()
# 登录
resp = session.request(method, url, data=data)
print(resp.text)
# 权限
method_1 = 'get'
url_1 = 'http://baiyou-pre.api.jgcmgs.com/v1/member/permissions'
# headers = {'Authorization': 'Bearer {}'.format((eval(resp.text))['data']['access_token'])}
params = {'project': 1}

resp_1 = session.request(method_1, url_1, params=params)
print(resp_1.text)

session.close()  #session关闭