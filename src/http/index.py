# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: index.py
    Time: 2021/7/15 下午4:05
-------------------------------------------------
    Change Activity: 2021/7/15 下午4:05
-------------------------------------------------
    Desc: 
"""
from src.http import BaseHandler


class Index(BaseHandler):
    def get(self, *args, **kwargs):
        return self.response(data='Hello World!')
