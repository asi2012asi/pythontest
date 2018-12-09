import platform
def laugh():
    print ('hhahaaa')
    print(platform.python_version())

#laugh()
ta = [1,2,3]
tb = [9,8,7]
zipped = zip(ta,tb)
print(zipped)
print(type(zipped))
na, nb = zip(*zipped)
print(na, nb)