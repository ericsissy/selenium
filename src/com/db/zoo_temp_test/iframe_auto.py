'''
Created on Feb 28, 2015

@author: jiefeng
'''
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

 

url = u'file:///E:/Users/egao/Desktop/main.html'
driver = webdriver.Firefox()
driver.get(url)

main_handle = driver.current_window_handle
handles = driver.window_handles
driver.find_element(By.ID, "btnLoad").click()
print main_handle
driver.switch_to.frame("TestFrame")
driver.find_element(By.ID, "frameText").send_keys("this is for testing...")
driver.find_element(By.ID, "btnSendBack").click()
# driver.switch_to.default_content()
# driver.switch_to.window(main_handle)

driver.switch_to.window(handles[0])
driver.find_element(By.ID, "btnLoad").click()
print driver.find_element(By.ID, "lblMsg").text

time.sleep(5)
driver.close()
