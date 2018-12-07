# -*- coding = utf-8 -*-

def _private_sound():#定义私有方法 编程习惯上不应该使用该方法
    print ("walalalla")

def talk():
    _private_sound()

if __name__ == "__main__":
    talk()