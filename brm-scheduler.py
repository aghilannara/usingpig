import subprocess
import shlex
from datetime import date,datetime

exec_time = datetime(2017,2,25,16,1,0,0)
#exec_time = datetime(2017,2,17,5,0,0,0)
i = 0
print "The time now is %s"%(datetime.now())
print "The oracle table will start output the result  at %s"%(exec_time)

while datetime.now() < exec_time:
        i = 0
        #print 'hello'
else:
        #print datetime.now()
        #cmd = 'python files/scripts/brm-test_oracle.py'
        #splitted = shlex.split(cmd)
        #print splitted
        #subprocess.call(splitted)

        cmd2 = 'hdfs dfs -put event_t-*.txt /user/trace/pig/'
        splitted2 = shlex.split(cmd2)
        subprocess.call(splitted2)

        cmd4 = 'pig -f run_pig.hql'
        splitted4 = shlex.split(cmd4)
        print splitted4
        subprocess.call(splitted4)
        
        cmd5 = 'hdfs dfs -get /user/trace/pig/event_t-diff_data files/result/'
        splitted5 = shlex.split(cmd5)
        print splitted5
        subprocess.call(splitted5)
