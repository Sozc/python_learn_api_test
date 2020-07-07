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
from API_8.common import do_mysql


@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'public')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequestSession()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_login(self, case):
        if case.data.find('login_mobile'):
            sql = 'select mobile from baiyou_pre.by_member where mobile="18356522530"'
            mobile = self.mysql.fetch_one(sql)[0]
            case.data = case.data.replace('login_mobile', mobile)

        resp = self.http_request.request(case.method, case.url, data=case.data)
        actual = resp.json()["message"]
        try:
            self.assertEqual(case.expected, actual)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
