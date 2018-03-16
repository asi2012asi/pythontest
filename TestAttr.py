#coding=utf8

# define class
class Me(object):
    def test(self):
        print "Hello!"

def new_function():
    print "New Hello!"

me = Me()

print hasattr(me,"test")
print hasattr(me,"new_function")
print getattr(me,"test")
setattr(me,"test",new_function)
# me.new_function()
print hasattr(me,"new_function")