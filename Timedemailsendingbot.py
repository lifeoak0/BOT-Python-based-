import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email():
    from_email = 'your_email@gmail.com'
    to_email = 'recipient@example.com'
    subject = 'Scheduled Email'
    message = 'This is a scheduled email sent using Python!'

    # 创建一个带有附件的邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # 添加正文
    msg.attach(MIMEText(message, 'plain'))

    # 使用SMTP连接到Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'your_app_password')

    # 发送邮件
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# 每天的10:00发送邮件
schedule.every().day.at("10:00").do(send_email)

# 运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)

