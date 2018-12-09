#coding=utf8
class Person(object):
    age = 10
    name = 'no name'
    sex = 'boy'
    def __init__(self,age,name,sex):
        self.age = age
        self.name = name
        self.sex = sex

    def saySomething(self):
        print 'Hello , my name is '+self.name+", I am "+self.age+" years old, I am a "+self.sex


class Teacher(Person):
    def doSomething(self):
        self.saySomething()
        print 'otherwise , I am a teacher.'


xiaoming = Person('20','xiaoming','boy');
xiaoming.saySomething()
lilei = Teacher('40','lilei','boy')
lilei.doSomething()
print 'somebody say '+lilei.name+" is a good teacher!"

# 测试类名 和名称
a = [1, 2, 3]
print a.__class__
print a.__class__.__name__

