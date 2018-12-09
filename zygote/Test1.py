from zygote import TestName

c = (1,2,"m",-1,True,False)
a = [3,6,True,0.1,False,'ggg']
for b in a:
    print b,type(b)

print '-----------------'
print range(10)
print a[3:]
print a[-2]
print('king')
if a[0]<a[1]:
    a[0] = a[0]+a[1]
else:a[0] = a[0] - a[1]
print a[0]

print dir(list)
print hasattr(TestName, 'test1')
print('king2')
print hasattr(TestName, 'test')
