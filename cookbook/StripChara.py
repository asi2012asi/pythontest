#encoding=utf8

'''处理不需要的字符'''

#strip函数可以处理左右两则不需要的字符 默认是空格
import re

str=' balaba     labala \n'
print(str)
str1=str.strip()
print(str1)
#左清除
str2=str.lstrip()
print(str2)
#右清除
str3=str.rstrip()
print(str3)
#也可以指定清除特殊的字符
str4='---windows####'
str5=str4.strip('-#')
print(str5)
#strip不会对中间进行清除 要对中间进行替换 可以使用replace或者re.sub函数
str6=re.sub(r'\s+'," ",str1)
print(str6)
