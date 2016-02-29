#-*- coding: UTF-8 -*-
'''
Created on Feb 15, 2015

@author: egao
'''
from selenium.webdriver.common.by import By

from com.db.library.Spider import Element


class CommonMethod():
    
    @classmethod
    def test_pofs_login_common(cls,username, password):
        u"""Common method for test cases to invoke."""
        
        POFS_USERNAME = Element.find_element(By.NAME, u'userName')
        POFS_PASSWORD = Element.find_element(By.NAME, u'password')
        POFS_SUBMIT = Element.find_element(By.XPATH, u'//input[@id="button"][@name="p_request_in"]')
        
        POFS_USERNAME.send_keys(username)
        POFS_PASSWORD.send_keys(password)
        POFS_SUBMIT.click()





