external_url 'http://119.3.221.174:40443'
##! email settings
# 以qq为例
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.qq.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "2528756899@qq.com"
# qq邮箱的授权码
gitlab_rails['smtp_password'] = "gwzsdcguoxgudife"
gitlab_rails['smtp_domain'] = "qq.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = true
gitlab_rails['smtp_tls'] = true
gitlab_rails['gitlab_email_from'] = '2528756899@qq.com'