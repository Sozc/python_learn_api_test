# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 11:06
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : test_login.py
# @Software: PyCharm

import unittest
from API_8.common.http_request import HttpRequest, HttpRequestSession
from API_8.common import do_excel
from API_8.common import contants
from ddt import ddt, data
from API_8.common import logger

logger = logger.get_logger(__name__)  #__name__  这个文件名

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequestSession()

    @data(*cases)
    def test_login(self,case):
        logger.info('开始测试：{}'.format(case.title))
        resp = self.http_request.request(case.method, case.url, data=case.data)
        actual = resp.json()["message"]
        try:
            self.assertEqual(case.expected, actual)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FAIL")
            logger.error('测试报错了：{}'.format(e))
            raise e
        logger.info('结束测试：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
