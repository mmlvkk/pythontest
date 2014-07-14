#coding:utf-8

import logging
import suds.client
from dummy_thread import exit
# from suds.client import Client
logging.basicConfig(level=logging.INFO)

url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# url = 'http://webservice.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl'
# url = 'http://webservice.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx?wsdl'
url = 'http://webservice.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
client = suds.client.Client(url)
# print client

#result = client.service.getDatabaseInfo()
a=1
while a:
    ip_name =  raw_input("请输入你的ip地址（退出输入exit）:")
    if ip_name=='exit':
        print '正常退出'
        exit()
        
    result = client.service.getCountryCityByIp(ip_name)
    print result
    print result
    print type(result)
#     a=0
#     for k, v in enumerate(result):
#         print v[1][1][0]
# print result
# result = client.service.getMobileCodeInfo('170789456')
# logging.info(result)



