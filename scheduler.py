import subprocess
import shlex
from datetime import date,datetime

exec_time = datetime(2017,3,7,4,0,0,0)
#exec_time = datetime(2017,2,17,5,0,0,0)
i = 0
print "The time now is %s"%(datetime.now())
print "The oracle table will start output the result  at %s"%(exec_time)

while datetime.now() < exec_time:
        i = 0
        #print 'hello'
else:
        print datetime.now()
        cmd = 'files/scripts/test_oracle.py'
        splitted = shlex.split(cmd)
        print splitted
        subprocess.call(splitted)
	'''
	cmd2 = 'hdfs dfs -put 20170221-s_asset_xm-output.txt /user/trace/pig/s_asset_xm-ora-output.txt'
	splitted2 = shlex.split(cmd2)
	subprocess.call(splitted2)

	cmd4 = 'pig -f run_pig.hql'
	splitted4 = shlex.split(cmd4)
	print splitted4
	subprocess.call(splitted4)'''
