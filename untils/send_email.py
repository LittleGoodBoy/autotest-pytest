import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''发送html类型的邮件'''
def send_emil_html():
    '''
    发送文本邮件
    :return:
    '''
    '''第一步：创建数据'''
    sender = '15902127953@163.com'  # 定义邮件发送者
    receiver = '15902127953@163.com'  # 定义接收者 qq，火狐
    password = 'test123456'  # 定义密码
    smtpserve = 'smtp.163.com'  # 定义邮件服务器

    '''第二部：构建邮件的内容: MIMEText
    1.添加主题和收件人
    '''
    content = MIMEText('''<html><body><h1>这是系统发送邮件，
    不用回放</h1><a href="http://127.0.0.1:8089/job/1031UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6/1/allure/">报告详情请点击cichu</a></body></html>
''', 'html', 'utf-8')  # 构建邮件的内容，类型，编码
    content['From'] = Header(sender, 'utf-8')
    content['To'] = receiver
    content['Subject'] = Header('学习邮件发送', 'utf-8')

    '''第三步：发送邮件，smtplib'''
    serve = smtplib.SMTP(smtpserve, 25)  # 定义邮件服务器
    serve.set_debuglevel(1)  # 打印日志
    serve.login(sender, password)  # 登录邮件服务器
    serve.sendmail(sender, receiver, content.as_string())  # 发送邮件
    serve.quit()

send_emil_html()



