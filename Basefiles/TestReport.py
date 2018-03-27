# _*_ coding:utf-8 _*_

import xlsxwriter
import time
import logging
from Readconfig import ReadConfig
loadReadConfig = ReadConfig()
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class Report:
    rpaddress=loadReadConfig.get_config("filebase","report_address")
    now = time.strftime("%Y-%m-%d-%H-%M-%S ", time.localtime(time.time()))
    repor_tddress = rpaddress + now + 'report.xlsx'
    workbook = xlsxwriter.Workbook(repor_tddress)  # 生成的报告的路径
    worksheet1 = workbook.add_worksheet("测试详情")

    def __int__(self):
        pass

    def get_workaddress(self):
        '''获取生成的excel地址'''
        return self.repor_tddress

    def get_sheet1(self):
        '''获取sheet2表'''
        return self.worksheet1

    def get_format(self, font_size=14, bg_color='#C7EDCC', font_color='#000000', num=1):
        '''
        设置单元格样式
        font_size: 字体大小（默认12号）
        bg_color: 背景色值（默认豆绿色）
        font_color: 字体色值（黑色）
        num: 是否有边框（1表示有）
        '''
        cell_style =  self.workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'border': num, 'font_size': font_size, 'bg_color': bg_color,
             'font_color': font_color})
        return cell_style
    def write_cell(self, worksheet, cl, data):
        '''
        单元格写入数据
        worksheet: 工作表
        cl: 单元格
        data: 数据
        wd: excel表
        '''
        return worksheet.write(cl, data, self.get_format())

    def write_basic(self, testcassid, testcassname, method, hope, url, data, worksheet, temp):
        '''
        把基本数据写入excel
        testcassid: 用例ID
        testcassname: 用例名称
        method: 用例方法
        hope: 预期code
        url: 接口地址
        data: 请求数据
        worksheet: 写入的工作表
        temp: 写入的行数
        '''
        item = {"t_id": testcassid, "t_name": testcassname, "t_method": method, "t_url": url,
                "t_param": '%s' % data, "t_hope": 'code: %s' % hope}
        self.write_cell(worksheet, "A" + str(temp), item["t_id"])
        self.write_cell(worksheet, "B%s" % temp, item["t_name"])
        self.write_cell(worksheet, "C%s" % temp, item["t_method"])
        self.write_cell(worksheet, "D%s" % temp, item["t_url"])
        self.write_cell(worksheet, "E%s" % temp, item["t_param"])
        self.write_cell(worksheet, "F%s" % temp, item["t_hope"])
    def write_special(self, actual, hope, worksheet, temp):
        '''
        把结果写入excel
        actual: 接口返回结果
        '''
        if actual == {}:
            self.write_cell(worksheet, "G%s" % temp, "参数缺失")
            self.write_cell(worksheet, "H%s" % temp, "失败")
        elif actual['response']['head']['error_code'] == hope:
            self.write_cell(worksheet, "G%s" % temp, "error_code：%s，msg：%s" % (actual['response']['head']['error_code'], actual['response']['head']["error_msg"]))
            self.write_cell(worksheet, "H%s" % temp, "通过")
        elif actual['response']['head']['error_code'] != hope:
            #self.write_cell(worksheet, "G%s" % temp, "error_code：%s，msg：%s" % (actual['response']['head']['error_code'], actual['response']['head']["error_msg"]))
            self.write_cell(worksheet, "H%s" % temp, "失败")
    def test_detail(self):
        '''创建测试详情表'''
        # 设置列宽
        self.worksheet1.set_column("A:A", 20)
        self.worksheet1.set_column("B:B", 20)
        self.worksheet1.set_column("C:C", 20)
        self.worksheet1.set_column("D:D", 20)
        self.worksheet1.set_column("E:E", 20)
        self.worksheet1.set_column("F:F", 20)
        self.worksheet1.set_column("G:G", 20)
        self.worksheet1.set_column("H:H", 20)

        # 生成工作表内容
        self.worksheet1.merge_range('A1:H1', '测试详情', self.get_format(14, "blue", "#ffffff"))
        self.write_cell(self.worksheet1, "A2", '用例ID')
        self.write_cell(self.worksheet1, "B2", '接口名称')
        self.write_cell(self.worksheet1, "C2", '接口方法')
        self.write_cell(self.worksheet1, "D2", 'URL')
        self.write_cell(self.worksheet1, "E2", '参数')
        self.write_cell(self.worksheet1, "F2", '预期结果')
        self.write_cell(self.worksheet1, "G2", '实际结果')
        self.write_cell(self.worksheet1, "H2", '测试结果')
        logging.info('测试详情表创建成功')

    def close_workbook(self):
        self.workbook.close()
        logging.debug('工作表关闭成功')

def main():
    re = Report()
    re.test_detail()
    re.close_workbook()

if __name__ == '__main__':
    main()