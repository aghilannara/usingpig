import os
import cx_Oracle
import csv
import subprocess
import shlex

tables = ['event_t']
created_time = '2017-01-25 16:57:49'

#SQL=[   "SELECT distinct(poid_id0) FROM pin.item_t where (to_date('1970-01-01','YYYY-MM-DD')+numtodsinterval(created_t,'SECOND'))>'2016-06-01 00:00:00' and (to_date('1970-01-01','YYYY-MM-DD')+numtodsinterval(created_t,'SECOND'))<='2017-02-27 18:50:44' order by poid_id0" ]
#SQL= [" SELECT count(*) from pin.event_t where (to_date('1970-01-01','YYYY-MM-DD')+numtodsinterval(created_t,'SECOND'))<='2017-03-07 20:49:51'"]
#HIVE = "SELECT distinct(row_id) FROM increment_test.siebel_nova_siebel_%s_current where created <= \'%s\' order by row_id"%(table_name,created_time) 
#SQL = ["SELECT distinct(poid_id0) from PIN.BILLINFO_T where (to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND')) > to_date('2016-01-01 17:00:00','YYYY-MM-DD HH24:MI:SS')"]
SQL = ["select extract(year from (to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND'))), count(*) from PIN.EVENT_T where (to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND')) <= to_date('2017-04-16 17:00:00','YYYY-MM-DD HH24:MI:SS') and extract(year from (to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND'))) in (2013,2014,2015) group by extract(year from (to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND')))"]
for i in range(0,len(tables)):
# Network drive somewhere
    filename="%s-ora2-output.txt"%(tables[i])
    FILE=open(filename,"w");
    output=csv.writer(FILE, dialect='excel')
    print SQL[i]
# You can set these in system variables but just in case you didnt
#os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1') 
#os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib') 
 
    connection = cx_Oracle.connect('TRACE_APP/Pasword2@10.41.23.127:1521/HBRMPRD')
 
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
