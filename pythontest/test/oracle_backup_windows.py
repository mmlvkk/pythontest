#!/usr/bin/env python
# -*- coding: GBK -*- 

#Name    : oracle_backup.py
#Author  : mmlvkk
#Mail    : mmlvkk@163.com
#Time    : 2014-07-02
#For     : Backup oracle databases on windows
#Version : 0.0.1 Beta
#Steps   :
# 1.backup databases
# 2.gzip backup
# 3.upload backup to ftp server

import os,gzip
# from ftplib import FTP
from ftplib import FTP_TLS
from datetime import datetime


# reload(sys)
# sys.setdefaultencoding('utf-8')

#oracle related
dmpdir = 'd:\\app\\backup_restore\\exp_backup\\'
dmpname = datetime.now().strftime('%Y%m%d')
dbhost = "127.0.0.1"
dbuser = "sa"
dbpass = "topsci"

#ftp related
isftp = 1
ftphost = 'ftp.cm-topsci.com'
ftpuser = 'kwang'
ftppass = 'dengken21'
ftpport = '15121'
ftppath ='''/ftp'''

nowdate = datetime.now().strftime('%Y%m%d')

'''
return :
    0: 
    1:备份成功
    2:备份目录不存在
'''
def backup_expdp():
    try:
        global dmpname 
        
        if os.path.exists(dmpdir):
            while  os.path.exists(dmpdir+dmpname+'.dmp'):
                dmpname = dmpname+ '_0'
            print dmpdir+dmpname+'.dmp'
            os.system('expdp sa/topsci@NNDB directory=dmpdir dumpfile={}.dmp schemas=sa exclude=statistics'.format(dmpname))
            return 1
        else:
            print "备份目录不存在"
            return 2
    except Exception,e:
        print  e
    
 
def gzip_db(dmpdir,dbname):
    print dmpdir
    print dbname
    
    gzip_in = open('{}{}.dmp'.format(dmpdir,dbname) , 'rb')
    gzip_out = gzip.open('{}{}.dmp.gz'.format(dmpdir,dbname) , 'wb')
    gzip_out.writelines(gzip_in)
    gzip_out.close()
    gzip_in.close()
    os.remove('{}{}.dmp'.format(dmpdir,dbname))



def ftp_backup(dmpdir,dbname):

    try:
#        
        ftp =FTP_TLS()
        ftp.connect(ftphost,ftpport)
        ftp.login(ftpuser,ftppass)
        ftp.prot_p()   
        print "Welcome:",ftp.getwelcome()
        print ftp.retrlines('LIST')
#         ftp =FTP()
#         ftp.connect(ftphost,ftpport)
#         ftp.login(ftpuser,ftppass)
#         print "Welcome:",ftp.getwelcome()
#         print ftp.retrlines('LIST')
    except Exception,e:
        print  e
        return
    try:
        ftp.cwd('./pub/upload/INFOAIR_NNG')
        print ftp.retrlines('LIST')
    except Exception,e:
        print e
#         print '''mkdir %s/%s''' %(ftppath,dbname)
#         ftp.mkd('''%s/%s''' %(ftppath,dbname))
#         ftp.cwd('''%s/%s''' %(ftppath,dbname))
 
    fd = open('{}{}.dmp.gz'.format(dmpdir,dbname),'rb')
    ftp.storbinary('STOR %s' % os.path.basename('{}{}.dmp.gz'.format(dmpdir,dbname)),fd)
    fd.close()
    ftp.retrlines('LIST')

    ftp.quit()

if __name__ == '__main__':
    backup_expdp()
    gzip_db(dmpdir,dmpname)
    ftp_backup(dmpdir,dmpname)
    
    