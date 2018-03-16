# -*- coding: UTF-8 -*-

# 1.能被4整除 不能被100整除  2.能被400整除

def isRuannian(year):
    if year%4 == 0 and year %100 !=0:
        return True
    elif year%400 == 0:
        return True
    else:return False

print isRuannian(2008)
print isRuannian(2009)
print isRuannian(2016)
print isRuannian(2018)
print isRuannian(2019)