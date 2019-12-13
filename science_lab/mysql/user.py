from mysql.models import User
from lib.mysql_session import session


def verify_user(uname, pwd):
    return session.query(User).filter(User.name == uname, User.password == pwd).scalar()


def has_user(uname):
    return session.query(User).filter(User.name == uname).scalar()


def add_user(userinfo):
    new = User(**userinfo)
    session.add(new)
    session.commit()
