#coding=utf8
'''在字符串的开头和结尾做文本匹配'''

#使用startwith和endwith来做开头和结尾的文本匹配 如果有多个需要匹配的项 可以传入元组
import os

filelist=os.listdir('.')
print(filelist)
txtfilename=[filename for filename in filelist if filename.endswith('txt') ]
print(txtfilename)
startwithfindandname=[filename for filename in filelist if filename.startswith(('Find','Name')) ]
print(startwithfindandname)
