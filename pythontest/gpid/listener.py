#!/usr/bin/env python
"""
kwang 2014年8月13日16:23:47  readme : gqid install failure. So test failure
"""
import os
import sys
import time

from proton import *

user = os.getenv('ACTIVEMQ_USER') or 'admin'
password = os.getenv('ACTIVEMQ_PASSWORD') or 'password'
host = os.getenv('ACTIVEMQ_HOST') or '127.0.0.1'
port = int(os.getenv('ACTIVEMQ_PORT') or 5672)
destination = sys.argv[1:2] or ['topic://event']
destination = destination[0]

msg = Message()
mng = Messenger()
mng.password=password
mng.start()
mng.subscribe("amqp://%s@%s:%d/%s"%(user, host, port, destination))

count = 0
start = time.time()
while True:
  mng.recv(10)
  while mng.incoming:
    mng.get(msg)
    if msg.body=="SHUTDOWN":
      diff = time.time() - start
      print 'Received %d frames in %f seconds' % (count, diff)
      exit(0)
    else:
      if count==0:
        start = time.time()
      count+=1
      if count % 1000 == 0:
        print 'Received %d messages.' % (count)

mng.stop()