'''
题目链接： https://www.acwing.com/problem/content/792/

思路 选取中间数来算三次方 然后比较大小
'''

n = float(input())
def bsearch(l, r):
    # 浮点数二分法的循环条件是r-l<1e-8,其中8是因为题目中要保留6位小数. 退出条件接近于l==r， 所以退回l和r都可以
    while r - l > 1e-8: 
        mid = float((l + r) /2)
        # 同样的check条件中的“等于” 也无关紧要。
        if mid**3 >= n:
            r = mid
        else:
            l = mid
    return l

l = bsearch(-10000, 10000)
print("{:.6f}".format(l))

