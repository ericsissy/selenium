'''
Created on Jan 7, 2015

@author: jiefeng
'''
from unittest import main, TestCase
import com.db.page
from com.db.library import Log
from com.db.conf import Conf
from com.db.library.Common import import_module_dynamic


class TestCaseLogin(TestCase):
    def test_case_login_001(self):
        Conf.CASE_NAME = "testCase001_Login"
        
        # Start to execute case and record the starting time
        Log.start_test(Conf.CASE_NAME)
        
        Csdn = import_module_dynamic("Csdn")
        Csdn.Profile.CSDN_USERNAME.send_keys("jiefenggao")
        Csdn.Profile.CSDN_PASSWORD.send_keys("gaojiefeng")
        Csdn.Profile.CSDN_SUBMIT.click()
        
        Log.stop_test()
        
if __name__ == "__main__":
    main()    