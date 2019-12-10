# 处理类

from tornado import web
import json


class BaseHandler(web.RequestHandler):

    def get_cookie(self, *args, **kwargs):
        return self.get_secure_cookie(*args, **kwargs)

    def set_cookie(self, *args, **kwargs):
        return self.set_secure_cookie(*args, **kwargs)

    def send_json(self, data):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(data))
        self.finish()
