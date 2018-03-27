# _*_ coding:utf-8 _*_

import logging
from TestRequest import Testrequest
from ReadExcel import  ReadExcel
from TestReport import Report
import json

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

ReadExcel = ReadExcel()
Testrequest = Testrequest()
TestReport = Report()

class Testcase:



    def __int__(self):
        pass
    def test_case(self,rownum,worksheet,temp):
        self.actual = {}
        self.caseid = ReadExcel.get_cell(rownum,1)
        print self.caseid
        self.testcasename = ReadExcel.get_cell(rownum, 2)
        self.url_path = ReadExcel.get_cell(rownum, 3)
        print self.url_path
        self.method = ReadExcel.get_cell(rownum, 4)
       # self.headers = ReadExcel.get_cell(rownum, 5)

        self.headers = {'Content-Type': 'application/json'}
        print self.headers
        self.requestdata = ReadExcel.get_cell(rownum, 6)
        print type(self.requestdata)

        self.hope = ReadExcel.get_cell(rownum, 7)
        print  self.hope
        if self.method == "POST":
            logging.debug('使用%s方法执行用例%s' % (self.method, self.caseid))
            try:
                self.actual = Testrequest.Testpostrequest(self.url_path, self.requestdata, self.headers, self.caseid, self.testcasename,

                                                       self.hope)
                print 'type ======='
                print   type(self.actual)
                print 'type 88888='
                print self.actual
                logging.debug('用例%s执行完毕' % self.caseid)
            # except Exception:
            #     logging.error('参数缺失')
            finally:
                TestReport.write_basic(self.caseid, self.testcasename, self.method, self.hope, self.url_path, self.requestdata, worksheet,
                                       temp)
                logging.info("基本数据写入成功")

                TestReport.write_special(self.actual, self.hope, worksheet, temp)
            logging.debug("特殊数据写入成功")

        elif self.method == "GET":
            logging.debug('使用%s方法执行用例%s' % (self.method, self.caseid))
            try:
                self.actual = Testrequest.Testpostrequest(self.url_path, self.requestdata, self.headers, self.caseid,
                                                          self.testcasename,
                                                          self.hope)
                logging.debug('用例%s执行完毕' % self.caseid)
            except Exception:
                logging.error('参数缺失')
            finally:
                TestReport.write_basic(self.caseid, self.testcasename, self.method, self.hope, self.url_path,
                                       self.requestdata, worksheet,
                                       temp)
                logging.info("基本数据写入成功")
                TestReport.write_special(self.actual, self.hope, worksheet, temp)
            logging.debug("特殊数据写入成功")
        else:
            TestReport.write_basic(self.caseid, self.testcasename, self.method, self.hope, self.url_path, self.requestdata, worksheet,
                               temp)
            TestReport.write_cell(worksheet, "G%s" % temp, "调用方法错误")
            TestReport.write_cell(worksheet, "H%s" % temp, "失败")
            logging.error('没有%s对应的方法%s' % (self.caseid, self.method))
        TestReport.close_workbook()

def main():
    TestReport.test_detail()
    case = Testcase()
    sheet1 = TestReport.get_sheet1()
    case.test_case(1,sheet1,3)



if __name__ == '__main__':
    main()



