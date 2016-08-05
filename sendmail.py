hostname = "smtp.gmail.com"
password = "ifqdxcimpptxwmul"
me = "bbb2daiict@gmail.com"
you = "ankitlakra137@gmail.com"

import smtplib
#from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()

msg["Subject"] = "Test subject"
msg["From"] = me
msg["To"] = you
#msg.attach(MIMEText(file("gmail1.py").read())
fp = open('filename.png', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

s = smtplib.SMTP_SSL(hostname)
s.login(me, password)
s.sendmail(me, [you], msg.as_string())
s.quit()

