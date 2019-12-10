
from lib.mysql_session import session
from mysql.models import Test
from lib.decorators import model_to_list, model_to_dict


def get_content():
    res = session.query(Test).all()[0]
    return res.content


@model_to_list
def get_all():
    return session.query(Test).all()


@model_to_dict
def get_one():
    return session.query(Test).all()[0]

