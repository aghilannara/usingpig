#!/usr/bin/env python

import csv
import cx_Oracle as ora
import argparse
import time
import pdb

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c','--connection', dest='connection', required=True)
  parser.add_argument('-i','--infile', dest='infile')#, required=True)
  parser.add_argument('-a','--alter', dest='alter')
  parser.add_argument('-f','--filenama', dest='filenama')
  args = parser.parse_args()

  filename = '%s-output-oracle.txt' %(args.filenama)

  con = ora.connect(args.connection)
  cur = con.cursor()

  resultstr = []

  with open(args.infile, 'rb') as csvinfile:
    spamreader = csv.reader(csvinfile)
    for row in spamreader:
      if args.alter == 'yes':
        result = cur.execute("""ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS'""")
        query = "%s"%(row[0])
        
        #pdb.set_trace()
      try:
        print query
        result = cur.execute(query)
        #pdb.set_trace()
        val = cur.fetchall()
        with open(filename, 'a') as csvoutfile:
          fieldnames = ['result']
          writer = csv.DictWriter(csvoutfile, fieldnames=fieldnames)
          print '\n'.join(str(item)for result in val for item in result)
          #result = '\n'.join(str(item)for result in val for item in result)

          writer.writerow({'result' : ','.join(str(item)for result in val for item in result)})
          #pdb.set_trace()
          #writer.writerow({'query': row['query'],'result' : '\n'.join(str(result) for result in val)})
      except ora.DatabaseError, e:
        print e.message
          
          

      #except Exception, e:
       # writer.writerow({'query': row['query'],'result' : e})
        #print e
        #for result in val:
        
          #resultstr.append(' '.join(result))
          #print ' '.join(str(result))
          #for item in result:

          
          #resultstr.append(' '.join(result))

  #print resultstr
          #writer.writerow({'result': row['query'],'result': result})
    cur.close()
    con.close()

main()

