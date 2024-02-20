import imaplib
import email
from email.header import decode_header

# 邮箱凭据
email_address = 'your_email@gmail.com'
password = 'your_password'

# 连接到Gmail邮箱
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_address, password)
mail.select('inbox')

# 搜索收件箱中的所有邮件
status, data = mail.search(None, 'ALL')
mail_ids = data[0].split()

# 遍历邮件
for num in mail_ids:
    status, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # 提取邮件主题和发件人
    subject = decode_header(msg['Subject'])[0][0]
    from_email = decode_header(msg['From'])[0][0]

    print(f'主题：{subject}')
    print(f'发件人：{from_email}')

# 关闭邮箱连接
mail.close()
mail.logout()
