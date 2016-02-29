#-*- coding: UTF-8 -*-
'''
Created on Jan 9, 2015

@author: egao
'''
from com.db.library.Log import load_test_case_record, stamp_datetime


# def case_list():
#     '''FOR APPLICATION POFS'''
#     cases = [
#             'com.db.project.pofs.case_pofs_login.TestCaseLogin',
#             'com.db.project.pofs.case_pofs_logout.TestCaseLogout',
#             'com.db.project.pofs.case_pofs_search.TestCaseSearch',
#              ]
#     load_test_case_record('+> %s Read case list successfully.' % stamp_datetime())
#     return cases

# def case_list():
#     '''FOR APPLICATION PAN.BAIDU'''
#     cases = [
#             'com.db.project.pan_baidu.pan_baidu.case_pan_login.TestCaseLogin',
#             'com.db.project.pan_baidu.pan_baidu.case_pan_forget_password.TestCaseForgetPassword',
#             'com.db.project.pan_baidu.pan_baidu.case_pan_register.TestCaseRegister',
#              ]
#     load_test_case_record('+> %s Read case list successfully.' % stamp_datetime())
#     return cases

def case_list():
    '''FOR APPLICATION TOURS'''
    cases = [
            'com.db.project.newtours.case_tour_login.TestCaseLogin',
            'com.db.project.newtours.case_tour_register.TestCaseLogin',
            'com.db.project.newtours.case_tour_order_flight.TestCaseOrderFlight',
             ]
    load_test_case_record('+> %s Read case list successfully.' % stamp_datetime())
    return cases