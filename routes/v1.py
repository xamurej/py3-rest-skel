#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

from rest_app import log

LOG = log.Logger.get('app')


class HelloWorldHandler(APIHandler):
    """Hello!"""

    @schema.validate(output_schema={"type": "string"})
    def get(self):
        """Shouts hello to the world!"""
        return "Hello world!"
