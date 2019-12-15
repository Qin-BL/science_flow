from mysql.user import verify_user, has_user
from lib.redis import rs


def user_verify(uname, pwd):
    if rs.exists('%s_%s' % (uname, pwd)):
        return True
    if verify_user(uname, pwd):
        rs.set('%s_%s' % (uname, pwd), ex=3600)
        return True
    return False


def has_uname(uname):
    if has_user(uname):
        return True
    return False
