'''
以下是用数组来模拟链表的代码。 目的是为了快因为在c++中 new的动态操作较慢。 所以动态生成的链表用数组来模拟。

NOTE 无论是e数组还是ne数组都是从0开始的。每次操作下标都会增加。所以插入的时候并不是说改变数组种原指针指向的下标的数值和指针，而是加入新的数值和指针然后
调整指针的指向。
'''

N = 100010
head = -1
e = [0] * N
ne = [0] * N
idx = 0

def addToHead(x):
    '''
    在头部插入一个节点。 步骤为：
    1. 将新节点指针 指向head指向的位置。
    2. 将head指针指向的旧指针删掉并指向新节点。
    '''
    global head, e, ne, idx
    e[idx] = x # 第一个节点的值将为x
    ne[idx] = head # 第一个节点的下标将为 -1 （第一步）
    head = idx # head指针指向第一个节点（第二步）
    idx += 1

def remove(k):
    global e, ne
    ne[k] = ne[ne[k]]

def insert(k, x):
    global e, ne, idx
    e[idx] = x
    ne[idx] = ne[k] # 插入的节点指向下标指向的节点 （第一步）
    ne[k] = idx # head指针指向下一个节点（第二步）
    idx += 1

def main():
    global head, e, ne, idx
    n = int(input())
    while(n):
        s = list(input().split(" "))
        if(s[0] == 'H'):
            x = int(s[1])
            addToHead(x)
        elif(s[0] == 'D'):
            k = int(s[1])
            if(k == 0): head = ne[head]
            else: remove(k - 1)
        else:
            k = int(s[1])
            x = int(s[2])
            insert(k - 1, x)
        n -= 1
    i = head
    while(i != -1):
        print(e[i], end=" ")
        i = ne[i]

main()