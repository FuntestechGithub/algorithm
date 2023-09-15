'''
n的二进制表示中第k位是几?

二进制中 个位数是0 以此类推。 例如 5的二进制是101, 5的第0位是1, 第1位是0, 第2位是1

步骤：
1. 先把第k位一刀最后一位。 
2. 在看各位是几 X & 1 ( X & 1 是取X 二进制数的最低位. X 为偶数，最低位 0，X 为奇数，最低位 1。)

公式： n >> k & 1

'''

def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])


n = 10
k = 3 
decimal_number = dec2bin(n)
print (decimal_number)
# 将n的二进制表示中所有位数表示出来 （备注右移0位等于不变，k=3的意思位右移最高位到各位）
for i in range(k,-1,-1):
    print(n >> i & 1)




