# -*- coding:gbk -*-
import suds

from com.db.library.Common import get_info_wb


url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# url = 'http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl'
client = suds.client.Client(url)
service = client.service

print client
status = service.getDatabaseInfo()
ss = service.getMobileCodeInfo("13815447896", "")
# print status
print ss
