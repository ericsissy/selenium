'''
Created on Jan 15, 2015

@author: jiefeng
'''
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
sender = 'gong500@163.com'
receiver = '695929419@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'gong500@163.com'
password = '198789'
  
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

#Construct the attachement
att = MIMEText(open('e:\\cat.png', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="cat.png"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()