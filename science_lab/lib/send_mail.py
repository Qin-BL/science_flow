import smtplib
from email.mime.text import MIMEText
from email.header import Header
import traceback
import logging


# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"
user = '2528756899@qq.com'
pwd = 'gwzsdcguoxgudife'


def send_mail(content, receiver):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("science lab", 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header('science lab 验证码', 'utf-8')
    try:
        s = smtplib.SMTP(mail_host)
        s.starttls()
        s.login(user, pwd)
        s.sendmail(user, receiver, message.as_string())
        logging.info('邮件发送成功')
        return True
    except:
        logging.error(traceback.format_exc())
        return False
