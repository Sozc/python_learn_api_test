# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 15:15
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : test_permission.py
# @Software: PyCharm

import unittest
from API_8.common.http_request import HttpRequest, HttpRequestSession
from API_8.common import do_excel
from API_8.common import contants
from ddt import ddt, data


@ddt
class PermissionTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'permission')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequestSession()

    @data(*cases)
    def test_permission(self, case):
        global headers
        if case.title == '正常登陆':
            resp = self.http_request.request(case.method, case.url, data=case.data)
            token = resp.json()["data"]["access_token"]
            headers = {'Authorization': 'Bearer {}'.format(token)}
        else:
            resp = self.http_request.request(case.method, case.url, params=case.data, headers=headers)
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
