#coding=utf8
'''针对任意多的分隔符拆分字符串'''

#使用字符串对象自身的split方法只能处理非常简单的情况 而且不支持多个分隔符
import re

str1='dad da;144,8811,d000ureqe-c1f87dac  fpp'
print(str1.split(','))
#使用re.split可以处理多个分隔符的情况 \s是一个空格 \s*是0个或多个空格
print(re.split(r'[\s,;-]\s*',str1))

#使用捕获组 对数据分组 分割字符也会包含在分组内
result=re.split(r'(\s|,|;|-)\s*',str1)
print(result)
#通过过滤可以得到分割后的数据或分割字符
print(result[::2])
print(result[1::2])
#要处理掉这些分隔符 但是又有捕获组 可以在分组内加入?:
result2=re.split(r'(?:\s|,|;|-)\s*',str1)
print(result2)