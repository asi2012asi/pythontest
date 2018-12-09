#coding=utf8
'''搜索包含关键字的某行，并且显示他的前面n行'''
from collections import deque


def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)#一直保存最新的5行

if __name__=="__main__":
    with open('../zygote/Test1.py') as f:
        for line,previous_line in search(f,'king',5):
            for pline in previous_line:
                print(pline,end="")
            print(line,end="")
            print('*'*20)
