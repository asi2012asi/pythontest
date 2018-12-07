f2 = open('TestDict.py', 'a')
f2.write('1')
f2.close()
f = open('TestDict.py', 'r')
content = f.readlines()
print (type(content))
print (content)
f.close()

f3 = open('SecondModule.py', 'r')
for line in f3:
    print (line)
# print f3.next() indeed it is a iterator
f3.close()

with open('TestDict.py','r') as fileDict:
    print(type(fileDict))
    print("fileDict line count = ",fileDict.readlines().__len__())

value = input("please your name:\n")
print(value)
floatvalue1 = float(value)
print(floatvalue1)
print(type(floatvalue1))
print(isinstance(floatvalue1,float))
