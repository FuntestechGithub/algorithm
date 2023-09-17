'''
题目链接： https://leetcode.com/problems/house-robber/

若将抢劫房屋问题视为0,1背包问题， 将会直接有以下三种解法

'''

# 1. 递归解法
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        # @cache
        # 从后开始抢
        def dfs(x):
            if x < 0:
                return 0

            # not pick
            res = dfs(x-1)

            # pick
            res = max(res, dfs(x-2)+nums[x])
            return res


        return dfs(n-1)


# 2. 一维动态解法 （因为只需要前一个状态， 所以可以用一维数组）
'''
f[i] 表示抢劫前i个房屋获得最大收益是多少。

不选第i个房屋： f[i+1] 
选第i个房屋： f[i+2]+nums[i]
f[i] = max(f[i+1], f[i+2][j]+nums[i])
'''
class Solution2:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # 因为加2， 所以需要初始化f[n+2]
        f = [0]*(n+2)
        for i, v in enumerate(nums):
            f[i+2] = max(f[i+1], f[i]+nums[i])
        return f[n+1]
