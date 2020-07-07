# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 15:33
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : context.py
# @Software: PyCharm

import re
from API_8.common.config import config
from configparser import NoOptionError


def replace(data):
    p = "#(.*?)#"
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找到第一个就返回
        g = m.group(1)  # 拿到参数化的KEY
        v = config.get('data', g)  # 根据KEY取配置文件里面的值
        # print(v)
        # 记得替换后的内容，继续用data接受
        data = re.sub(p, v, data, count=1)
    return data
