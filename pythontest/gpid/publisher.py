#!/usr/bin/env python
"""
kwang 2014年8月13日16:23:47  readme : gqid install failure. So test failure
"""tations under the License.

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
address = "amqp://%s@%s:%d/%s"%(user, host, port, destination)

msg = Message()
mng = Messenger()
mng.password=password
mng.start()

messages = 10000

msg.address = address
msg.body = unicode('Hello World from Python')

count = 0
start = time.time()
for _ in xrange(messages):
  mng.put(msg)
  count += 1
  if count % 1000 == 0 :
    print("Sent %d messages"%(count))

msg.body = unicode("SHUTDOWN")
mng.put(msg)
mng.send

diff = time.time() - start
print 'Sent %s frames in %f seconds' % (count, diff)

mng.stop()