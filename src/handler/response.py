# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: response.py
    Time: 2021/7/14 下午4:19
-------------------------------------------------
    Change Activity: 2021/7/14 下午4:19
-------------------------------------------------
    Desc: 
"""


class ResponseHandler(object):
    response_info = {}

    def set_response_info(self, **kwargs):
        pid = f"{kwargs['group_id']}|{kwargs['action_name']}|{kwargs['__process_id__']}"
        self.response_info[pid] = kwargs.get('data', '')

    def get_response_info(self, **kwargs):
        pid = f"{kwargs['group_id']}|{kwargs['action_name']}|{kwargs['__process_id__']}"
        return self.response_info.get(pid)

    def del_response_info(self, **kwargs):
        pid = f"{kwargs['group_id']}|{kwargs['action_name']}|{kwargs['__process_id__']}"
        if self.response_info.get(pid):
            del self.response_info[pid]


response_handler = ResponseHandler()
