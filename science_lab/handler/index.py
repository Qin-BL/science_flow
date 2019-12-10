
from handler import BaseHandler
from control.index import get_index_content, get_all_content, get_one_content


class IndexHandler(BaseHandler):

    def get(self):
        uname = self.get_current_user()
        if not uname:
            self.redirect('/login')
            return


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        pass


class LogoutHandler(BaseHandler):

    def get(self):
        pass


class RegisterHandler(BaseHandler):

    def get(self):
        pass
