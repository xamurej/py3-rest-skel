#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

from rest_app import log

LOG = log.Logger.get('app')


class CarsHandler(APIHandler):
    """A red car"""

    @schema.validate(output_schema={"type": "string"})
    def get(self, color):
        """returns 'A <color> car.'"""
        return "A {0} car.".format(color)
