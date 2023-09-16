'''
题目链接： https://leetcode.com/problems/house-robber/

若将抢劫房屋问题视为0,1背包问题， 将会直接有以下三种解法

'''

# 1. 递归解法
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
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


# 2. 二维动态解法