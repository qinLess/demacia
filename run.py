# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: run.py
    Time: 2021/7/13 下午6:57
-------------------------------------------------
    Change Activity: 2021/7/13 下午6:57
-------------------------------------------------
    Desc: 
"""
import tornado.ioloop
import tornado.httpserver
from tornado.web import Application

from src.utils.log_setting import get_logger
from src.http.index import Index
from src.socket_server import SocketServer
from src.http.get_group_list import GetGroupList
from src.http.async_invoke import AsyncInvoke

logger = get_logger('tornado')


# # 配置 tornado log 输出
# from src.utils.log_settings import LoggerFormatter
#
# log_path = os.path.join(os.path.dirname(__file__), 'logs', datetime.datetime.now().strftime('%Y-%m-%d'))
# if not os.path.exists(log_path):
#     os.makedirs(log_path)
#
# options.log_file_prefix = os.path.join(log_path, 'tornado.log')
# options.parse_command_line()
# [i.setFormatter(LoggerFormatter()) for i in logging.getLogger().handlers]


class DemaciaApplication(Application):
    def __init__(self):
        # 路由
        routers = [
            ('/demaica', Index),
            ('/demaica/websocket', SocketServer),
            ('/demaica/getGroupList', GetGroupList),
            ('/demaica/asyncInvoke', AsyncInvoke),
        ]

        # web 全局配置
        settings = {
            'debug': False
        }

        super().__init__(routers, **settings)


# 初始化服务，监听端口号
app = DemaciaApplication()
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(10521)
logger.info(f'start server Success! {10521}')
tornado.ioloop.IOLoop.current().start()
