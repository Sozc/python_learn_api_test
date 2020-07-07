# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 13:52
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : logger.py
# @Software: PyCharm

import logging
from API_8.common.config import config
from API_8.common import contants

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt = logging.Formatter('[line:%(lineno)d]%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

    console_handler = logging.StreamHandler()  # 控制台
    # 把日志级别放到配置文件里面配置
    console_level = config.get('loglevel', 'console_level')
    # print(console_level)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(fmt)

    file_hadler = logging.FileHandler(contants.log_dir+'/case.log', encoding='utf-8')
    # 把日志级别放到配置文件里面配置
    file_level = config.get('loglevel', 'file_level')
    # print(file_level)
    file_hadler.setLevel(file_level)
    file_hadler.setFormatter(fmt)

    logger.addHandler(console_handler)
    logger.addHandler(file_hadler)
    return logger


if __name__ == '__main__':
    logger = get_logger('case')
    logger.info('测试开始')
    logger.error('测试报错')
    logger.debug('测试数据')
    logger.info('测试结束')
