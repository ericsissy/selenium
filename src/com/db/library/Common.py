# -*- coding: gbk -*-
'''
Created on Dec 23, 2014

@author: egao
'''


import HTMLTestRunner
from datetime import datetime
import doctest
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 
import importlib
import inspect
import os.path
import smtplib  
import unittest
import urllib, urllib2
import zipfile
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import suds

from com.db.conf import Conf
from com.db.execution import Case_List
from com.db.library import Log
from com.db.library.Log import mkdirs, load_test_case_record, stamp_datetime, \
    init_env_record, stamp_datetime_co


# import MySQLdb
# import cx_Oracle
# reload(sys)
# sys.setdefaultencoding('gbk')
class DriverInvoker:
    
    def __init__(self, driverName):
        self.driverName = driverName
        self.url = Conf.URL
    """To judge and decide which browser will be used in testing,
        system supports 3 kinds of browser for testing, they are : 
            ->>firefox
            ->>chrome
            ->>IE or htmlunit
    """
    def webBrowser(self):
        if self.driverName.upper() == 'FIREFOX':
            '''There are 2 different way to get the instance of webdriver:
                1. Use configuration file to record it, but when use it, system will not recognize its methods, but useful.
                    i.e.    Conf.BROWSER = webdriver.Firefox()
                            
                            #-> Init and create instance
                            di = DriverInvoker("firefox");
                            di.webBrowser()
                            Conf.BROWSER.get(Conf.URL)
                            Conf.BROWSER.maximize_window()
                            Conf.BROWSER.quit()
                2. To return the instance of webdriver.
                    i.e.    DRIVER = webdriver.Firefox()
                            return DRIVER
                            
                            #-> Init and create instance
                            di = DriverInvoker("firefox");
                            DRIVER = di.webBrowser()
                            DRIVER.get(Conf.URL)
                            DRIVER.maximize_window()
                            DRIVER.quit()
            '''

            # Method 1
            fp = FirefoxProfile()
            fp.native_events_enabled = False
#             fp.accept_untrusted_certs()
            Conf.DRIVER = webdriver.Firefox(firefox_profile=fp)
            
            # Method 2
#             DRIVER = webdriver.Firefox()
#             return DRIVER
            
        elif self.driverName.upper() == 'CHROME':
            # os.popen("TASKKILL /F /IM chrome.exe")
            os.popen("TASKKILL /F /IM chromedriver.exe")
            
            # Method 1
            Conf.DRIVER = webdriver.Chrome(executable_path=Conf.DRIVER_CHROME)
            
            # Method 2
#             DRIVER = webdriver.Chrome(executable_path=Conf.DRIVER_CHROME)
#             return DRIVER
            
        elif self.driverName.upper() == 'IE':
            # os.popen("TASKKILL /F /IM iexplore.exe")
            os.popen("TASKKILL /F /IM IEDriverServer.exe")
            
            dc = DesiredCapabilities.INTERNETEXPLORER.copy()
            dc['acceptSslCerts'] = True
            dc['nativeEvents'] = True
            dc['ignoreProtectedModeSettings'] = True
            
            os.environ["webdriver.ie.DRIVER"] = Conf.DRIVER_IE
            Conf.DRIVER = webdriver.Ie(executable_path=Conf.DRIVER_IE, capabilities=dc)
            
            # Method 2
#             DRIVER = webdriver.Ie(executable_path=Conf.DRIVER_IE, capabilities=dc)
#             return DRIVER
        
        elif self.driverName.upper() == 'HTMLUNIT':
            err_msg = "Selenium server is shut down, please to start it..."
            start_selenium_server = "java -jar selenium-server-standalone-2.41.0.jar"
            try:
                Conf.DRIVER = webdriver.Remote("http://localhost:4444/wd/hub",
                                               webdriver.DesiredCapabilities.HTMLUNITWITHJS)
            except Exception as e:
                print str(e)
                init_env_record('-> %s %s \n      %s \n      Start by : %s' 
                                % (stamp_datetime(), str(e), err_msg, start_selenium_server))
        
        else:
            return None

