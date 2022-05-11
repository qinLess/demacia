# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: get_group_list.py
    Time: 2021/7/13 下午11:10
-------------------------------------------------
    Change Activity: 2021/7/13 下午11:10
-------------------------------------------------
    Desc: 
"""

from src.http import BaseHandler
from src.handler.group import group_handler


class GetGroupList(BaseHandler):
    def post(self, *args, **kwargs):
        return self.response(group_handler.get_group_list())

    def get(self, *args, **kwargs):
        return self.response(group_handler.get_group_list())
