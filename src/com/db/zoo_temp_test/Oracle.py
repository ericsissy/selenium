# -*- coding: gbk -*-
'''
Created on Jan 16, 2015

@author: jiefeng
'''

import os

import cx_Oracle

from com.db.conf import Conf
from com.db.library import Log
from com.db.library.Common import DatabaseOpeartor

import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

if __name__ == '__main__':

#     reload(sys)
#     sys.setdefaultencoding('utf8')
    sql = u'SELECT * FROM capital_adjust'
    print DatabaseOpeartor.get_all_records("oracle", sql)
#     print DatabaseOpeartor.get_one_record('oracle', sql)

# 
# # cur = conn.cursor()
# 
# 
# ## There is no symbol " ; " at the end of the sql.
# sql = u'SELECT * FROM capital_adjust'
# cur.execute(sql)
# # cur.execute(sql.decode('utf8'))
# records = cur.fetchall()
# lines = len(records)
# for i in range(lines):
#     print records[i]
# cur.close()