# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: async_invoke.py
    Time: 2021/7/14 上午12:03
-------------------------------------------------
    Change Activity: 2021/7/14 上午12:03
-------------------------------------------------
    Desc: 
"""
import json

from tornado.gen import sleep

from src.http import BaseHandler
from src.handler.group import group_handler
from src.handler.response import response_handler
from src.utils.log_setting import get_logger

logger = get_logger('async_invoke')


class AsyncInvoke(BaseHandler):

    async def res_handler(self, post_data):
        time_num = 1
        while True:
            if time_num > 15:
                response_handler.del_response_info(**post_data)
                return self.response(data='请求超时异常', code=400)

            res = response_handler.get_response_info(**post_data)

            if res is not None:
                response_handler.del_response_info(**post_data)
                return self.response(data=res)

            else:
                time_num += 1
                await sleep(0.1)

    async def post(self, *args, **kwargs):
        post_data = json.loads(self.request.body.decode('utf-8'))
        logger.info(f'AsyncInvoke.post_data: {json.dumps(post_data, ensure_ascii=False)}')

        group_id = post_data.get('group_id')
        action_name = post_data.get('action_name')

        if not group_id:
            self.response(data='group_id 不能为空', code=400)
            return

        if not action_name:
            self.response(data='action_name 不能为空', code=400)
            return

        socket_instance = group_handler.get_group_info(group_id)
        if not socket_instance:
            self.response(data='group_id 未注册', code=400)
            return

        post_data['__process_id__'] = self.random_process_id(json.dumps(post_data, ensure_ascii=False))
        socket_instance.send_msg(post_data)

        return await self.res_handler(post_data)
