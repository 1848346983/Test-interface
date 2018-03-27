# _*_ coding:utf-8 _*_
import xlrd

import urllib2
import urllib
import json
import requests
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data = {"request":{"head":{"src_chid":"BC_TDHL","dest_chid":"BC_CEB","tx_code":"BC10010001","tx_msgno":"20180226098765432"},"metadata":{"id":"2017071000001","product_id":"660009","trans_date":"2017-07-10","date":"2017-07-10","transfertype_id":"026","amount":"10000.34","payer_acct_name":"同业证券公司","payer_acct_number":"35500188067646196","payer_org_name":"中国光大银行北京分行本部","payee_acct_name":"shoukuanhuming","payee_acct_number":"30000446457777544","payee_org_name":"jiansheyinhang","payee_large_paymentno":"200345897612","summary":"yibanhuakuan"}}}


headers = {'Content-Type': 'application/json'}

request = urllib2.Request(url='http://192.168.103.21:9098/Service'
, headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
print  response

request1 = requests.post(url='http://192.168.103.21:9098/Service', headers=headers, data=json.dumps(data) )
resonse1 = json.dumps(request1.text)# str
resonse3 = json.loads(request1.text) #

resonse2 = json.loads(resonse1) #

a =  resonse1.replace('\\','')
b = eval(a)

print a.strip('"')
print a

print  resonse1
print  resonse3
print resonse3.keys()
print  type(resonse1)
print type(resonse2)
#print type(resonse3)

if resonse3['response']['head']['error_code'] == '0000':
    print 'ok'



