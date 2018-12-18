#coding=utf8
'''以固定的列数重新格式化文本 可以使用textwrap来重新格式化文本的输出 有wrap和fill等函数方便使用'''
import textwrap

print(__doc__)
print(textwrap.fill(__doc__,10))
print('*'*30)
#定义一个段落 前面空两格
print(textwrap.fill(__doc__,10,initial_indent='  '))
print('*'*30)
#定义一个段落 后面空两格
print(textwrap.fill(__doc__,10,subsequent_indent='  '))
print('*'*30)
#返回一个包含每一行的列表
print(textwrap.wrap(__doc__,10,initial_indent='  '))

