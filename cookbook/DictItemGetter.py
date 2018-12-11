#coding=utf8
'''我们想创建一个字典 其本身是另一个字典的子集'''

mydict0={'x':1,'y':2,'z':3}

mydict={key:value for key,value in mydict0.items() if value>2 }
print(mydict)
#将元组传给词典也可以创建一个词典
mydict2=dict(((key,value) for key,value in mydict0.items() if value>2 ))
print(mydict2)