'''
Created on Jan 7, 2015

@author: jiefeng
'''
from unittest import TestCase
import unittest

from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library import Datadriver
from com.db.library import Log
from com.db.library.Common import LoginApp
from com.db.library.Spider import Element, Assert, Browser
from com.db.project.pofs.case_pofs_common import CommonMethod


class TestCaseLogin(TestCase):
    """
    http://my.oschina.net/lionets/blog/268704
    """
    @classmethod
    def setUpClass(self):
        self.driver = LoginApp().sysLogin()
        Conf.DRIVER = self.driver
    
    def setUp(self):
        pass
    
    def test_case_login_001(self):
        '''Login page, write username and password'''
        Conf.CASE_NAME = "test_case_login_001"
         
        Log.start_test(Conf.CASE_NAME)
        
        CommonMethod.test_pofs_login_common("EDPRBI", "test")
        
        Browser.navigate_to(Conf.URL)
        Log.stop_test()
        
    def test_case_login_002(self):
        '''Login page, reset button'''
        Conf.CASE_NAME = "test_case_login_002"
         
        Log.start_test(Conf.CASE_NAME)
        
        self.POFS_USERNAME = Element.find_element(By.NAME, u'userName')
        self.POFS_PASSWORD = Element.find_element(By.NAME, u'password')
        self.POFS_RESET = Element.find_element(By.XPATH, u'//input[@type="reset"][@value="Reset"]')
         
        self.POFS_USERNAME.send_keys("EDPRBI")
        self.POFS_PASSWORD.send_keys("test")
        self.POFS_RESET.click()
        
        username = self.driver.execute_script("var input = document.getElementsByName('userName')[0].value;return input")
        password = self.driver.execute_script("var input = document.getElementById('password').value;return input")
        Assert().assert_equal(username, "")
        Assert().assert_equal(password, "")
        if username == "" and password == "":
            print "pass"
        else:
            print "fail"

#         self.driver.get(Conf.URL)
        Browser.navigate_to(Conf.URL)
        
        Log.stop_test()
        
        
    def test_case_login_003(self):
        '''Login page, wrong username and correct password'''
        
        Conf.CASE_NAME = "test_case_login_003"
        Log.start_test(Conf.CASE_NAME)
        
        CommonMethod.test_pofs_login_common("EDPRBIa", "test")
        error_message = Element.find_element(By.XPATH, u'//td[@class="subhead"][@align="center"]').text
        Assert().assert_equal(error_message, "Invalid UserID or Password. Attempt 1 of 6.")
        
#         self.driver.get(Conf.URL)
        Browser.navigate_to(Conf.URL)
        
        Log.stop_test()
        
        
    def test_case_login_004(self):
        excel = Datadriver.ExcelSheet(r"Employee.xlsx", "Sheet1")
        
        for i in range(1, excel.nrows()):
            employeeID = excel.cell(i, "Empoyee_ID")
            password = excel.cell(i, "Password")
            department=excel.cell(i,"Department")
            hiredate=excel.cell(i,"Date_Of_Hiring")
            role=excel.cell(i,"Employee_Role")
            fname=excel.cell(i,"F_Name")
            acountry=excel.cell(i,"Bj")
            nationality=excel.cell(i,"Nationality")
            
            if employeeID !="":
                print employeeID
                
            if password != "":
                print password
                print type(password)
                
            if department !="":
                print department
                print type(department)
                
            if hiredate!="":
                print hiredate
                
            if role!="":
                print role
                
            if fname!="":
                print fname
                
            if acountry!="":
                print acountry
                
            if nationality !="":
                print nationality


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(TestCaseLogin("test_case_login_003"))
#     suite.addTest(TestCaseLogin("test_case_login_001"))
#     suite.addTest(TestCaseLogin("test_case_login_002"))
    suite.addTest(TestCaseLogin("test_case_login_004"))
    unittest.TextTestRunner().run(suite)
#     main()
        