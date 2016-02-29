'''
Created on Dec 23, 2014

@author: egao

#
The package "page" must be imported(import com.db.page), 
because it will initial the module path like : com.db.page.Login
'''
# -*- conding=utf-8 -*-

from com.db.library import Log
from com.db.conf import Conf
from com.db.library.Spider import Assert
from com.db.library.Common import import_module_dynamic, choose_spinner_value, \
    switch_to_new_window, switch_to_default_window, close_window
from unittest import TestCase, main
import com.db.page
import time



class TestCaseSearch():
    
    
    def testCase001_Login(self):
        '''This always is the 1st case for automation'''
        Conf.CASE_NAME = "testCase001_Login"
        
        #Start to execute case and record the starting time
        Log.start_test(Conf.CASE_NAME)
        
        #Which page you want to import, use name of this page as a parameter.
        Login = import_module_dynamic("Login")
        Login.Profile.POFS_USERNAME.send_keys(Conf.USERNAME)
        Login.Profile.POFS_PASSWORD.send_keys(Conf.PASSWORD)
        Login.Profile.POFS_SUBMIT.click()
        time.sleep(1)


    def testCase002_Search(self):
        '''testCase002_Search is dependent on testCase001_Login'''
        Conf.CASE_NAME = "testCase002_Search"
        
        
        Home = import_module_dynamic("Home")
        Assert().assert_equal(Home.Profile.POFS_TITLE.text, "P.O. Tracking Application0")
        Assert().assert_equal(Home.Profile.POFS_HEADER.text, "Application Main Menu")
        Assert().assert_equal(Home.Profile.POFS_LOGOUT.text, "Log Out")
        Home.Profile.POFS_OVERVIEW_SEARCH.click()
        
        
        OverviewSearch = import_module_dynamic("OverviewSearch")
#         OverviewSearch.Profile.POFS_PONO.send_keys("0000434")
#         OverviewSearch.Profile.POFS_EXPTYPE[1].click()

        Assert().assert_equal_spinder(OverviewSearch.Profile.POFS_EXPTYPE_CONTENT, ["LCLa", "FCL", "Select", "AIR", "TRUCK"])
        choose_spinner_value(OverviewSearch.Profile.POFS_EXPTYPE, OverviewSearch.Profile.POFS_EXPTYPE_CONTENT, "LCL")
        
        OverviewSearch.Profile.POFS_PO_ISSUE_DATE.click()
        
        switch_to_new_window()
        import_module_dynamic("OverviewSearchDatePicker")
        switch_to_default_window()
        
        
        OverviewSearch.Profile.POFS_SEARCH.click()
        
        OverviewSearchResult = import_module_dynamic("OverviewSearchResult")
        OverviewSearchResult.Profile.POFS_DETAIL.click()
        time.sleep(2)
        switch_to_new_window()
        OverviewSearchResultDetail = import_module_dynamic("OverviewSearchResultDetail")
        Assert().assert_equal(OverviewSearchResultDetail.Profile.POFS_PONUMBER.text, "0000434")
        close_window()
        switch_to_default_window()
        
        
        time.sleep(2)
        
        
        #Stop and  case and record the starting time
        Log.stop_test()




# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestCaseLogin('testCase001_Login'))
#     suite.addTest(TestCaseSearch('testCase001_Login'))
#     suite.addTest(TestCaseSearch('testCase002_Search'))
#     
#     
#     return suite
# 
# if __name__ == '__main__':
#     unittest.TextTestRunner().run(suite())



# if __name__ == "__main__":
    '''If wanna call this case by this single file,
       the test case should inherit "unitest.TestCase"
       
       e.g. : 
           from unittest import TestCase, main
           class TestCaseSearch(TestCase):
    '''
#     main()