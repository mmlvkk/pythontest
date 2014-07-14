'''
Created on 2014-5-29

@author: a

'''

import sys
import os
import glob
import test.hello_world as tt
if __name__ == '__main__':
    print tt.os_port()


reload(sys).setdefaultencoding('UTF-8')
sys.dont_write_bytecode = True
sys.path += glob.glob('%s/*.egg' % os.path.dirname(os.path.abspath(__file__)))
#print sys.path