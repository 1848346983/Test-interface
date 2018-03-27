# coding=utf-8
import xlrd
from selenium import webdriver
xls = xlrd.open_workbook('sample.xls')
sheet = xls.sheets()[0]

try:
    num = 20
    guess = int(input("please intput  a  number："))
    if guess < 0:
        print 'dsd'
    while guess > 0:
        if guess > num:
            print 'big'
            guess = input("please intput  a  number：")
            continue
        elif guess < num:
            print 'smaller'
            guess = input(" please intput  a  number：")
            continue
        else:
            print 'ok值相等'
            break
except StandardError:
    print '输入的值的类型不匹配'

# finally:
#     print '2222'
