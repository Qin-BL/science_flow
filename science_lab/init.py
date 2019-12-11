#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tornado import web
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.options import options, define
import logging
from ui import modules, methods
import base64
import uuid

define('port', default=8888)
define('debug', default=False)
options.parse_command_line()

if options.debug:
    from settings_debug import *
else:
    from settings import *

urls = [
    (r'/', 'handler.index.IndexHandler'),
    (r'/index', 'handler.index.IndexHandler'),
    (r'/login', 'handler.index.LoginHandler'),
    (r'/logout', 'handler.index.LogoutHandler'),
    (r'/register', 'handler.index.RegisterHandler'),
]


class Application(web.Application):
    def __init__(self):
        super(Application, self).__init__(urls, **{
            'debug': options.debug,
            'compress_response': True,  # 如果为 True, 以文本格式的响应 将被自动压缩
            'ui_modules ': modules,
            'ui_methods ': methods,
            'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),  # 防止cookie被篡改
            'login_url': '/login',
            'xsrf_cookies': True,  # 如果true, 跨站请求伪造(防护) 将被开启
            'static_path': STATIC_PATH,
            'template_path': TEMPLATE_PATH,
        })


if __name__ == '__main__':
    app = Application()
    httpserver = HTTPServer(app, xheaders=True)
    httpserver.listen(options.port)
    logging.info('running..., port=%d, debug=%s' % (options.port, options.debug))
    tornado.ioloop.IOLoop.instance().start()

