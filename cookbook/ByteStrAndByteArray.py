#encoding=utf8
'''在字节串上执行本文操作'''

#与处理字符串差不多一样
data=b'Hello World'
print(data.startswith(b'Hell'))
print(data.split())

#不但可以对字节串做操作 也可以对字节数组做操作
arr=bytearray(data)
print(arr.endswith(b'ld'))