# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: socket_server.py
    Time: 2021/7/13 下午9:48
-------------------------------------------------
    Change Activity: 2021/7/13 下午9:48
-------------------------------------------------
    Desc: 
"""
import json

from tornado.websocket import WebSocketHandler
from src.handler.group import group_handler
from src.handler.response import response_handler
from src.utils.log_setting import get_logger

logger = get_logger('socket_server')


class SocketServer(WebSocketHandler):
    def send_msg(self, data):
        self.write_message(data)

    def open(self):
        group_id = self.get_query_argument('group_id', None)
        client_id = self.get_query_argument('client_id', None)

        if not group_id:
            self.close(reason='group_id 不能为空')
            return

        if not client_id:
            self.close(reason='client_id 不能为空')
            return

        group_handler.set_group_info(group_id, self)

    def on_message(self, message):
        logger.info(f'on_message.message: {message}')
        message = json.loads(message)
        response_handler.set_response_info(**message)

    def on_close(self):
        pass

    # 允许WebSocket的跨域请求
    def check_origin(self, origin):
        return True
