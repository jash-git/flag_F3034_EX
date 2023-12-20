import smtplib

gmail_user = 'your_email@gmail.com'
gmail_password = 'your_password'

to = 'hueyan@ms2.hinet.net'
subject = '自動化Email'
body = '這是使用Python程式自動寄送的電子郵件。'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, to, subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print('Something went wrong...', e)
