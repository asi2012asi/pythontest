f2 = open('TestDict.py','a')
f2.write('1')
f2.close()
f = open('TestDict.py','r')
content = f.readlines()
print type(content)
print content
f.close()

f3 = open('SecondModule.py','r')
for line in f3:
    print line
# print f3.next() indeed it is a iterator
f3.close()