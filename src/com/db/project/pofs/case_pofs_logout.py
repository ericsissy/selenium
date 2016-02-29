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
from com.db.library.Spider import Element, Assert
from com.db.project.pofs.case_pofs_common import CommonMethod


class TestCaseLogout(TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = LoginApp().sysLogin()
        Conf.DRIVER = self.driver
    
    def setUp(self):
        pass
    
    def test_case_logout_001(self):
        '''Login page, write username and password'''
        Conf.CASE_NAME = "test_case_logout_001"
         
        Log.start_test(Conf.CASE_NAME)
        
        #Login
        CommonMethod.test_pofs_login_common()
        
        #Logout
        self.POFS_LOGOUT = Element.find_element(By.XPATH, u'//a[@href="login/logout.jsp"]')
        Assert().assert_equal(self.POFS_LOGOUT.text, "Log Out")
        self.POFS_LOGOUT.click()
        
        self.POFS_LOGOUT_MESSAGE = Element.find_element(By.XPATH, u'//td[@align="right"][@style=" color: red;"]').text
        print self.POFS_LOGOUT_MESSAGE
        Assert().assert_equal(self.POFS_LOGOUT_MESSAGE, "You are successfully logged out")
        
        Log.stop_test()
        
        
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseLogout("test_case_logout_001"))
    unittest.TextTestRunner().run(suite)