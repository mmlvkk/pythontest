# -*- coding: GBK -*- 
import subprocess
#coding:utf-8
cmd="cmd.exe"
begin=72
end=73
while begin<end:

    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
                   stdin=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    p.stdin.write("ping 192.168.3."+str(begin)+"\n")

    p.stdin.close()
    p.wait()

#     print "execution result: %s"%p.stdout.read()
    print p.stdout.read()
    begin +=1