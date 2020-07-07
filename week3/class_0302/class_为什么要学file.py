# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:11
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : class_为什么要学file.py
# @Software: PyCharm

def add(a, b):
    print(a + b)
    return a + b

# file = open('test.txt', 'r')
## res= file.readline() #读取一行内容，返回字符串形式的数据
# resp = file.readlines()  # 读取所有行，以列表的形式返回，每一行数据是列表一个字符串元素
# print(resp)
# print(type(resp))
# file.close()

# for item in resp:
    # str=item.strip('\n')#以\n进行分割，返回移除字符串头尾指定的字符生成的新字符串
    # print(str)
    # print(type(str))
    # data = str.split(',')#以,进行分割，返回分割后的字符串列表。
    # print(data)
    # print(type(data))
    # add(int(data[0]),int(data[1]))

import requests

file = open('baidu.txt','w',encoding='utf-8')
resp = requests.get('http://www.baidu.com')
file.write(resp.text)
file.close()

# 1:存储测试数据
# 2：可以写入我们的结果
# 3：写日志 logging