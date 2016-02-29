#-*- coding: UTF-8 -*-
'''
Created on Jan 12, 2015

@author: jiefeng
'''

import MySQLdb

from com.db.conf import Conf
from com.db.library import Log


class DatabaseOpeartor:
    
    @classmethod
    def open_connection(cls, database_type):
        if database_type is "mysql":
            try:
                conn = MySQLdb.connect(Conf.DB_IP, Conf.DB_USERNAME, Conf.DB_PASSWORD, Conf.DB_NAME, charset = Conf.DB_CHARSET)
                print "Create connection of MySQL successfully."
                Log.step_succ("Create connection of MySQL successfully.")
            except Exception  as e:
                print "Create connection of MySQL failed."
                Log.step_fail("Create connection of MySQL failed.")
            return conn
        elif database_type is "oracle":
            pass
        elif database_type is "sqlite":
            pass
        else:
            print "Database Error : Undefined database type."
            Log.step_fail("Undefined database type.")
            return None
    
    @classmethod
    def get_all_records(cls, database_type, sql_string):
        '''
        :Purpose: Return all records as result_all list
        
        :Parameter: 
            database_type : mysql, oracle, sqliste
            sql_string: sql
        
        :return:
            [u'gao', u'luo']
            
        :uasge: 
            sql_content = "select first_name from employee;"
            result_list = DatabaseOpeartor.get_all_records("mysql", sql_content)
        '''
        
        conn = DatabaseOpeartor.open_connection(database_type)
        if conn:
            cur = conn.cursor()
        else:
            print "No database connection exist, do nothing."
            
        cur.execute(sql_string)
        data = cur.fetchall()
        numrows = int(cur.rowcount)
        result_list = []
        for i in range(numrows):
            for j in range(len(data[i])):
                result_list.append(data[i][j])
        if conn:
            conn.close()
        return result_list
    
    @classmethod
    def get_one_record(cls, database_type, sql_string):
        '''
        :Purpose: Return one record as result_all list
        
        :Parameter: 
            database_type : mysql, oracle, sqliste
            sql_string: sql
        :Return:
            [u'gao', u'jiefeng']
        
        :Uasge: 
            sql_content = "select first_name, last_name from employee;"
            result_list = DatabaseOpeartor.get_one_record("mysql", sql_content)
        '''
        conn = DatabaseOpeartor.open_connection(database_type)
        if conn:
            cur = conn.cursor()
        else:
            print "No database connection exist, do nothing."
        
        cur.execute(sql_string)
        data = cur.fetchone()
        numrows = int(cur.rowcount)
        result_list = []
        for i in range(numrows):
            result_list.append(data[i])
        if conn:
            conn.close()
        return result_list




if __name__ == "__main__":
#     sql_content = "select * from employee"
    sql_content = "select first_name, last_name from employee;"
#     sql_content = "select first_name from employee;"
    result_list = DatabaseOpeartor.get_all_records("mysql", sql_content)
#     result_list = DatabaseOpeartor.get_one_record("mysql", sql_content)
    print result_list
    
#     result_list = []
#     for i in range(len(result_all)):
#         for j in range(len(result_all[i])):
#             result_list.append(result_all[i][j])
#     print result_list
    















