import time
import sys

import stomp

class MyListener(object):
    def on_error(self, headers, message):
        print 'received an error %s' % message

    def on_message(self, headers, message):
        print 'received a message %s' % message

conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect()

conn.subscribe(destination='/queue/test',id='wangkang', ack='auto')

conn.send( destination='/queue/test',body='fffffffffffewewe')
conn.send( destination='/queue/test',body='22222222ewe')

time.sleep(2000)
conn.disconnect()