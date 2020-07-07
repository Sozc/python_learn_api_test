# -*- coding: utf-8 -*-
# @Time    : 2020-6-15 20:15
# @Author  : Z_c
# @Email   : zc_9211@163.com
# @File    : study_requests.py
# @Software: PyCharm

import requests

"""
1、构造请求：请求方式、请求地址、请求参数
2、发起请求
3、返回响应
4、判断响应码
"""

# method = 'get'
url = 'http://baiyou-pre.api.jgcmgs.com/v1/site/login'
data = {'mobile': '18356522530', 'password': '123456'}
resp = requests.post(url, data=data)
print('响应码：', resp.status_code)
print('响应文本：', resp.text)
# print(eval(resp.text))
# print(type(eval(resp.text)))
# print('响应头：', resp.headers)
# print('响应cookies：', resp.cookies)

headers = {'Authorization':'Bearer {}'.format((eval(resp.text))['data']['access_token'])}
data_2 = {'project':1}
resp_1 = requests.get('http://baiyou-pre.api.jgcmgs.com/v1/member/permissions',data=data_2,headers=headers)
print(resp_1.text)


# url_1 = 'http://baiyou-pre.api.jgcmgs.com/v1/marketing/outpatient-type/create'
# data_1 = {'outpatient_name':'test616','project_id':'1','status':'1'}
# # headers = {'Authorization':'Bearer o9BFrvF4jnoZm6Ovif_KKiXp2f74_w50_1592269001'}
# resp_1 = requests.post(url_1,data=data_1,cookies = resp.cookies)
#
# print('响应码：', resp_1.status_code)
# print('响应文本：', resp_1.text)
# print('响应头：', resp_1.headers)
# print('响应cookies：', resp_1.cookies)

