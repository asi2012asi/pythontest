a = [1,2,3,4,5]
b = [3,4,5]

class superList(list):
    def __sub__(self, other):
        me = self[:]
        other1 = other[:]
        for item in other:
            if item in me:
                me.remove(item)
        return me

c = superList(a) - superList(b)
# print c

xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print L
