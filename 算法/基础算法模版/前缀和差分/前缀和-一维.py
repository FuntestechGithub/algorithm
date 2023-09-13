'''
前缀和其实就是一个数组，这个数组的第i个元素就是原数组从下标0到下标i的所有元素的和。
这其实个公式：
sum[i] = sum[i-1] + nums[i]

前缀和应用
1. 求总和 （预处理）
S[i] = a[1] + a[2] + ... a[i] (前缀和都是从1开始)
2. 用l,r来求区间和
a[l] + ... + a[r] = S[r] - S[l - 1] (其中S[r]代表的是前r个元素和 减去 前l-1个元素和 就是区间和)

用这个统一模版就很容易解决很多问题了
'''

def prefixSum1(n, nums):
    s = [0] * (n+1)
    for i,x in enumerate(nums):
        s[i+1] = s[i] + x
    return s

def prefixSum2(nums):
    s = [0]
    for x in nums:
        s.append(s[-1] + x)
    return s

s = prefixSum1(5, [1,2,3,4,5])
# 计算2到4的区间和
l, r = 2, 4
print(s[r] - s[l-1])

