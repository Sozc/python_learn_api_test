# -*- coding: utf-8 -*-
# @Time    : 2020-5-6 21:23
# @Author  : Z_c
# @Email   : zc_9211@163.com
# @File    : 格式化输出.py
# @Software: PyCharm

# 格式化输出   .py用中文命名不合理
name = '呵呵'
age = 18
sex = 1  #0:女生  1：男生
salary = '10k' #str、int、float
hobby = '篮球'
height = 180.35 #float

# '+'：字符串之间的拼接，只能针对同类型的数据，非同类型的会报错 str(数字)--->字符串
# print('Python15期有一个学生名字叫：'+name+'，他的薪资是：'+salary+'，她今年'+str(age)+'岁')
# print('Python15期有一个学生名字叫：'+name+'，他的薪资是：'+salary+'，她今年',age,'岁')
#
# print(1,2,3)#内置函数 *args--->arguments--->参数们 可以输入任意多个参数，用逗号隔开

# 第一种格式化输出 %s（字符串）、%d（数字）、%f（浮点数）  占坑，按顺序赋值
# %s是万能的，啥都可以接；数字类型：%d %f %s 其他类型，必须用%s
# print('Python15期有一个学生名字叫:%s,他的薪资是:%s,他今年%d岁,他的身高是%.2f'%(name,salary,age,height))

# 第二种格式化输出  {}.format  推荐使用
print('Python15期有一个学生名字叫:{},他的薪资是:{},他今年{}岁,他的身高是{}'.format(name,salary,age,height))
# 1）不标序号，按顺序赋值 2）标序号，按序号给值（值参照索引）
# print('Python15期有一个学生名字叫:{1},他的薪资是:{1},他今年{1}岁,他的身高是{1}'.format(name,salary,age,height))

print('''------student's info------
      Python15期有一个学生名字叫:{}
      他的薪资是:{}
      他今年{}岁
      他的身高是{}'''.format(name,salary,age,height))
