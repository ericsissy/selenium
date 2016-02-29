#-*- coding: UTF-8 -*-
'''
Created on Dec 23, 2014

@author: egao
'''


# -*- coding: utf-8 -*-
#Login App with browser    chrome/firefox/ie(HtmlUnit)
BROWSER       = "firefox"
DRIVER = ""

# Driver of web browser, such as: webdriver.Firefox()
# BROWSER             = ""

# URL which will be tested web site
URL                 = u"http://newtours.demoaut.com/"
# URL                 = u"http://ddv-ntcat1.us.signintra.com:8080/po_fs/"
# URL = u"http://pan.baidu.com"


# WEB SITE ACCOUNT
USERNAME            = u"EDPRBI"
PASSWORD            = u"test"

'''WORK IN HOME'''
# Root path of the testing project.
PROJECT_PATH        = u"D:\\lunaworkspace\\Schenker_3"
RESULT_PATH        = u"D:\\lunaworkspace\\Schenker_3\\result"
CONFIG_PATH         = u"D:\\lunaworkspace\\Schenker_3\\config"
 
# Location of DRIVER(CHROME / FIREFOX / IE)
DRIVER_CHROME       = u"D:\lunaworkspace\Schenker_3\driver\chromedriver.exe"
# DRIVER_IE           = u"D:\lunaworkspace\Schenker_1\driver\IEDriverServer.exe"
DRIVER_IE           = r"C:\Python27\IEDriverServer.exe"
DRIVER_FIREFOX      = ""

'''WORK IN COMPANY'''
# Root path of the testing project.
# PROJECT_PATH        = u"E:\\workspace\\Schenker_3"
# RESULT_PATH        = u"E:\\workspace\\Schenker_3\\result"
# CONFIG_PATH         = u"E:\\workspace\\Schenker_3\\config"
#  
# # Location of DRIVER(CHROME / FIREFOX / IE)
# DRIVER_CHROME       = u"E:\workspace\DBSchenker\driver\chromedriver.exe"
# DRIVER_IE           = u"E:\workspace\DBSchenker\driver\IEDriverServer.exe"
# DRIVER_FIREFOX      = ""

# Location of WEB BROWSER
BINARY_CHROME       = u"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
BINARY_FIREFOX      = ""
BINARY_IE           = ""

# Test Case/Module variables.
CASE_START_TIME     = ""
CASE_STOP_TIME      = ""
CASE_NAME           = ""
CASE_PASS           = ""
CASE_LOAD           = "LOAD_TEST_CASE"
ENV_INIT            = "ENV_INIT"

MODULE_NAME         = ""

PAGE                = ""

REPORT_FILE_NAME    = "POFS OF SCHENKER"
REPORT_TITLE        = "DB Schenker - SHARED SERVICE CENTER NANJING CHINA"
REPORT_DESC         = "This is desc of report"

# zip file name
LOG_FILES            = "Auto_Test_Log"

# email config
MAIL_SENDER         = 'gong500@163.com'
MAIL_RECEIEVER      = '695929419@qq.com'
MAIL_SUBJECT        = 'Test report fom Automation testing'
MAIL_SMTPSERVER     = 'smtp.163.com'
MAIL_USERNAME       = 'gong500@163.com'
MAIL_PASSWORD       = '198789'

# Database Operation
# MySQL
MYSQL_IP               = u"127.0.0.1"
MYSQL_USERNAME         = u"root"
MYSQL_PASSWORD         = u"root"
MYSQL_DBNAME             = u"testdb"
MYSQL_CHARSET          = u"utf8"

# Oracle
ORACLE_IP               = u"127.0.0.1"
ORACLE_PORT             = u"1521"
ORACLE_USERNAME         = u"sdp"
ORACLE_PASSWORD         = u"sdp"
ORACLE_INSTANCE             = u"sdp"



