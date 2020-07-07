# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 15:55
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : 列表内置函数.py
# @Software: PyCharm

# 增删改查
# L = [0.02, 100, 'hello', (1, 2, 3), ['python', 0.02]]

# 增加：
# 1)两个列表相加，两个列表的元素，会合成到一个列表里
# s = [4, 5, 6]
# L=L+s
# print(L)

# 2）append() 给列表里面增加元素，增加在最后面
# L.append([4,5,6]) #每一次只能加一个元素
# print(L)

# 3）insert() 给列表里面增加元素，可以增加在指定位置
# L.insert(0,'柠檬')
# print(L)

# 4）exteng() 拓展列表  效果与+（方法1）等效
# s = [6, 66, 666]
# L.extend(s)
# print(L)

# 改
# L = [0.02, 100, 'hello', (1, 2, 3), ['python', 0.02]]
# L[0]='hh' #赋值运算，赋值到某个索引位置
# print(L)

# 删除
# L = [0.02, 100, 'hello', (1, 2, 3), ['python', 0.02],0.02]
# 1）pop()，默认删除最后一个元素  指定索引，就删除指定位置的值，会有返回值
# res = L.pop(1)
# print(L)
# print('被删除的元素：', res)

# 2）del 直接从内存中删除，不建议使用
# del L
# print(L)

# 3）clear()  清空的操作
# L.clear()
# print(L)

# 4）remove() 删除指定的值，删除第一个符合的值
# L.remove(0.02)
# print(L)

# 查：利用索引取值，以及切片取值


# range函数：
# range(m,n,k)#生成指定范围的整数序列
# 和切片很相似
# m:索引头  n:索引尾   k:步长  k默认值为1
# 传一个参数，默认索引头为0，从0开始
# res=list(range(1,6,2))
# print(res)

# res=list(range(10))
# print(res)

# L = [0.02, 100, 'hello', (1, 2, 3), ['python', 0.02],0.02]
# for item in L:
#     print(item)

# 正序
# for i in range(len(L)):#range(4)-->range(0,4,1)-->0  1  2  3
#     print(L[i])

# 倒序
# for i in range(len(L)-1,-1,-1):#range(3,-1,-1)-->3  2  1  0
#     print(L[i])

# L.reverse()#列表翻转
# print(L)

# s = [1, 22, 16, 37, 4, 6, 57]
# s.sort()  # 针对数字类型的排序
# print(s)
