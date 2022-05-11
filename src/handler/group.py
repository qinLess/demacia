# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: group.py
    Time: 2021/7/13 下午10:48
-------------------------------------------------
    Change Activity: 2021/7/13 下午10:48
-------------------------------------------------
    Desc: 
"""


class GroupHandler(object):
    group_info = {}

    def set_group_info(self, group_id, socket_instance):
        self.group_info[group_id] = socket_instance

    def get_group_info(self, group_id):
        return self.group_info.get(group_id)

    def get_group_list(self):
        return list(self.group_info.keys())


group_handler = GroupHandler()
