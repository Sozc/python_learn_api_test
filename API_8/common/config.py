# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 16:54
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : config.py
# @Software: PyCharm

import configparser
from API_8.common import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file, encoding='utf-8')  # 先加载global
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contants.online_file)
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contants.test_file)

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()  # 直接实例一个对象。供后续调用

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api', 'pre_url'))
