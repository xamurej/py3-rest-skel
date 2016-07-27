#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

import tornado.ioloop
from tornado_json.routes import get_routes
from tornado_json.application import Application

from rest_app import log
from rest_app import options

import routes as app_routes

import json

LOG = log.Logger.get('main')


def main():
    # configargparse raises a SystemExit on error
    args = options.Options().parse()
    LOG.debug(args)

    routes = get_routes(app_routes)
    LOG.error(json.dumps([(url, repr(rh)) for url, rh in routes]))
    application = Application(routes=routes, settings={})
    application.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    sys.exit(main())
