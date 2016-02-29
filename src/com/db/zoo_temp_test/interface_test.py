#-*- conding:gb2312-*-
'''
Created on Feb 4, 2015

@author: jiefeng
'''
import urllib, urllib2

"""
    Convert special char to normal string
"""
def urlcode(date):
    return urllib2.quote(str(date))



def get_info_http(url, param_in, method, post_key = None):
    """
        HTTP GET / POST to get the result from HTTP server.
        NOTE: should optimize the input parameter to get more
            pair of key-values
    """
    if method.upper() == 'GET':
        url_get = url + urlcode(param_in)
        result = urllib2.urlopen(url_get).read()
        return result
   
    if method.upper() == 'POST':
        url_post = url
        values = {post_key : param_in}
        data = urllib.urlencode(values)
        req = urllib2.Request(url_post, data)
        response = urllib2.urlopen(req)
        result = response.read()
        return result
    
"""
    Test case
"""

if __name__ == "__main__":
    url_post = url_base = 'http://api.liqwei.com/location/'
    url_get = 'http://api.liqwei.com/location/?ip='
    
    print get_info_http(url_get, "202.108.33.32", "GET")
    print get_info_http(url_post, "202.108.33.32", "POST", "ip")






