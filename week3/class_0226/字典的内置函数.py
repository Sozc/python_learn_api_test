# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 15:26
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : 字典的内置函数.py
# @Software: PyCharm

# 增删改查

# 增加和改  赋值运算
# key 要求数据类型是不可变 唯一不重复 字典取值：字典名[key]
# d = {'name': 'lemon', 'age': 22, 'score': 99.99}
# print(d['name']) #取值
# d['name']='summer' #赋值  key是唯一的
# d['sex']='男' #新增
# print(d)
# 字典名[key]=value  如果key是已经存在的，那就是修改；如果key不存在，那就是新增

# 查 取值  字典名[key]

# 删除 pop()  删除键值对
d = {'name': 'lemon', 'age': 22, 'score': 99.99}
# d.pop('age') #指定key删除
# d.popitem()#随机删除
# d.clear()#清空 -->空字典

# print(d)

# res=d.copy()  #复制
# res=d.items() #返回键值对，用元组括起来
# res=d.keys()  #获取key值
# res=d.values()  #获取value值

res=d.get('name')  #根据key取值，get里面传递的参数是key
print(res)
