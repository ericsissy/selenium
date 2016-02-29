#-*- coding: UTF-8 -*-
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


class TestCaseLogin(TestCase):
    """
    http://my.oschina.net/lionets/blog/268704
    """
    @classmethod
    def setUpClass(self):
        self.driver = LoginApp().sysLogin()
        Conf.DRIVER = self.driver
        self.driver.implicitly_wait(30)

    def test_case_login_001(self):
        u"""This is comment of test_case_login_001 shown in report"""
        Conf.CASE_NAME = "test_case_login_001"
         
        Log.start_test(Conf.CASE_NAME)
        
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__userName').send_keys("jiefenggao")
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__password').send_keys("P@ssw0rd")
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__submit').click()
        
#         self.driver.get(Conf.URL)
        Browser.navigate_to(self.driver, Conf.URL)
        Log.stop_test()
        
    def test_case_login_002(self):
        u"""This is comment of test_case_login_002 shown in report"""
        Conf.CASE_NAME = "test_case_login_002"
        
        Log.start_test(Conf.CASE_NAME)
        
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__userName').send_keys("jiefenggaoa")
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__password').send_keys("P@ssw0rd")
        Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__submit').click()
        
        Browser.navigate_to(self.driver, Conf.URL)
        Log.stop_test()
        
    def test_case_login_003(self):
        u"""This is comment of test_case_login_003 shown in report"""
        
        Conf.CASE_NAME = "test_case_login_003"
        
        Log.start_test(Conf.CASE_NAME)

        excel = Datadriver.ExcelSheet(r"Employee.xlsx", "Sheet1")
        
        for i in range(1, excel.nrows()):
            employeeID = excel.cell(i, "Empoyee_ID")
            password = excel.cell(i, "Password")
            expect = excel.cell(i, "Expect")
            
            if employeeID !="":
                Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__userName').send_keys(employeeID)
            if password != "":
                Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__password').send_keys(password)
            Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__submit').click()
            print Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__error').text
            if expect == "expect_result_1":
                # Maybe the element should be asserted is the same one.
                # Change it in every iteration.
                Assert().assert_equal(Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__error').text, expect)
            elif expect == "expect_result_2":
                Assert().assert_equal(Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__error').text, expect)
            elif expect == "expect_result_3":
                Assert().assert_equal(Element.find_element(self.driver, By.ID, u'TANGRAM__PSP_4__error').text, expect)
            else:
                return None
#             self.driver.get(Conf.URL)
            Browser.navigate_to(self.driver, Conf.URL)
        
        Log.stop_test()
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseLogin("test_case_login_001"))
    suite.addTest(TestCaseLogin("test_case_login_002"))
    suite.addTest(TestCaseLogin("test_case_login_003"))
    
    unittest.TextTestRunner().run(suite)

        
