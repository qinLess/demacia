# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: log_setting.py
    Time: 2021/7/15 下午5:35
-------------------------------------------------
    Change Activity: 2021/7/15 下午5:35
-------------------------------------------------
    Desc: 
"""
import logging.config

import os
import datetime
import logging
import logging.handlers

from tornado.log import LogFormatter


class LoggerFormatter(LogFormatter):
    def __init__(self):
        fmt = '[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] %(message)s'
        date_fmt = '%Y-%m-%d %H:%M:%S'
        super().__init__(fmt, date_fmt)


class Logger(object):
    def __init__(self, name):
        self.logger = logging.getLogger(name)

        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            day_date = datetime.datetime.now().strftime("%Y-%m-%d")
            log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
            self.log_path = os.path.join(log_path, f'{day_date}/')
            if not os.path.exists(self.log_path):
                os.makedirs(self.log_path)

            self.log_name = f'{self.log_path}{name + ".log"}'
            fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
            fh.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            formatter = logging.Formatter(
                '[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
            fh.close()
            ch.close()


def get_logger(name):
    return Logger(name).logger
