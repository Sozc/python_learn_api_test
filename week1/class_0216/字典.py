# -*- coding: utf-8 -*-
# @Time    : 2020-5-7 20:42
# @Author  : Z_c
# @Email   : zc_9211@163.com
# @File    : 字典.py
# @Software: PyCharm

# 字段 dict--->dictionary {}

# 1：空字典 d={}
# d={}
# print(type(d))

# 2：字典 key:value  键值对，不同的键值对之间用逗号隔开
# key:不可变数据类型：int、float、boolean、str、tuple    key是唯一的，不能重复的，会覆盖值
# 一般都是用字符串'' ""
# value:可以是任意类型：int、float、boolean、str、tuple、list、dict
# d={1:'我',0.02:'爱',True:'罗','age':22,(1,2,3):'tuple'}

d={"name":"柠檬班",
   "class_name":"python15",
   "score":[99,98,88],
   "height":{'sadness':180.89,'小强':183}}
# 3：字典取值：字典名[key]
# print(d["score"])
# print(d["height"])
# 4：嵌套取值，层级定位
print(d["height"]["sadness"])

# 5：字典是可变无序数据类型
d["class_name"]="柠檬班15期" #重新赋值
print(d)