'''
lowbit: 一个数的二进制表示中最低位的1所对应的值
比如：
x = 1010 lowbit(x) = 10
x = 10100 lowbit(x) = 100

lowbit(x) = x & -x = x & (~x + 1)
负数是取反(~x)加1 

应用： 统计x里有多少个1。 方法就是一直去掉最低位的1，直到x为0
'''

def lowbit(x):
    return x & -x

def countOnes(x):
    res = 0
    # 当x不为0的时候
    while x:
        x -= lowbit(x)
        res += 1
    return res

print(countOnes(10))