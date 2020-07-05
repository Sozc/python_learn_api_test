# -*- coding: utf-8 -*-
# @Time    : 2020-5-7 20:17
# @Author  : Z_c
# @Email   : zc_9211@163.com
# @File    : 元组.py
# @Software: PyCharm

# 元组 tuple()

# 1：空元祖 t=()
# 2：元组里面只有一个数据，要加一个逗号，才会是元组类型  t=('hello',)
# t = (1,)
# print(type(t))
# 3：元组里面的数据可以是任意类型,不同的元素之间用逗号隔开
# t = (1, 0.02, 'hello', True, (1, 2, 3))
# 4：是有下标（索引），正序/反序编号都支持，取值方式同字符串
t = (1, 0.02, 'hello', True, (1, 2, 3, 666,'python'))
# 单个取值:元组名[索引值]
print(t[2])  # 取'hello'
# 切片：元组名[索引头:索引尾:步长] 步长默认为1
# 倒序输出元组里面的每一个元素
print(t[::-1])
# 嵌套取值：元组里面还有元组
print(t[-1][-2])  #取666
# 取值python里的y
print(t[-1][-1][1])

# 5：元组是不可变类型，有序
# t[0]='hehe' # TypeError: 'tuple' object does not support item assignment