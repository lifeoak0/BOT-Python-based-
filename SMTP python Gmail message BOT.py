import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email, from_email, password):
    # 创建一个带有附件的邮件对象,
    msg = MIMEMultipart()
    msg['From'] = ''
    msg['To'] = ''
    msg['Subject'] = '很高兴认识你'

    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # 使用SMTP连接到Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# 使用Gmail账户信息发送邮件
send_email('测试邮件', '这是一封测试邮件', '', '', '')  #password提供应用专用密码
