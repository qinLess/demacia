# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: ws_client.py
    Time: 2021/7/14 下午10:15
-------------------------------------------------
    Change Activity: 2021/7/14 下午10:15
-------------------------------------------------
    Desc: 
"""
import time
import json

import websocket


class SocketConnect(object):
    def __init__(self, ws_url):
        self.ws = None
        self.ws_url = ws_url

    def on_connect(self):
        # websocket.enableTrace(True)
        try:
            self.ws = websocket.WebSocketApp(
                url=self.ws_url,
                on_message=self.on_message,
                on_close=self.on_close,
                on_error=self.on_error
            )
            self.ws.on_open = self.on_open
            self.ws.run_forever()

        except Exception as e:
            print(f'on_connect socket error: {e}')
            time.sleep(2)
            return self.on_connect()

    def on_open(self, *args):
        pass

    def on_error(self, *args):
        print(f'on_error.args: {args}')
        self.ws.close()

    def on_close(self, *args):
        self.ws.close()

    def on_message(self, ws, message):
        print(f'message.message: {message}')
        self.handle_request(message)

    def handle_request(self, request_json):
        raise NotImplemented

    def register_action(self, action, handler):
        raise NotImplemented


class SocketClient(SocketConnect):
    def __init__(self, **kwargs):
        self.handlers = {}
        self.socket = {}

        super().__init__(**kwargs)

    def send_message(self, request, response, status):
        response_json = {
            'data': response,
            'status': status,
            'group_id': request['group_id'],
            'action_name': request['action_name'],
            '__process_id__': request['__process_id__'],
        }

        response_text = json.dumps(response_json, ensure_ascii=False)

        self.ws.send(response_text)

    def register_action(self, action, handler):
        print(f'register_action: {action}')
        self.handlers[action] = handler

    def handle_request(self, request_json):
        request = json.loads(request_json)
        action_name = request['action_name']

        try:
            res = self.handlers[action_name](**request)
            self.send_message(request, res, 0)

        except Exception as e:
            self.send_message(request, f'{e}', -1)
