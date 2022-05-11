# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: __init__.py.py
    Time: 2021/7/13 下午11:10
-------------------------------------------------
    Change Activity: 2021/7/13 下午11:10
-------------------------------------------------
    Desc: 
"""
import time
import json
import hashlib

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """解决跨域请求问题"""

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

        # 打开长连接，server，不会自动 关闭连接
        self._auto_finish = False

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, token, Access-Control-Allow-Origin, Access-Control-Allow-Headers, '
                        'X-Requested-By, Access-Control-Allow-Methods')

    def response(self, data, code=200):
        result = {
            'data': data,
            'code': code,
            'desc': '成功' if code == 200 else '失败'
        }

        self.finish(json.dumps(result, ensure_ascii=False))

    @staticmethod
    def random_process_id(string):
        new_string = f'{string}{str(time.time_ns())}'
        new_md5 = hashlib.md5()
        new_md5.update(new_string.encode(encoding='utf-8'))
        return new_md5.hexdigest()
