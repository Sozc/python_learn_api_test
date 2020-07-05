# -*- coding: utf-8 -*-
# @Time    : 2020-5-7 20:30
# @Author  : Z_c
# @Email   : zc_9211@163.com
# @File    : 列表.py
# @Software: PyCharm

# 列表 list[]

# 1：空列表 t=()
# 2：列表里面的元素可以是任意类型，不同的元素之间用逗号隔开
L = [1, 0.02, 'hello', True, (1, 2, 3, 666, 'python'), ['python', 'java', 'ruby']]
#    0    1     2        3               4                          5    正序
#   -6   -5    -4       -3              -2                         -1    反序
# 3：是有索引  index 正序/反序编号都支持，取值方式同字符串
# 单个取值:列表名[索引值]
print(L[2])  # 取'hello'
# 切片：列表名[索引头:索引尾:步长] 步长默认为1
# 倒序输出列表里面的每一个元素
print(L[::-1])
print(L[-1][-2][::-1])   #拿到java，在反序输出成avaj
# 嵌套取值：元组里面还有元组
print(L[-1][-2])  # 取java

# 4：列表是有序可变类型
L[2]='你好'
print(L)

# 列表和元组，并不是绝对的不能修改，要看最后定位的是列表还是元组
# t = (1, 0.02, 'hello', True, (1, 2, 3, 666,'python'))
# N = [1, 0.02, 'hello', True, (1, 2, 3, 666, 'python'), ['python', 'java', 'ruby']]