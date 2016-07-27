#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

import configargparse

from rest_app import log

LOG = log.Logger.get()


class Options(object):

    def __init__(self):
        self.parser = configargparse.ArgParser(
            default_config_files=['./config.ini'])

        self.parser.add('-c', '--my-config',
                        required=False,
                        is_config_file=True,
                        help='config file path')

        # this option can be set in a config file because it starts with '--'
        self.parser.add('--port',
                        required=False,
                        type=int,
                        help='listen port',
                        default=8888,
                        env_var='APP_PORT')

    def parse(self):
        return self.parser.parse_args()
