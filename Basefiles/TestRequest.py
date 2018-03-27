# _*_ coding:utf-8 _*_
import requests
import json
import logging

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

passcase = 0

class Testrequest:


    def __int__(self):
        pass

    def Testpostrequest(self,url,data,headers,caseid,casename,hope):
        global passcase

        request = requests.post(url, data=json.dumps(data).replace('\\','').encode('utf-8').strip('"'),headers=headers)
        responses = json.loads(request.text)
        print type(json.dumps(data).replace('\\','').encode('utf-8')),json.dumps(data).replace('\\','').encode('utf-8')
        print json.dumps(data).replace('\\','').encode('utf-8').strip('"')
        print '++++++++-----'
        print type(responses)
        print responses['response']['head']['error_code']
        if hope == responses['response']['head']['error_code']:

            passcase += 1
            logging.info("测试用例id: %s" % caseid)
            logging.info("用例名称: %s" % casename)
            logging.debug("测试通过")
            logging.debug('测试返回数据：%s' % responses)
            logging.debug('测试返回code数据：%s' % responses['response']['head']['error_code'])
        else:

            logging.info("测试用例id: %s" % caseid)
            logging.info("用例名称: %s" % casename)
            logging.debug("测试失败")
            logging.debug('测试返回数据：%s' % responses)
            logging.debug('测试返回code数据：%s' % responses['response']['head']['error_code'])
        return responses

    def Testgetrequest(self,url,data,headers,caseid,casename,hope):

        global passcase1
        request = requests.post(url,data=data,headers=headers)

        responses = json.loads(request.text)
        print responses['response']['head']['error_code']

        if responses['response']['head']['error_code'] == hope:
            passcase1 += 1
            logging.info("测试用例id: %s" % caseid)
            logging.info("用例名称: %s" % casename)
            logging.debug("测试通过")
            logging.debug('测试返回数据：%s' % responses)
            logging.debug('测试返回code数据：%s' % responses['response']['head']['error_code'])
        else:

            logging.info("测试用例id: %s" % caseid)
            logging.info("用例名称: %s" % casename)
            logging.debug("测试失败")
            logging.debug('测试返回数据：%s' % responses)
            logging.debug('测试返回code数据：%s' % responses['response']['head']['error_code'])
            return responses
def main():
    data = {"request": {"head": {"src_chid": "BC_TDHL", "dest_chid": "BC_CEB", "tx_code": "BC10010001",
                                 "tx_msgno": "20180226098765432"},
                        "metadata": {"id": "2017071000001", "product_id": "660009", "trans_date": "2017-07-10",
                                     "date": "2017-07-10", "transfertype_id": "026", "amount": "10000.34",
                                     "payer_acct_name": "同业证券公司", "payer_acct_number": "35500188067646196",
                                     "payer_org_name": "中国光大银行北京分行本部", "payee_acct_name": "shoukuanhuming",
                                     "payee_acct_number": "30000446457777544", "payee_org_name": "jiansheyinhang",
                                     "payee_large_paymentno": "200345897612", "summary": "yibanhuakuan"}}}
    print type(data)

    headers = {'Content-Type': 'application/json'}

    testp = Testrequest()
    testp.Testpostrequest(url='http://192.168.103.21:9098/Service',data = json.dumps(data), headers=headers, caseid='1-1' , casename='查看医生信息', hope='0000')

if __name__ == '__main__':
    pass



