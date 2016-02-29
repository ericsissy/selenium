#-*- coding: UTF-8 -*-
'''
Created on Jan 11, 2015

@author: jiefeng
'''
from unittest import TestCase
import unittest

from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library import Log
from com.db.library.Common import LoginApp
from com.db.library.Spider import Element, Browser


class TestCaseLogin(TestCase):

    @classmethod
    def setUpClass(self):
        Conf.DRIVER = self.driver = LoginApp().sysLogin()
        self.driver.implicitly_wait(30)

    def test_tour_login_001(self):
        u"""This is comment of test_case_login_001 shown in report"""
        Conf.CASE_NAME = "test_tour_login_001"
         
        Log.start_test(Conf.CASE_NAME)
        
        Element.find_element(By.NAME, u'userName').send_keys("a")
        Element.find_element(By.NAME, u'password').send_keys("a")
        Element.find_element(By.NAME, u'login').click()
        
        Browser.navigate_to(Conf.URL)
        Log.stop_test()
        

    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseLogin("test_tour_login_001"))
    
    unittest.TextTestRunner().run(suite)