"""Invoking "LoginApp" to call function of selenium
	to lunch the browser and navigate to a tested_page
"""
class LoginApp:
    def sysLogin(self):
        di = DriverInvoker(Conf.BROWSER)
        di.webBrowser()
        DRIVER = Conf.DRIVER
        DRIVER.implicitly_wait(30)
        DRIVER.get(Conf.URL)
        DRIVER.maximize_window()
        
        return DRIVER

# DRIVER = LoginApp().sysLogin()

"""
class DatabaseOpeartor:
    '''
    DatabaseOpeartor is used to operate the database of mysql, oracle, sqlite
    '''
    @classmethod
    def open_connection(cls, database_type):
        '''
        :Purpose: Return database connection by a certain type of database(mysql, oracle, sqlite)
        
        :Parameter: 
            database_type : mysql, oracle, sqliste
        
        :return:
            database connection
            
        :uasge:
            conn = DatabaseOpeartor.open_connection(database_type)
        '''
        
        if database_type.upper() == "MYSQL":
            try:
                conn = MySQLdb.connect(Conf.MYSQL_IP, Conf.MYSQL_USERNAME, Conf.MYSQL_PASSWORD,
                                       Conf.MYSQL_DBNAME, charset=Conf.MYSQL_CHARSET)
                print "Create connection of MySQL successfully."
                Log.init_env_record("Create connection of MySQL successfully.")
            except MySQLdb.Error  as e:
                print "Create connection of MySQL failed."
                Log.init_env_record("Create connection of MySQL failed, err_msg : %s" % (str(e)))
                return None
            
            return conn
        
        elif database_type.upper() == "ORACLE":
            # Can not use sysdba / dba role to connect Oracle
            # There are two kinds of connection string format
            try:
            # Type 1
#                 conn = cx_Oracle.connect('%s' %Conf.ORACLE_USERNAME , '%s' %Conf.ORACLE_PASSWORD,
#                                          '%s:%s/%s' % (Conf.ORACLE_IP, Conf.ORACLE_PORT, Conf.ORACLE_INSTANCE))
            # Type 2
                conn = cx_Oracle.connect('%s/%s@%s:%s/%s'.decode('utf8') 
                                         %(Conf.ORACLE_USERNAME, Conf.ORACLE_PASSWORD, 
                                           Conf.ORACLE_IP, Conf.ORACLE_PORT, Conf.ORACLE_INSTANCE))
                print "Create connection of Oracle successfully."
                Log.init_env_record("Create connection of Oracle successfully.")
            except cx_Oracle.DatabaseError as e:
                print "Create connection of Oracle failed."
                Log.init_env_record("Create connection of Oracle failed, err_msg : %s" % (str(e)))
                return None
            
            return conn
        
        elif database_type.upper() == "SQLITE":
            pass
        
        else:
            print "Database Error : Undefined database type."
            Log.init_env_record("Undefined database type.")
            return None
    
    @classmethod
    def get_all_records(cls, database_type, sql_string):
        '''
        :Purpose: Return all records as result_all list
        
        :Parameter: 
            database_type : mysql, oracle, sqliste
            sql_string: sql
        
        :return:
            [u'gao', u'luo']
            
        :uasge: 
            sql_mysql = "select first_name from employee;"
            sql_oracle = u'SELECT * FROM capital_adjust'    # no ";" at the end of sql of oracle
            result_list = DatabaseOpeartor.get_all_records("mysql", sql_content)
        '''
        
        conn = DatabaseOpeartor.open_connection(database_type)
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_string)
                data = cur.fetchall()
                Log.init_env_record("Get cursor successfully.")
            except Exception as e:
                Log.init_env_record("Get cursor failed, err_msg : %s", str(e))
        else:
            print "No database connection exist, do nothing."
            Log.init_env_record("No database connection exist, do nothing.")
            return None
            
        
        numrows = int(cur.rowcount)  # get the total row number of result set
        result_list = []
        for i in range(numrows):
            for j in range(len(data[i])):
                result_list.append(data[i][j])
        
        if cur: cur.close()
        if conn: conn.close()
        
        return result_list
    
    @classmethod
    def get_one_record(cls, database_type, sql_string):
        '''
        :Purpose: Return one record as result_all list
        
        :Parameter: 
            database_type : mysql, oracle, sqliste
            sql_string: sql
        :Return:
            [u'gao', u'jiefeng']
        
        :Uasge: 
            sql_mysql = "select first_name from employee;"
            sql_oracle = u'SELECT * FROM capital_adjust'    # no ";" at the end of sql of oracle
            result_list = DatabaseOpeartor.get_one_record("mysql", sql_content)
        '''
        conn = DatabaseOpeartor.open_connection(database_type)
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_string)
                data = cur.fetchone()
                Log.init_env_record("Get cursor successfully.")
            except Exception as e:
                Log.init_env_record("Get cursor failed, err_msg : %s", str(e))
        else:
            print "No database connection exist, do nothing."
            Log.init_env_record("No database connection exist, do nothing.")
            return None
        
        result_list = []
        for i in range(len(data)):
            result_list.append(data[i])
            
        if cur: cur.close()
        if conn: conn.close()
        
        return result_list
"""

