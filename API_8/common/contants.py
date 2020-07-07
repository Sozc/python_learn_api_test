# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 17:30
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : contans.py
# @Software: PyCharm

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3,从当前模块定位，一层一层文件夹往上找
# print(base_dir)

case_file = os.path.join(base_dir, 'data', 'case.xlsx')
# print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)

log_dir = os.path.join(base_dir, 'log')

case_dir = os.path.join(base_dir, 'testcases')

report_dir = os.path.join(base_dir, 'reports')
