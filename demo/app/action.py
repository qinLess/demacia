# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: action.py
    Time: 2021/7/31 下午2:47
-------------------------------------------------
    Change Activity: 2021/7/31 下午2:47
-------------------------------------------------
    Desc: 
"""
import os
import sys

file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(file_path)

from demo.app.ws_client import SocketClient
from demo.app.frida_hook import get_x_sign_8110, get_mini_wua_8110


class GetEncrypt(object):
    def __init__(self):
        group_id = 'tianmao'
        client_id = 'tianmao'

        url = 'ws://127.0.0.1:10521/demaica'
        ws_url = f'{url}/websocket?group_id={group_id}&client_id={client_id}'

        self.socket_client = SocketClient(ws_url=ws_url)

    @staticmethod
    def get_x_sign_8110(**kwargs):
        return get_x_sign_8110(kwargs['params'])

    @staticmethod
    def get_mini_wua_8110(**kwargs):
        return get_mini_wua_8110(kwargs['params'])

    def start(self):
        self.socket_client.register_action('get_x_sign_8110', self.get_x_sign_8110)
        self.socket_client.register_action('get_mini_wua_8110', self.get_mini_wua_8110)

        self.socket_client.on_connect()


if __name__ == '__main__':
    GetEncrypt().start()
