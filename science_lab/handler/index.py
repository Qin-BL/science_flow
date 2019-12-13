
from handler import BaseHandler
from control.index import get_index_content, get_all_content, get_one_content
from control.user import user_verify


class IndexHandler(BaseHandler):

    def get(self):
        uname = self.get_current_user()
        if not uname:
            self.redirect('/login')
            return
        self.render(
            'index.html',
        )


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html', errmsg='')

    def post(self):
        try:
            uname = self.get_argument('uname')
            passwd = self.get_argument('passwd')
        except:
            return self.send_json(errcode=1001, errmsg='参数错误')
        vres = user_verify(uname, passwd)
        if vres:
            self._login(uname)
            self.redirect('/')
        else:
            self.render('login.html', errmsg='用户名或密码错误')


class LogoutHandler(BaseHandler):

    def get(self):
        self._logout()
        self.redirect('/login')
        return


class RegisterHandler(BaseHandler):

    def get(self):
        self.render('register.html')

    def post(self):
        pass


class ChangePwdHandler(BaseHandler):

    def get(self):
        uname = self.get_current_user()
        if not uname or len(uname.split('|')) < 3:
            self.redirect('/login')
            return
        user_name, authority, agent_id = uname.split('|')
        agent_info = ctrl.api.get_agent_info_by_uname(user_name)
        phone_num = agent_info.get('mobile_no', '')
        phone_num_tips = phone_num[:3] + '****' + phone_num[7:]
        self.render('change_psw.tpl',
                    phone_num=phone_num,
                    phone_num_tips=phone_num_tips
                    )

