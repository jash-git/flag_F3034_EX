import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 設置Gmail帳戶和密碼
gmail_user = 'your_email@gmail.com'
gmail_password = 'your_password'

# 設置收件人、主題和郵件內容
to = 'recipient@example.com'
subject = '開會通知'
body = '附檔是本次開會的資料'

# 讀取Excel檔案並提取電子郵件地址
df = pd.read_excel('meeting.xlsx')
# emails = df['B2':'B4'].values.flatten()
emails = df["電子郵件地址"]

# 使用SMTP協議連接到Gmail郵件服務器
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

# 發送郵件給每個電子郵件地址
for email in emails:
    # 建立MIMEMultipart對象並設置主題、寄件人、收件人和郵件內容
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = gmail_user
    message['To'] = email

    # 將郵件內容轉換為MIMEText對象並添加到郵件中
    text = MIMEText(body)
    message.attach(text)

    # 將"各通路業積報告.pdf"文件讀取為二進制數據並附加到郵件中
    with open('各通路業積報告.pdf', 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename='各通路業積報告.pdf')
        message.attach(attachment)

    # 發送郵件
    server.sendmail(gmail_user, email, message.as_string())

# 關閉SMTP連接
server.quit()