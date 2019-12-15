from handler import BaseHandler
from control.user import user_verify, has_uname
from lib.send_mail import send_mail
from control.index import gen_verify_code, verify_vcode
from mysql.user import add_user


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
        try:
            uname = self.get_argument("uname")
            mail = self.get_argument("mail")
            pwd = self.get_argument("password")
            vcode = self.get_argument("vcode")
        except:
            return self.send_json(errcode=1001, errmsg='参数错误')
        vres = verify_vcode(mail, vcode)
        if not vres:
            return self.send_json(errcode=1002, errmsg="验证码失效")
        if has_uname(uname):
            return self.send_json(errcode=1003, errmsg="用户名已存在")
        uinfo = {
            "name": uname,
            "mail": mail,
            "password": pwd
        }
        add_user(uinfo)
        self.send_json()


class ResetHandler(BaseHandler):

    def get(self):
        self.render('reset.html')

    def post(self):
        try:
            uname = self.get_argument("uname")
            mail = self.get_argument("mail")
            pwd = self.get_argument("password")
            vcode = self.get_argument("vcode")
        except:
            return self.send_json(errcode=1001, errmsg='参数错误')
        vres = verify_vcode(mail, vcode)
        if not vres:
            return self.send_json(errcode=1002, errmsg="验证码失效")
        if not has_uname(uname):
            return self.send_json(errcode=1004, errmsg="用户名不存在")
        uinfo = {
            "name": uname,
            "mail": mail,
            "password": pwd
        }
        add_user(uinfo)
        self.send_json()


class VerifyCodeHandler(BaseHandler):

    def get(self):
        try:
            receiver = self.get_argument('rec')
        except:
            return self.send_json(errcode=1001)
        code = gen_verify_code(receiver)
        text = "【验证码】%s（5分钟内有效），欢迎使用science lab" % code
        send_mail(receiver, text)
        self.send_json()


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

