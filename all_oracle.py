import os
import cx_Oracle
import csv
 
#SQL="SELECT distinct(row_id) FROM siebel.s_evt_act where created > '2016-06-01 00:00:00' order by row_id"
SQL="select max((to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(created_t,'SECOND'))) created_t, max((to_date('1970-01-01','YYYY-MM-DD') + numtodsinterval(mod_t,'SECOND'))) mod_t from pin.event_t" 
# Network drive somewhere
filename="event_t-output.txt"
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
 
# You can set these in system variables but just in case you didnt
#os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1') 
#os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib') 
 
connection = cx_Oracle.connect('TRACE_APP/Pasword2@10.41.23.127:1521/HBRMPRD')
 
cursor = connection.cursor()
cursor.execute("alter session set nls_date_format = 'YYYY-MM-DD HH24:MI:SS'")
cursor.execute(SQL)
for row in cursor:
    output.writerow(row)
cursor.close()
connection.close()
FILE.close()