class ArchiveFile():
    
    @classmethod
    def zip_dir(cls, dirname = Conf.RESULT_PATH, 
                zipfilename = "%s\\%s_%s.zip" % (Conf.RESULT_PATH, Conf.LOG_FILES, stamp_datetime_co())):
        '''
            :Purpose: Zip directory or file
            
            :Parameter: 
                dirname :     directory should be archived
                zipfilename : the output zip file name
            
            :return:
                Zip file name
                
            :uasge: 
                zip_dir()
                OR
                zip_dir(Conf.RESULT_PATH,
                        "%s\\%s_%s.zip" % (Conf.RESULT_PATH, Conf.LOG_FILES, stamp_datetime_co()))
            '''
        
#         Conf.LOG_FILES = zipfilename
        print Conf.LOG_FILES
        filelist = []
        
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))
        
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            print arcname
            zf.write(tar, arcname)
        zf.close()
        
        return zipfilename

    @classmethod
    def unzip_file(cls, zipfilename, unziptodir):
        """ do not verify
        """
        if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\', '/')
            
            if name.endswith('/'):
                os.mkdir(os.path.join(unziptodir, name))
            else:            
                ext_filename = os.path.join(unziptodir, name)
                ext_dir = os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir) : os.mkdir(ext_dir, 0777)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()


"""
    Convert special char to normal string
"""
def urlcode(date):
    return urllib2.quote(str(date))

def get_info_http(url, param_in, method, post_key = None):
    """
        HTTP GET / POST to get the result from HTTP server.
        +++NOTE: should optimize the input parameter to get more
            pair of key-values
        :Usage: 
            if __name__ == "__main__":
                url_post = url_base = 'http://api.liqwei.com/location/'
                url_get = 'http://api.liqwei.com/location/?ip='
    
                print get_info_http(url_get, "202.108.33.32", "GET")
                print get_info_http(url_post, "202.108.33.32", "POST", "ip")
    """
    if method.upper() == 'GET':
        url_get = url + urlcode(param_in)
        result = urllib2.urlopen(url_get).read()
        return result
   
    elif method.upper() == 'POST':
        url_post = url
        values = {post_key : param_in}
        data = urllib.urlencode(values)
        req = urllib2.Request(url_post, data)
        response = urllib2.urlopen(req)
        result = response.read()
        return result
    else:
        return None

'''
    WebService
'''
def get_info_wb(url, param_in=None):
    """
        +++NOTE: should optimize the input parameter to get more
    """
    client = suds.client.Client(url)
    service = client.service
    
    '''
    Use this 'client' to know the methods of this WebService, like :
        Service ( qqOnlineWebService ) tns="http://WebXml.com.cn/"
        Prefixes (0)
        Ports (2):
          (qqOnlineWebServiceSoap)
             Methods (1):
                qqCheckOnline(xs:string qqCode, )
             Types (0):
          (qqOnlineWebServiceSoap12)
             Methods (1):
                qqCheckOnline(xs:string qqCode, )
             Types (0):
    '''
    print client
    
    status = service.qqCheckOnline(param_in)
    print status
    
    '''
        Use "client.last_received()" to get the response message of WebService, like : 
        <?xml version="1.0" encoding="UTF-8"?>
            <soap:Envelope>
               <soap:Body>
                  <qqCheckOnlineResponse xmlns="http://WebXml.com.cn/">
                     <qqCheckOnlineResult>Y</qqCheckOnlineResult>
                  </qqCheckOnlineResponse>
               </soap:Body>
            </soap:Envelope>
    '''
    print client.last_received()
    
    return status

