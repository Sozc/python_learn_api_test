# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 16:16
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : task.py
# @Software: PyCharm

# 等边三角形
# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("* ", end="")
#     print("")

# 9*9乘法表
# for i in range(1, 10):
#     print()
#     for j in range(1, 1 + i):
#         print('{}*{}={}'.format(j, i, j * i),' ',end='')

# 冒泡算法
# s=[1,6,5,23,17,55,45]
# for i in range(len(s)-1):#控制循环次数  n-1次循环
# 下面的for循环作用是完成每一次相邻两个数据的比较并且完成数值的交换'''
#     for j in range(len(s)-1):
#         if s[j]>s[j+1]:
#             s[j],s[j+1]=s[j+1],s[j]
# print(s)

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 print(i, j, k)

# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)

# a = 2
# b = 4
# a, b = b, a  # python 支持这样的用法  交换值

# a, b = 1, 2  # 连续赋值的用法
# print(a, b)
