#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

import logging

from pythonjsonlogger import jsonlogger


class Logger(object):
    LOGGERLIST = [
        'options',
        'main',
        'output',
        'tornado.access',
        'tornado.generic',
    ]

    FORMAT = '%(asctime) %(module) %(levelname) %(message)'

    def __init__(self):
        self.handler = logging.StreamHandler()

        self.formatter = jsonlogger.JsonFormatter(self.FORMAT)

        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.DEBUG)

        for name in self.LOGGERLIST:
            logger = logging.getLogger(name)
            # logger.setLevel(logging.DEBUG)
            logger.addHandler(self.handler)

    def setLevel(self, level):
        self.handler.setLevel(level)

    @staticmethod
    def get(logger_name):
        return logging.getLogger(logger_name)