def send_mail(attachment_file_name):
    print attachment_file_name
#     attach_name = attachment_file_name.split('\\')[4].split('.')[0]
    attach_name = attachment_file_name.split('\\')[4]
    
    sender      = Conf.MAIL_SENDER
    receiver    = Conf.MAIL_RECEIEVER
    subject     = Conf.MAIL_SUBJECT
    smtpserver  = Conf.MAIL_SMTPSERVER
    username    = Conf.MAIL_USERNAME
    password    = Conf.MAIL_PASSWORD
    
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    
    # Construct the attachment
    att = MIMEText(open(attachment_file_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % attach_name
    msgRoot.attach(att)
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print "Mail sended successfully"
    Log.init_env_record("Mail sended successfully")

def import_module_dynamic(pageName):
    """Import the module which is the name of a certain page
    """
    return importlib.import_module(Conf.PAGE + pageName)

def make_directory(directory_name, flag="result"):
    '''Make directory under the project result
    '''
    if flag == "result":
        mkdirs("%s\\%s\\" % (Conf.RESULT_PATH, directory_name))
    elif flag == "project":
        mkdirs("%s\\%s\\" % (Conf.PROJECT_PATH, directory_name))
    else:
        return False

def generate_report(report_name="default_report_name"):
    '''Generate report with report name as input parameter
    '''
    make_directory("reports", "result")
    file_name = "%s\\reports\\%s.html" % (Conf.RESULT_PATH, report_name)
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                                          stream=fp,
                                          title=Conf.REPORT_TITLE,
                                          description=Conf.REPORT_DESC)
    return runner

"""Get current function name"""
def get_function_name():
#     return inspect.stack()[1][3]
    return sys._getframe().f_code.co_name

"""Get current system time"""
def get_system_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def execute_automation_test(send_flag=None, report_name=Conf.REPORT_FILE_NAME):
    '''Used to load test cases, execute the test case and generate the report
    '''
    load_test_case_record('   %s Initial environment...' % stamp_datetime())
    
    suite = doctest.DocTestSuite()
    cases = Case_List.case_list()
    
    load_test_case_record('   %s Case loading start...' % stamp_datetime())
    print 'Case loading start...'
    for case in cases:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(case))
            load_test_case_record("+> %s %s is loaded successfully." % (stamp_datetime(), case))
        except Exception as e:
            load_test_case_record('-> %s ERROR: Skipping tests from "%s" from err_msg : %s.' % (stamp_datetime(), case, str(e)))
            try:
                __import__(case)
            except ImportError as e:
                load_test_case_record('----------> %s, can not import it.' % str(e))
            else:
                load_test_case_record('==========> Could not load the test suite, please contact service desk.')
    load_test_case_record('   %s Case loading done!' % stamp_datetime())
    print 'Case loading done!'
#             from traceback import print_exc
#             print_exc()
    print load_test_case_record('   %s Running the tests...' % stamp_datetime())
    print 'Running the tests...'
    
    # Generate the test report
    generate_report(report_name).run(suite)
    
    # Judge to send email
    if send_flag is not None:
        send_mail(ArchiveFile.zip_dir())
    else:
        return None

def get_value_from_conf(key):
    '''Used to get value by key from configuration file : //config/conf.ini
    '''
    conf_file = u"%s\\conf.ini" % Conf.CONFIG_PATH
    
    if not os.path.exists(conf_file):
        return ""
    
    if not os.path.isfile(conf_file):
        return ""
    
    try:
        with open(conf_file, 'r') as f:
            while True:
                data = f.readline()
                
                if not data:
                    break
                
                if len(data.split('=')) < 2:
                    continue
                
                if data.strip()[0] == "#":
                    continue
                
                if data.split('=')[0].strip() == key:
                    return str(data.split('=', 1)[1].strip())
    except IOError:
        return ""


if __name__ == '__main__':
    pass
