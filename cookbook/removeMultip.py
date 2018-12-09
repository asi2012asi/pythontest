# coding=utf8
'''从序列中移除重复项目且保持元素间的顺序不变'''


# 使用这种方式的话 item必须是可哈希的 即不可变的
def dedupe1(items):
    # 创建一个集合用来往里面放数据
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 使用这个函数可以传递一个函数变量为key 对不可哈希的item做进一步运算后再求值
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        #下面这句话相当于java的三目运算符 val=(key==null)?item:key(item)
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__=="__main__":
    a=[1,20,1,3,4,1,7,6,1,9,1]
    print(list(dedupe1(a)))
    b=[{'x':1,'y':2}, {'x':1,'y':3},{'x':2,'y':3},{'x':3,'y':4}]
    #前面两个x:1 重复了 所以只取第一个
    print(list(dedupe2(b,lambda item:item['x'])))
    #去除重复项最简单的做法是直接运行set 但是不一定能保证元素原来的顺序
    print(set(a))