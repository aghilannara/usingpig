import cx_Oracle
import pdb

#con = cx_Oracle.connect('TRACE_APP/Pasword2@10.41.63.50:1521/CPC2PRD')
con = cx_Oracle.connect('TRACE_APP/Pasword2@10.41.23.127:1521/HSBLPRD')
cur = con.cursor()
cur.execute("alter session set nls_date_format = 'YYYY-MM-DD HH24:MI:SS'")
cur.execute("select distinct(row_id) from siebel.s_asset_xm where created<='2017-02-17 17:31:26'")
lines =[]
for result in cur:
    line = "%s\n"%(result[0])
    lines.append(line)

with open('s_asset_xm-ora-output.txt','w') as f:
    f.writelines(lines)       
pdb.set_trace()
cur.close()
con.close()
