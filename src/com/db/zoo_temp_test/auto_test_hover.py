'''
Created on Feb 28, 2015

@author: jiefeng
'''
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()
driver.get("http://51job.com")
driver.maximize_window()

main_handle = driver.current_window_handle
dist_button = driver.find_element(By.NAME, "btnJobarea")
unlimit_button = driver.find_element(By.XPATH, '//span[@cctype="buxian"]')
close_button = driver.find_element(By.XPATH, '//span[@cctype="close"]')
dist_list = driver.find_elements(By.XPATH, '//td[@style="cursor: pointer; font-weight: bold; width: 75px; padding-left: 1px;"]')

#get hover text

# action = webdriver.ActionChains(driver)
# driver.execute_script("document.getElementById('popup_C').style.display='block';")
# driver.find_element(By.XPATH,"//*[@id='popup_C']/div[2]/div/a[1]").click()
# action.move_to_element(driver.find_element(By.XPATH, "//*[@id='Map']/area[1]"))
# action.click(driver.find_element(By.XPATH,"//*[@id='popup_A']/div[2]/div/a[1]"))
# print driver.find_element(By.XPATH,"//*[@id='popup_A']/div[2]/div/a[1]").text
# action.perform()
# time.sleep(1000)
# driver.quit()

zczx = driver.find_elements(By.XPATH, "//*[@id='newart'][@title]")
for i in range(len(zczx)):
    print zczx[i].text

'''
action = webdriver.ActionChains(driver)
driver.execute_script("document.getElementById('popup_B').style.display='block';")
action.click(driver.find_element(By.XPATH,"//*[@id='popup_B']/div[2]/div/a[1]"))
print driver.find_element(By.XPATH,"//*[@id='popup_B']/div[2]/div/a[1]").text
action.perform()
time.sleep(1000)
driver.quit()
#### or 
driver.execute_script("document.getElementById('popup_B').style.display='block';")
driver.find_element(By.XPATH,"//*[@id='popup_B']/div[2]/div/a[1]").click()
'''
'''
dist_button.click()
dist_list[0].click()
key_word = driver.find_element(By.NAME, "keyword")
key_word.send_keys("a")
search_button = driver.find_element(By.NAME, "image")
search_button.click()

#switch to new window
handles = driver.window_handles
driver.switch_to.window(handles[-1])

# area_button = driver.find_element(By.NAME, "btnJobarea")
# area_button.click()
# map_button = driver.find_element(By.ID, "Map")

map_button = driver.find_element(By.XPATH, '//area[@href="javascript:void(0);"][@shape="rect"]')
action = webdriver.ActionChains(driver)
driver.execute_script("document.getElementById('all-channel').style.display='block';")
# action.move_to_element(map_button)  #
# action.click(map_button)    #or use 
action.click(driver.find_element(By.XPATH, '/html/body/div/div[8]/div/table/tbody/tr[3]/td[4]/a[4]'))
action.perform()

time.sleep(5)
driver.quit()

##go back to the main page
# driver.switch_to.window(handles[0])
# search_button = driver.find_element(By.NAME, "image")
# search_button.click()
'''