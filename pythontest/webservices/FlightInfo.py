#coding:utf-8
'''
Created on 2014-6-24

@author: a
'''
import logging
from suds.client import Client
logging.basicConfig(level=logging.INFO)
url = 'http://webservice.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl'
client = Client(url)
logging.info(client)
#result = client.service.getDatabaseInfo()

result = client.service.getMobileCodeInfo('170789456')
print result
#查看该service提供的方法