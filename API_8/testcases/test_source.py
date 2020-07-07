# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 10:29
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : test_source.py
# @Software: PyCharm

import unittest
from API_8.common.http_request import HttpRequest, HttpRequestSession
from API_8.common import do_excel
from API_8.common import contants
from ddt import ddt, data
from API_8.common import context
from API_8.common.config import config


@ddt
class SourceTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'source')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequestSession()
        # cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_source(self, case):
        global headers
        # case.data = eval(case.data)  # 变成字典
        # if 'mobile' in case.data and case.data['mobile'] == 'normal_user':
        #     case.data['mobile'] = config.get('data', 'normal_user') #拿到配置文件里的值赋给mobile
        # if 'password' in case.data and case.data['password'] == 'normal_pwd':
        #     case.data['password'] = config.get('data', 'normal_pwd')
        # if 'project' in case.data and case.data['project'] == 'normal_project':
        #     case.data['project'] = config.get('data', 'normal_project')

        # 在请求之前，替换参数化的值
        case.data = context.replace(case.data)

        if case.title == '正常登陆':
            resp = self.http_request.request(case.method, case.url, data=case.data)
            token = resp.json()["data"]["access_token"]
            headers = {'Authorization': 'Bearer {}'.format(token)}
        else:
            resp = self.http_request.request(case.method, case.url, data=case.data, headers=headers)
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
        # cls.mysql.close()
