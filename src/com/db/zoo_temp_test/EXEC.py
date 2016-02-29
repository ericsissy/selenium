'''
Created on Jan 6, 2015

@author: egao
'''
from com.db.test.TESTCASE_Login import TestCaseLogin
from com.db.test.TESTCASE_Search import TestCaseSearch
from unittest import main
import os


if __name__ == '__main__':
#     main()
    TestCaseLogin().testCase001_Login()
    TestCaseSearch().testCase001_Login()
#     os.popen("TASKKILL /F /IM chromedriver.exe")
    TestCaseSearch().testCase002_Search()
#     pass