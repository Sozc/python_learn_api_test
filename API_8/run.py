# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 16:46
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : run.py.py
# @Software: PyCharm

import sys
sys.path.append('./') # project根目录

import unittest
from API_8.testcases import test_login
from API_8.testcases import test_permission
import HTMLTestRunnerNew
from API_8.common import contants

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_permission_new))

discover = unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

with open(contants.report_dir+'/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title = 'PYTHON15 API TEST REPORT',
                                              description='baiyou',
                                              tester='zc')
    # runner.run(suite)
    runner.run(discover)
