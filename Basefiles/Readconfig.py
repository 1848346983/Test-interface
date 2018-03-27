# _*_ coding:utf-8 _*_
import os
from configparser import ConfigParser
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

prodir = os.path.split(os.path.realpath(__file__))[0] #获取当前文件路径
configpath = os.path.join(prodir,'Config.ini') #获取指定文件的完整路径

class ReadConfig:
    def __int__(self):
        pass


    def get_config(self,fileid,key):
        self.v = ConfigParser()
        self.v.read(configpath)
        result = self.v.get(fileid,key)
        return result
def main():
    config = ReadConfig()
    config.get_config("filebase","case_address")


if __name__ == '__main__':
    main()