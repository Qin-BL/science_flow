#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from tornado.options import options


# cookie名
COOKIES = 'my_science_lab'

# 静态资源路径
STATIC_PATH = os.path.join(sys.path[0], 'static')
# tornado 模板路径
TEMPLATE_PATH = os.path.join(sys.path[0], 'static/template')
# 默认redis
DEFAULT_REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}
# 默认mysql
mysql_master = {
    'user': 'root',
    'password': 'qinbilei888',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'science'
}
# ES
ES_CONF = ["http://127.0.0.1:9200"]
# 请放在结尾
if options.debug:
    from settings_debug import *
