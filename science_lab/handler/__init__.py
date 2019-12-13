# 处理类

from tornado import web
import json
from settings import COOKIES
import re


class BaseHandler(web.RequestHandler):

    def get_cookie(self, *args, **kwargs):
        return self.get_secure_cookie(*args, **kwargs)

    def set_cookie(self, *args, **kwargs):
        return self.set_secure_cookie(*args, **kwargs)

    def send_json(self, data={}, errcode=200, errmsg='', status_code=200):
        res = {
            'errcode.py': errcode,
            'errmsg': errmsg if errmsg else '请求成功'
        }
        res.update(data)

        json_str = json.dumps(res)

        jsonp = self.get_argument('jsonp', '')
        if jsonp:
            jsonp = re.sub(r'[^\w\.]', '', jsonp)
            self.set_header('Content-Type', 'text/javascript; charet=UTF-8')
            json_str = '%s(%s)' % (jsonp, json_str)
        else:
            self.set_header('Content-Type', 'application/json')

        origin = self.request.headers.get("Origin")
        origin = '*' if not origin else origin

        self.set_header("Access-Control-Allow-Origin", origin)
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PUT, DELETE')

        self.set_status(status_code)
        self.write(json_str)
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

    def get_real_ip(self):
        req_headers = self.request.headers
        real_ip = ''
        try:
            if 'X-Forwarded-For' in req_headers:
                real_ip = req_headers['X-Forwarded-For']
            if not real_ip and 'X-Real-Ip' in req_headers:
                real_ip = req_headers['X-Real-Ip']
            if not real_ip:
                real_ip = self.request.remote_ip
        except:
            real_ip = ''
        if real_ip.count(',') > 0:
            real_ip = re.sub(',.*', '', real_ip).strip()
        return real_ip
