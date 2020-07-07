# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 15:01
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : class_file文件操作.py
# @Software: PyCharm

# 文件的新建、读取、写入数据
# open()#新建文件的操作  .txt  .log .py .xlsx .mp4 .png
# .txt 文本文件

# file = open('..\class_0226\python15.txt',encoding='utf-8')#获取文件的操作权限，然后进行读或者写

# r   只读  如果我们要进行读或者写的文件里面有中文，那么就要设置编码为utf-8
# file = open('python15.txt',encoding='utf-8')
# # res = file.read()
# res = file.read(10)#读取的字符的长度
# print(res)
# file.close()

# r+  读写  可以进行读写操作，但是目标文件必须要存在，否则会报错
# 1）先读再写，写入的内容就写在最后面
# 2）不读直接写，从头开始写，逐字覆盖写，按字符长度覆盖
# 3）写在置顶位置 tell()（获取光标位置） seek(offset,where)（偏移光标位置） -->了解
# offset 偏移量 0 3 6 9 where 0：头部 1：当前位置 2：尾部
# file = open('python15.txt',mode='r+',encoding='utf-8')
# res = file.read()
# res = file.read(10)#读取的字符的长度
# print(res)
# file.write('double同学在不在？！')
# print(file.tell())#1个汉字--3位  数字符号英文 1位
# file.seek(0,0)
# print(file.tell())
# file.close()

#utf-8 gbk unicode ---> 3位

# w   只写 清空写 如果文件存在，清空写；如果文件不存在，新建一个文件再去写
# file = open('python15.txt','w',encoding='utf-8')
# file.write('文件存在覆盖写')
# file.close()
# file = open('python16.txt','w',encoding='utf-8')
# file.write('文件不存在，重新写')
# file.close()

# w+  读写 清空写 如果文件存在，清空写；如果文件不存在，新建一个文件再去写
# file = open('python15.txt','w+',encoding='utf-8')
# # print(file.read())#打开文件的时候就会清空，先写入，光标偏移到头部，再读
# file.write('文件存在覆盖写')
# file.seek(0,0)
# print(file.read())
# file.close()

# a   追加 不可读 如果文件存在，直接追加；如果文件不存在，新建一个文件再去写
# file = open('python17.txt','a',encoding='utf-8')
# file.write('---我是一个分割线---')
# file.close()
# file = open('python666.txt','a',encoding='utf-8')
# file.write('---文件不存在，我就会新建---')
# file.close()

# a+  读追加 可以读 如果文件存在，直接追加；如果文件不存在，新建一个文件再去写
# file = open('python17.txt','a+',encoding='utf-8')
# file.seek(0,0)#不偏移光标到头部，会读不到内容，因为默认在尾部
# print(file.read())
# file.write('---我是一个分割线---')
# file.close()
# file = open('python777.txt','a',encoding='utf-8')
# file.write('---文件不存在，我就会新建---')
# file.close()

# rb、rb+、wb、wb+、ab、ab+  #文件流的形式的时候去写入文件的时候 binary  不要求掌握