it = iter(range(10))
try:
    for i in range(100):
        print it.next()
except StopIteration:
    print 'it is end ! i = ',i

try:
    raise NameError
except NameError:
    print 'i catch you ! nameError ahahah'
