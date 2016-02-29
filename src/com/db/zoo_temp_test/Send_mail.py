#coding: utf-8
'''
Created on Jan 15, 2015

@author: jiefeng
'''
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'gong500@163.com'  
receiver = '695929419@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = 'gong500@163.com'  
password = '198789'  
  
msg = MIMEText('Hello','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  