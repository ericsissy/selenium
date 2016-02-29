# -*- coding: UTF-8 -*-
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
from com.db.library.Spider import Element, Assert, Browser
from com.db.project.pofs.case_pofs_common import CommonMethod


class TestCaseSearch(TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = LoginApp().sysLogin()
        Conf.DRIVER = self.driver
        

    def test_case_search_001(self):
        Conf.CASE_NAME = "test_case_search_001"
        Log.start_test(Conf.CASE_NAME)
        
        CommonMethod.test_pofs_login_common('EDPRBI', 'test')
        
        Log.stop_test()

    def test_case_search_002(self):
        Conf.CASE_NAME = "test_case_search_002"
        Log.start_test(Conf.CASE_NAME)
        
        POFS_OVERVIEW_SEARCH = Element.find_element(By.XPATH, u'//a[@id="b"][@href="overview/overview.jsp"]')
        POFS_OVERVIEW_SEARCH.click()
        
        POFS_EXPTYPE = Element.find_elements(By.XPATH, u'//select[@name="exportType"]/option')
        POFS_EXPTYPE_CONTENT = Element.get_spinner_values(By.XPATH, u'//select[@name="exportType"]/option')
        Element.choose_spinner_value(POFS_EXPTYPE, POFS_EXPTYPE_CONTENT, "LCL")
        
        POFS_PO_ISSUE_DATE = Element.find_element(By.XPATH, u'//img[@src="../images/cal.gif"]')
        POFS_PO_ISSUE_DATE.click()
        
        Browser.switch_to_new_window()
        Element.date_picker(31, 1, 2008)
        Browser.switch_to_default_window()
        
        POFS_SEARCH = Element.find_element(By.NAME, u'submit')
        POFS_SEARCH.click()
        
        POFS_DETAIL = Element.find_element(By.XPATH, u'//img[@src="../images/detail.gif"]')
        POFS_DETAIL.click()
        Browser.switch_to_new_window()
        POFS_PONUMBER = Element.find_element(By.XPATH, u'//*[@id="printable"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]')
        Assert().assert_equal(POFS_PONUMBER.text, "0000434")
        Browser.close_window()
        Browser.switch_to_default_window()
        
        Log.stop_test()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseSearch("test_case_search_001"))
    suite.addTest(TestCaseSearch("test_case_search_002"))
    unittest.TextTestRunner().run(suite)
    
        