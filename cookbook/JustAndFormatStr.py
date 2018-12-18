#coding=utf8
'''对齐文本字符串'''

text="Hello world!"
#右对齐 总共30个字符
text2=text.rjust(30)
print(text2)
#左对齐 总共30个字符
text3=text.ljust(30)
print(text3)
#居中对齐
text4=text.center(30)
print(text4)
#居中 并用*填充两边字符
text5=text.center(30,'*')
print(text5)

#使用format函数来进行格式化 >表示右对齐 <表示左对齐 ^表示中间对齐 前面的符号是填充的符号
text6=format(text,'*>30')
print(text6)
text7=format(text,'-<30')
print(text7)
text8=format(text,'#^30')
print(text8)

#内建函数format不止可以作用于字符串 也可以作用于数字
text9=format(10,'^30')
print(text9)



