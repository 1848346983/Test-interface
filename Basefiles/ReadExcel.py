# _*_ coding:utf-8 _*_
import xlrd
from Readconfig import ReadConfig
loadReadConfig = ReadConfig()
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class ReadExcel:
    case_address = loadReadConfig.get_config("filebase", "case_address")
    workbook = xlrd.open_workbook(case_address)

    table = workbook.sheet_by_index(0)
    def __int__(self):
        pass


    def get_rows(self):

        rows = self.table.nrows
        return rows
    def get_cell(self,row,col):
        cell_data = self.table.cell(row,col).value
        return cell_data
    def get_col(self,col):
        col_data = self.table.col_values(col)
        return col_data
def main():
        excel_data = ReadExcel()
        print (excel_data.get_cell(1,2))
        print (excel_data.get_col(2))
        print(excel_data.get_rows(1).encode('utf-8'))


if __name__ == '__main__':
    main()






