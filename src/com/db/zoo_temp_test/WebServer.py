'''
Created on Feb 27, 2015

@author: egao
'''


import soaplib 
from soaplib.core.model.clazz import Array 
from soaplib.core.model.clazz import ClassModel 
from soaplib.core.model.primitive import Integer, String 
from soaplib.core.server import wsgi 
from soaplib.core.service import DefinitionBase 
from soaplib.core.service import soap 


class C_ProbeCdrModel(ClassModel): 
        __namespace__ = "C_ProbeCdrModel" 
        Name=String 
        Id=Integer 
class AdditionService(DefinitionBase):  #this is a web service 
        @soap(Integer,Integer,_returns=String) 
        def addition(self,a,b): 
                print 'aaaaaaaaaaaa' 
                return str(a)+'+'+str(b)+'='+str(a+b) 
        @soap(_returns=Array(String)) 
        def GetCdrArray(self): 
                print 'bbbbbbbbbb' 
                L_Result=["1","2","3"] 
                return L_Result 
        @soap(_returns=C_ProbeCdrModel) 
        def GetCdr(self): 
                print 'ccccccc' 
                L_Model=C_ProbeCdrModel() 
                L_Model.Name=L_Model.Name 
                L_Model.Id=L_Model.Id 
                return L_Model 

if __name__=='__main__': 
    try: 
        print 'service start' 
        from wsgiref.simple_server import make_server 
        soap_application = soaplib.core.Application([AdditionService], 'tns') 
        wsgi_application = wsgi.Application(soap_application) 
        server = make_server('localhost', 7789, wsgi_application) 
        server.serve_forever() 
    except ImportError: 
        print 'error'  

##Client to test it : 1st should start server
from suds.client import Client 
test=Client('http://localhost:7789/SOAP/?wsdl') 
print test 