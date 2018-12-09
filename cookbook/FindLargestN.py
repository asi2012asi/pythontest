#coding=utf8
'''找到集合中最大或最小的n个元素'''
import heapq


def pushitem(heap1,item,priority,index):
    heapq.heappush(heap1,(item,priority,index))

def findLargest(coll,n,key=None):
    return heapq.nlargest(n,coll,key)

def findSmallest(coll,n,key=None):
    return heapq.nsmallest(n,coll,key)

def findLargeNDependOnSize(coll,n,key=None):
    if(1==n):
        return max(coll)
    #集合的大小与n相近 距离小于等于10 采用排序的方式求值
    if(coll.__size__-n<=10):
        return sorted(coll)[:n]
    else :
        return findLargest(coll,n,key)

if __name__ == "__main__":
    coll=[3,6,1,4,8,2,9,7]
    largestn=findLargest(coll,3)
    print(largestn)
    smallestn=findSmallest(coll,3)
    print(smallestn)
    human=[{'name':'xiaoming','age':19,'money':8000},
        {'name':'xiaohong','age':18,'money':9000},
        {'name':'xiaowang','age':20,'money':10000},
        {'name':'xiaowang','age':21,'money':6000},
        {'name':'xiaowang','age':28,'money':15000},]
    largestn2=findLargest(human,3,lambda man:man['money'])
    print(largestn2)
    print(type(coll))
    heapq.heapify(coll)
    print(coll)
    #heap中第一个元素始终是最小值
    print(coll[0])
    #继续pop下一个
    print(heapq.heappop(coll))
    print(heapq.heappop(coll))

    print('*'*20)
    dict1={'a':1,'a':2,'b':3}
    print(dict1['a'])
    print(dict1.keys(),dict1.values())
