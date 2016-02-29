'''
Created on Jan 7, 2015

@author: jiefeng
'''
from unittest import TestCase
import unittest

from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library import Log
from com.db.library.Common import LoginApp
from com.db.library.Spider import Element


class TestCaseForgetPassword(TestCase):
    def setUp(self):
        self.driver = LoginApp().sysLogin()
        Conf.DRIVER = self.driver
        self.driver.implicitly_wait(30)
        

    def test_case_001_forget_password(self):
        Conf.CASE_NAME = "test_case_001_forget_password"
        
        Log.start_test(Conf.CASE_NAME)
        
        Element.find_element(self.driver, By.CLASS_NAME, u'pass-fgtpwd').click()
        Log.stop_test()
        
        
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseForgetPassword("test_case_001_forget_password"))
    unittest.TextTestRunner().run(suite)