# 处理类

from tornado import web
import json
from settings import COOKIES


class BaseHandler(web.RequestHandler):

    def get_cookie(self, *args, **kwargs):
        return self.get_secure_cookie(*args, **kwargs)

    def set_cookie(self, *args, **kwargs):
        return self.set_secure_cookie(*args, **kwargs)

    def send_json(self, data):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(data))
        self.finish()

    @property
    def username(self):
        username = self.get_secure_cookie(COOKIES)
        return username

    def get_current_user(self):
        username = self.username
        if not username:
            self._logout()
            return
        return username.decode()

    def _login(self, username):
        self.set_secure_cookie(COOKIES, username, expires_days=1)

    def _logout(self):
        self.clear_cookie(COOKIES)
