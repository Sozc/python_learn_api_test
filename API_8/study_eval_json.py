# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 16:43
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : study_eval_json.py
# @Software: PyCharm


# 数据类型的转换  str-->dict
# json序列化与反序列化
# 1、序列化---将dict序列化为str或file
# dumps(),dump()
# 2、反序列化---将str或file反序列化为dict
# loads(),load()

import json
# 正常的json格式  (所有的字符串都必须用双引号，单引号不识别)
# {"key":[]}

params = '{"code":200,"message":"OK","data":{"access_token":"rkfHwFqrXKaKclGYR8tPE1Hk7ODli1L6_1592551854","info":{"member_id":2,"username":"赵璀","realname":"赵璀","email":"","mobile":"18356522530","is_super":1,"project_id":0,"head_img_url":"http://baiyou-pre.api.jgcmgs.com/attachment/images/2020/04/11/image_158656999357531025.jpg","is_bind_dingtalk":0}}}'

# json.loads()
# d=eval(params)  # 根据python的数据类型来做转换
# print(d['data']) # NameError: name 'null' is not defined

d=json.loads(params)
print(d['data']['access_token'])