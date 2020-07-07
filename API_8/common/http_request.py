# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 16:53
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : http_request.py
# @Software: PyCharm

import requests
from API_8.common.config import config
from API_8.common import logger

logger = logger.get_logger(__name__)


class HttpRequest:
    """
    使用这个类的request方法去完成不同的http请求，并且返回响应结果
    """

    def request(self, method, url, params=None, data=None, json=None, cookies=None, headers=None):
        if type(data) == str:
            data = eval(data)

        # 拼接请求的url
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url：{}'.format(url))
        logger.debug('请求的data：{}'.format(data))

        if method.lower() == 'get':
            resp = requests.get(url, params=params, cookies=cookies, headers=headers)  # resp是Response对象
        elif method.lower() == 'post':
            if json:  # 如果json传参不为空
                resp = requests.post(url, json=json, cookies=cookies, headers=headers)
            else:
                resp = requests.post(url, data=data, cookies=cookies, headers=headers)
        else:
            logger.error('UN-support method')
        logger.debug('请求response：{}'.format(resp.text))
        return resp


class HttpRequestSession:
    """
        使用这个类的request方法去完成不同的http请求，并且返回响应结果
    """

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, params=None, data=None, json=None, headers=None):
        if type(data) == str:
            data = eval(data)

        # 拼接请求的url
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url：{}'.format(url))
        logger.debug('请求的data：{}'.format(data))

        if method.lower() == 'get':
            resp = self.session.request(method, url, params=params, headers=headers)
        elif method.lower() == 'post':
            if json:
                resp = self.session.request(method, url, json=json, headers=headers)
            else:
                resp = self.session.request(method, url, data=data, headers=headers)
        else:
            resp = None
            logger.error('UN-support method')
        logger.debug('请求response：{}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()


if __name__ == '__main__':
    method = 'post'
    url = 'http://baiyou-pre.api.jgcmgs.com/v1/site/login'
    data = {'mobile': '18356522530', 'password': '123456'}
    resp = HttpRequest().request(method, url, data=data)
    print(resp.text)

    # method_1 = 'get'
    # url_1 = 'http://baiyou-pre.api.jgcmgs.com/v1/member/permissions'
    # headers = {'Authorization': 'Bearer {}'.format((eval(resp.text))['data']['access_token'])}
    # params = {'project': 1}
    # resp_1 = HttpRequest().request(method_1, url_1, params=params, headers=headers)
    # print(resp_1.text)
