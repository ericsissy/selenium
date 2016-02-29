# -*- coding: UTF-8 -*-
'''
Created on Feb 16, 2015

@author: egao
'''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from com.db.conf import Conf
from com.db.library.Spider import Element


Conf.DRIVER = driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(u"E:\\Users\\egao\\Desktop\\alert.html")


print os.path.join(os.path.dirname(__file__))
print os.path

ALERT_BUTTON = driver.find_element_by_id("alert")
# a = Element.find_element(By.NAME, "alert")
CONFIRM_BUTTON = driver.find_element_by_id("confirm")
PROMPT_BUTTON = driver.find_element_by_id("prompt")

t = driver.find_element_by_id("test")
print t.get_attribute("value")


# ALERT_BUTTON.click()
# ALERT_DIAG = driver.switch_to_alert()
# time.sleep(3)
# print "====>", ALERT_DIAG.text
# ALERT_DIAG.accept()
# 
# CONFIRM_BUTTON.click()
# CONFIRM_DIAG = driver.switch_to_alert()
# time.sleep(3)
# print "====>", CONFIRM_DIAG.text
# CONFIRM_DIAG.accept()
# 
# CONFIRM_BUTTON.click()
# CONFIRM_DIAG = driver.switch_to_alert()
# time.sleep(3)
# CONFIRM_DIAG.dismiss()

# PROMPT_BUTTON.click()
# PROMPT_DIAT = driver.switch_to_alert()
# time.sleep(3)
# PROMPT_DIAT.accept()

# PROMPT_BUTTON.click()
# PROMPT_DIAT = driver.switch_to_alert()
# time.sleep(3)
# PROMPT_DIAT.dismiss()

# PROMPT_BUTTON.click()
# PROMPT_DIAT = driver.switch_to_alert()
# time.sleep(3)
# # print "------->", PROMPT_DIAT.text
# PROMPT_DIAT.send_keys("THIS IS USED FOR TESTING.")
# print "------->", PROMPT_DIAT.text
# PROMPT_DIAT.accept()
# print "------->", PROMPT_DIAT.text


time.sleep(3)
driver.quit()