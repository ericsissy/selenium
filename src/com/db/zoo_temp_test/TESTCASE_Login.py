'''
Created on Jan 6, 2015

@author: egao
#
The package "page" must be imported(import com.db.page), 
because it will initial the module path like : com.db.page.Login
'''
# -*- coding=utf-8 -*-

from com.db.library import Log
from com.db.conf import Conf
from com.db.library.Common import import_module_dynamic
from unittest import TestCase, main
import com.db.page
import time

class TestCaseLogin():
    def testCase001_Login(self):
        '''This always is the 1st case for automation'''
        Conf.CASE_NAME = "testCase001_Login"
        
        # Start to execute case and record the starting time
        Log.start_test(Conf.CASE_NAME)
        
        # Which page you want to import, use name of this page as a parameter.
        Login = import_module_dynamic("Login")
        Login.Profile.POFS_USERNAME.send_keys(Conf.USERNAME)
        Login.Profile.POFS_PASSWORD.send_keys(Conf.PASSWORD)
        Login.Profile.POFS_SUBMIT.click()
        time.sleep(1)
        
        Log.stop_test()





if __name__ == "__main__":
    '''If wanna call this case by this single file,
       the test case should inherit "unitest.TestCase"
       
       e.g. : 
           from unittest import TestCase, main
           class TestCaseSearch(TestCase):
           
        If wanna call this case in other file, 
        the test case should NOT inherit "unittest.TestCase"
        
        e.g. :
            class TestCaseSearch():
            call it use : TestCaseLogin().testCase001_Login()
            
        But, if you wanna use main() to call case, it should
        inherit "unittest.TestCase"
    '''
    main()

