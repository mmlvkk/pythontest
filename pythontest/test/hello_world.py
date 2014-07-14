#coding:utf-8
'''
Created on 2014-5-28

@author: a
'''


import os

def os_port():
    print 'os_port'
    return os.getcwd();

if __name__ == '__main__':
    print '45在'
    
    win_port = os.system('dir')
    print win_port
    print type(win_port)
    
    from ftplib import FTP_TLS
    ftps = FTP_TLS('ftp.python.org')
    ftps.login()           # login anonymously before securing control channel
    ftps.prot_p()          # switch to secure data connection
    ftps.retrlines('LIST') 
    
else:
    print 'else'




