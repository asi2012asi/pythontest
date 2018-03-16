def saySomething():
    print 'i am a man'

def doSomething():
    print 'i have haven a lunch'

def watchSomething():
    print  'i am watching tv'

def sumNumber(*num):
    sum = 0
    for item in num:
        sum  = sum+item
    return sum

def sumRange(num):
    if num == 0:
        return 0
    elif num < 0:
        print 'num should be bigger than 0'
        return 0
    sum = 0
    for item in range(num):
        sum = sum+item
    return sum
dict
def printScore(**scorelist):
    for item in scorelist:
        print item,type(item)

    print scorelist.values()

def printScore2(dic):
    for i in range(0,len(dic),1):
        print dic[i]


def printScore3(li):
    for i in range(0, len(li), 2):
        print li[i]

def printNum2(*num):
    for (index,value) in enumerate(num):
        print 'use printNum2'
        print index
        print value






