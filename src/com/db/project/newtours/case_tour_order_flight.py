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
from com.db.project.newtours.case_tour_common import CommonMethod


class TestCaseOrderFlight(TestCase):

    @classmethod
    def setUpClass(cls):
        Conf.DRIVER = cls.driver = LoginApp().sysLogin()
#         Conf.DRIVER = self.driver
        cls.driver.implicitly_wait(30)

    def test_tour_order_flight_001(self):
        u"""This is comment of test_case_login_001 shown in report"""
        Conf.CASE_NAME = "test_tour_order_flight_001"
         
        Log.start_test(Conf.CASE_NAME)
        
#         Element.find_element(By.NAME, u'userName').send_keys("a")
#         Element.find_element(By.NAME, u'password').send_keys("a")
#         Element.find_element(By.NAME, u'login').click()
        
        CommonMethod.test_tour_login_common()
        
        
        
        login_flag = Element.find_element(By.XPATH, u'//img[@src="/images/masts/mast_flightfinder.gif"]')
        if login_flag is not None:
            print "Login system successfully."
            Log.step_succ("Login system successfully.")
        else:
            print "Login system failed."
            Log.step_fail("Login system failed.")
            return None
        #### Flight Details
        Element.find_element(By.XPATH, u'//input[@value="oneway"]').click()
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="passCount"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="passCount"]/option'),
                                                  "4")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="fromPort"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="fromPort"]/option'),
                                                  "Paris")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="fromMonth"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="fromMonth"]/option'),
                                                  "September")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="fromDay"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="fromDay"]/option'),
                                                  "9")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="toPort"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="toPort"]/option'),
                                                  "London")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="toMonth"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="fromMonth"]/option'),
                                                  "October")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="toDay"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="fromDay"]/option'),
                                                  "19")
        
        #### Preferences
        Element.find_element(By.XPATH, u'//input[@value="Business"]').click()
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="airline"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="airline"]/option'),
                                                  "Unified Airlines")
        Element.find_element(By.NAME, "findFlights").click()
        
        #### DEPART
        if "DEPART" in Element.find_element(By.XPATH, u'//font[@color="#FF9900"][text()="DEPART"]').text:
            print "Navigate success, please choosing departure item."
            Log.step_succ("Navigate success, please choosing departure item.")
        else:
            print "Navigate failed, please check info in FLIGHT FINDER."
            Log.step_fail("Navigate failed, please check info in FLIGHT FINDER.")
            return None
        
        Element.find_element(By.XPATH, u'//input[@value="Pangea Airlines$362$274$9:17"][@name="outFlight"]').click()
        #### RETURN
        Element.find_element(By.XPATH, u'//input[@value="Blue Skies Airlines$631$273$14:30"][@name="inFlight"]').click()
        Element.find_element(By.NAME, u'reserveFlights').click()
        
        #### BOOK A FLIGHT
        book_flight = Element.find_element(By.XPATH, u'//img[@src="/images/masts/mast_book.gif"]')
        if book_flight is not None:
            print "Navigate success, please complete the form to book the flight online."
            Log.step_succ("Navigate success, please complete the form to book the flight online.")
        else:
            print "Navigate failed, please check DEPART/RETURN info in SELECT FLIGHT."
            Log.step_fail("Navigate failed, please check DEPART/RETURN info in SELECT FLIGHT.")
            return None
        
        Element.find_element(By.NAME, u'passFirst0').send_keys("Jiefeng")
        Element.find_element(By.NAME, u'passLast0').send_keys("Gao")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="pass.0.meal"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="pass.0.meal"]/option'),
                                                  "Diabetic")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="creditCard"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="creditCard"]/option'),
                                                  "Discover")
        Element.find_element(By.NAME, u'creditnumber').send_keys("0000000000000000000")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="cc_exp_dt_mn"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="cc_exp_dt_mn"]/option'),
                                                  "06")
        Element.choose_spinner_value(Element.find_elements(By.XPATH, u'//select[@name="cc_exp_dt_yr"]/option'),
                                                  Element.get_spinner_values(By.XPATH, u'//select[@name="cc_exp_dt_yr"]/option'),
                                                  "2008")
        Element.find_element(By.NAME, u'cc_frst_name').send_keys("Gao")
        Element.find_element(By.NAME, u'cc_mid_name').send_keys("Jie")
        Element.find_element(By.NAME, u'cc_last_name').send_keys("feng")
        Element.find_element(By.NAME, u'ticketLess').click()
        
        Element.checkbox_all(Element.find_elements(By.NAME, u'ticketLess'))
        
        Element.find_element(By.NAME, u'buyFlights').click()
        
        #### FLIGHT CONFIRMATION
        confirmation_message = Element.find_element(By.XPATH, u'//img[@src="/images/masts/mast_confirmation.gif"]')
        if confirmation_message is not None:
            print "Book a flight successfully."
            Log.step_succ("Book a flight successfully.")
        else:
            print "Book a flight failed."
            Log.step_fail("Book a flight failed.")
        
        Element.find_element(By.XPATH, u'//img[@ src="/images/forms/home.gif"]').click()
        
        """Here's something should do calculate :
                Total Taxes:      $44 USD
                Total Price (including taxes):      $584 USD
        """
        
        Browser.navigate_to(Conf.URL)
        Log.stop_test()
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCaseOrderFlight("test_tour_order_flight_001"))
    
    unittest.TextTestRunner().run(suite)
