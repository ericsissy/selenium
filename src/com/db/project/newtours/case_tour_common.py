#-*- coding: UTF-8 -*-
'''
Created on Feb 15, 2015

@author: egao
'''
from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library.Spider import Element


class CommonMethod():
    
    @classmethod
    def test_tour_login_common(self):
        u"""Common method for test cases to invoke."""
        
        Element.find_element(By.NAME, u'userName').send_keys("a")
        Element.find_element(By.NAME, u'password').send_keys("a")
        Element.find_element(By.NAME, u'login').click()





