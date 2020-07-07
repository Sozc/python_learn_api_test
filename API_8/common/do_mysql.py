# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 15:54
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : do_mysql.py
# @Software: PyCharm

import pymysql
from API_8.common.config import config


class DoMysql:
    """
    完成与MySql数据库的一个交互
    """

    def __init__(self):
        self.host = eval(config.get('mysql', 'host'))
        # print(type(self.host),self.host)
        self.user = eval(config.get('mysql', 'user'))
        # print(type(self.user),self.user)
        self.password = eval(config.get('mysql', 'password'))
        # print(type(self.password),self.password)
        self.port = int(config.get('mysql', 'port'))
        # print(type(self.port),self.port)
        self.mysql = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port)
        # print(self.mysql)
        self.cursor = self.mysql.cursor()
        # 创建连接


    def fetch_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接


if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one('select mobile from baiyou_pre.by_member where mobile="18356522530"')
    print(result)
    mysql.close()
