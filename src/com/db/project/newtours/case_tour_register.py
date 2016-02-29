# -*- coding: UTF-8 -*-
'''
Created on Jan 11, 2015

@author: jiefeng
'''
import time
from unittest import TestCase
import unittest

from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library import Datadriver
from com.db.library import Log
from com.db.library.Common import LoginApp
from com.db.library.Spider import Element, Assert


class TestCaseLogin(TestCase):

    @classmethod
    def setUpClass(self):
        Conf.DRIVER = self.driver = LoginApp().sysLogin()
#         Conf.DRIVER = self.driver
        self.driver.implicitly_wait(30)

    def test_tour_register_001(self):
        u"""This is comment of test_case_login_001 shown in report"""
        Conf.CASE_NAME = "test_tour_register_001"
        register_text = "000To create your account, we'll need some basic information about you. This information will be used to send reservation confirmation emails, mail tickets when needed and contact you if your travel arrangements change. Please fill in the form completely."
         
        Log.start_test(Conf.CASE_NAME)
        
        Element.find_element(By.LINK_TEXT, u'REGISTER').click()
        time.sleep(2)
        register_desc = Element.find_element(By.XPATH, u'html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p/font').text
        if "To create your account" in register_desc:
            Log.step_succ("Navigate to register page successfully.")
            Assert().assert_equal(register_text, register_desc)
            
            excel = Datadriver.ExcelSheet(r"Employee.xlsx", "Sheet2")
            
            for i in range(1, excel.nrows()):
                first_name       = excel.cell(i, "first")
                last_name        = excel.cell(i, "last")
                phone            = excel.cell(i, "phone")
                email            = excel.cell(i, "email")
                address1         = excel.cell(i, "address1")
                address2         = excel.cell(i, "address2")
                city             = excel.cell(i, "city")
                state            = excel.cell(i, "state")
                postal           = excel.cell(i, "postal")
                country          = excel.cell(i, "country")
                username         = excel.cell(i, "username")
                password         = excel.cell(i, "password")
                confirm_password = excel.cell(i, "confirm_password")
                
                if first_name !="":
                    Element.find_element(By.NAME, u'firstName').send_keys(first_name)
                if last_name != "":
                    Element.find_element(By.NAME, u'lastName').send_keys(last_name)
                if phone !="":
                    Element.find_element(By.NAME, u'phone').send_keys(phone)
                if email !="":
                    Element.find_element(By.NAME, u'userName').send_keys(email)
                if address1 !="":
                    Element.find_element(By.NAME, u'address1').send_keys(address1)
                if address2 !="":
                    Element.find_element(By.NAME, u'address2').send_keys(address2)
                if city !="":
                    Element.find_element(By.NAME, u'city').send_keys(city)
                if state !="":
                    Element.find_element(By.NAME, u'state').send_keys(state)
                if postal !="":
                    Element.find_element(By.NAME, u'postalCode').send_keys(postal)
                if country != "":
                    Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="country"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="country"]/option'),
                                                  "ANGOLA")
                if username != "":
                    Element.find_element(By.NAME, u'email').send_keys(username)
                if password != "":
                    Element.find_element(By.NAME, u'password').send_keys(password)
                if confirm_password != "":
                    Element.find_element(By.NAME, u'confirmPassword').send_keys(confirm_password)
                Element.find_element(By.NAME, u'register').click()
        else:
            Log.step_fail("Navigate to register page failed.")
        
        register_succ_desc = Element.find_element(By.XPATH, u'html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b').text
        if "Dear" in register_succ_desc:
            Log.step_succ("Register for user %s successfully." % username)
        else:
            Log.step_fail("Register for user %s failed." % username)
        
#         Browser.navigate_to( Conf.URL)
        Log.stop_test()
        

    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseLogin("test_tour_register_001"))
    
    unittest.TextTestRunner().run(suite)
