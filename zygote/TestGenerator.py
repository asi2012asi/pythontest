def gen():
    a = 100
    yield a
    a = 8**8
    yield a
    yield 10

for i in gen():
    print (i)

g = (x for x in range(10))
print (g,type(g))
print (g.__next__())
print (g.__next__())
print (g.__next__())

L = [x**2 for x in range(10)]
print (L,type(L))

#相当于下面
# L = []
# for x in range(10):
#     L.append(x**2)
# print (L,type(L))