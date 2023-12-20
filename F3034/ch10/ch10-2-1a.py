import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

gmail_user = 'your_email@gmail.com'
gmail_password = 'your_password'

to = 'hueyan@ms2.hinet.net'
subject = '自動化Email'
body = '這是使用Python程式自動寄送的電子郵件。'

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject

msg.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, msg.as_string())
    server.close()

    print('Email sent!')
except Exception as e:
    print('Something went wrong...', e)
