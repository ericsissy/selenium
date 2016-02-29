# -*- coding: gbk -*-
'''
Created on Feb 9, 2015

@author: jiefeng
'''
'''
Endpoint: http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx 
Disco: http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx?disco 
WSDL: http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx?wsdl 
'''

import suds
from suds.servicedefinition import ServiceDefinition

from com.db.library import Datadriver


def get_method_wb(client=None):
    '''get the methods of soap
        return a METHOD list
        it will be used a parameter of the invoker function
        [getDatabaseInfo(),
        getMobileCodeInfo(xs:string mobileCode, xs:string userID,)
        ]
        '''
#     print client    #get methods which should handled again.
    method_list = ["getDatabaseInfo", "getMobileCodeInfo"]
    return method_list

def get_param_no_wb(function_name=None):
    # Get the number of the function input parameters
    return 2
    

def get_info_wb(url):
    
    client = suds.client.Client(url)
    service = client.service
    
    method_list = get_method_wb(client)
    print "method_list--->", method_list
    sd = []
    for s in client.wsdl.services:
        print s
        sp = ServiceDefinition(client.wsdl, s)
        sd.append(sp)
    print "service:", sd
    # parameters
    excel = Datadriver.ExcelSheet(r"Employee.xlsx", "Sheet3")
    for method in method_list:
        #Get the number of the function
        param_number = get_param_no_wb(method)
        print "param_number--->", param_number
        param_list = []
        init_no = 1 #which line of parameter-file
        
        for i in range(param_number):
            param_list.append(excel.cell(init_no,"p"+str(i+1)))
        print param_list
        print "method : %s" %(method)
        
        if param_number == 0:
            status = service.method
            print status
        elif param_number > 0:
            if param_number == 1:
                status = service.method(param_list[0])
            elif param_number == 2:
                status = service.method_list[1](param_list[0], param_list[1])
                
                print status
            elif param_number == 3:
                status = service.method(param_list[0], param_list[1], param_list[2])
            elif param_number == 4:
                status = service.method(param_list[0], param_list[1], param_list[2], param_list[3])
            elif param_number == 5:
                status = service.method(param_list[0], param_list[1], param_list[2], param_list[3], param_list[4])
            else:
                print "Should change function to handle more parameters...."
        else:
            print "Error of parameter list"
        return status
        
        init_no += 1
        if init_no > excel.nrows(): break
        continue
    
    print client.last_received()
    

if __name__ == '__main__':
    print get_method_wb()
    print get_param_no_wb()
    
    url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
    get_info_wb(url)
