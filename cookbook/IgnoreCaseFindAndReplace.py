#coding=utf8
'''忽略大小写的替换和查找'''

#re有个flag 专门用作在sub和find的时候忽略大小写 ignorecase
import re

str1="i come from guangzhou !"
findsome=re.findall(r'GUANGZHOU',str1)
print(findsome)
#使用ignorecase后
findsome2=re.findall(r'GUANGZHOU',str1,flags=re.IGNORECASE)
print(findsome2)