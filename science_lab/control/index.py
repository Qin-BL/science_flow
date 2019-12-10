
from lib.redis import rs
from mysql.index import get_content, get_all, get_one


def get_index_content(id=1):
    res = rs.get('index_content')
    if not res:
        res = get_content()
    return res


def get_all_content():
    return get_all()


def get_one_content():
    return get_one()

