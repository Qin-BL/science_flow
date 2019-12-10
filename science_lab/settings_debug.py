#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import options


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
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'test'
}
