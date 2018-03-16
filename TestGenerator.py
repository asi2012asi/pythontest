def gen():
    a = 100
    yield a
    a = 8**8
    yield a
    yield 10

for i in gen():
    print i

g = (x for x in range(10))
print g,type(g)
print g.next(),g.next(),g.next()