import os
import cx_Oracle
import csv
import subprocess
import shlex

tables = ['s_asset_x']
created_time = '2017-01-25 16:57:49'

SQL=[   "select distinct(row_id) from siebel.s_asset_x where created>='2015-01-01 00:00:00' and created<'2016-01-01 00:00:00'" ]

#HIVE = "SELECT distinct(row_id) FROM increment_test.siebel_nova_siebel_%s_current where created <= \'%s\' order by row_id"%(table_name,created_time) 

for i in range(0,len(tables)):
# Network drive somewhere
    filename="%s-ora-output.txt"%(tables[i])
    FILE=open(filename,"w");
    output=csv.writer(FILE, dialect='excel')
    print SQL[i]
# You can set these in system variables but just in case you didnt
#os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1') 
#os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib') 
 
    connection = cx_Oracle.connect('TRACE_APP/Pasword2@10.41.23.127:1521/HSBLPRD')
 
    cursor = connection.cursor()
    cursor.execute("alter session set nls_date_format = 'YYYY-MM-DD HH24:MI:SS'")
    cursor.execute(SQL[i])
    for row in cursor:
        output.writerow(row)
    cursor.close()
    connection.close()
    FILE.close()

'''
# hive output
#print datetime.now()
cmd = 'hive -e \"%s\" > %s-hive-output.txt'%(HIVE,table_name)
splitted = shlex.split(cmd)
print SQL
print HIVE
print cmd
#subprocess.call(splitted)
'''
