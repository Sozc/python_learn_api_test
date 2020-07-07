# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 14:24
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : robot.py
# @Software: PyCharm

def robot(name,msg):
    print('{}你有一条信息：{}'.format(name,msg))

# 测试代码
if __name__ == '__main__':#代码执行的主入口
    robot('001','今天一起吃晚饭吗？')

