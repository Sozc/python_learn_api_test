# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 14:23
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : class知识补充.py
# @Software: PyCharm

# 1：变量的范围  2：import 和 main

# from week3.class_0302.robot import robot
# robot('小蚂蚁','今天一起去shopping吗？')

# language='java'  #全局变量  函数外面的叫做全局变量

def coding():
    global language #声明这个language是个全局变量
    language = 'python'  # 局部变量  函数里面的叫做局部变量，只能在当前函数内部生效
    print('我喜欢的代码是：{}'.format(language))

# coding()

def automation_testing(type):
    print('{}测试，用{}代码比较适合公司的框架'.format(type, language))

coding()
automation_testing('app')

# 全局变量和局部变量同名的话：
# 1：如果全局变量和局部变量同时存在的话，那么函数优先调用自己局部变量
# 2：如果不存在局部变量，那么函数就调用全局变量
# 3：global 变量名  声明是一个全局变量
