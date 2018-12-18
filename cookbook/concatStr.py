#coding=utf8
'''连接字符串'''

#java中的连接字符串很简单 两个字符串间使用+即可 python类似
str1="hello "
str2="world"
num = 1000
str3=str1+str2
print(str3)
#连接数字
str4=str3+str(num)
print(str4)

#连接列表 字典 元组 序列 都可以使用str 自带的str
arr=['i','am','a','cool','guy','!']
arr2=('i','am','a','cool','guy','!')
arr3={'a':'我','b':"带",'c':"你"}
str5=" ".join(arr)
print(str5)
str6="&".join(arr2)
print(str6)
str7="%".join(arr3)
print(str7)

#如果不需要变量名拼接 最简单是这样
str8="well"" come on!"
print(str8)

#与java类似 python也不推荐使用+连接字符串 影响内存拷贝和垃圾回收 除非是很简单和少次数的 一般采用join是最好的
#如果只是非常简单的加连接符打印 可以使用string自带的sep
print(str1,str2,sep=",")
