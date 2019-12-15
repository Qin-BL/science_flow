
from lib.redis import rs
from mysql.index import get_content, get_all, get_one
import random


def get_index_content(id=1):
    res = rs.get('index_content')
    if not res:
        res = get_content()
    return res


def get_all_content():
    return get_all()


def get_one_content():
    return get_one()


def gen_verify_code(rec):
    code = random.randint(10000, 99999)
    rs.set('%s_%s' % (rec, code), ex=60*5)
    return code


def verify_vcode(mail, code):
    key = '%s_%s' % (mail, code)
    if not rs.exists(key):
        return False
    return True
