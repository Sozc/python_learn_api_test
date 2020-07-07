# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 15:14
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : study_pymysql.py
# @Software: PyCharm

import pymysql

# 1、建立连接：数据库的连接信息（host、user、password、port）
host = "39.98.61.102"
user = "his_test"
password = "his123456"
port = 3306
mysql = pymysql.connect(host=host, user=user, password=password, port=port)

# 2、新建一个查询页面
cursor = mysql.cursor()
# 3、编写SQL
sql = 'select * from baiyou_pre.by_member where mobile="18356522530"'
# sql = 'select * from baiyou_pre.by_member'

# 4、执行SQL
cursor.execute(sql)

# 5、查看结果
result = cursor.fetchone()  # 获取查询结果集里面最近的一条数据返回
# result = cursor.fetchall()  # 获取全部结果集
print(type(result), result)

# 6、关闭查询
cursor.close()

# 7、关闭数据库连接
mysql.close()
