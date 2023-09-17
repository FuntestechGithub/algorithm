'''
leetcode 494: https://leetcode.com/problems/target-sum/description/
'''
# 递归解法
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        '''
        假设所有正数合为p
        数组里面所有数字合为s
        target 测试 p-(s-p) => 2p = s+t =? p = s+t>>1
        问题变为在数组中找到一些数字 而他们的合等于p
        '''
        n = len(nums)
        target += sum(nums)
        # 如果target是负数或者奇数， 因为奇数除以2不再是整数了。
        if target < 0  or (target & 1) or (target % 2):
            return 0
        target //= 2
        
        @cache
        def dfs(i, j):
            if i < 0:
                # 如果已经到了第一位了
                return 1 if j == 0 else 0
            #被压迫不选因为超过剩余J了
            if j < nums[i]:
                return dfs(i-1,j)
            #可以选的时候 加入可选可不选组合
            return dfs(i-1,j)+dfs(i-1, j-nums[i])

        return dfs(n-1, target)
    

# 二维动态解法
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        假设所有正数合为p
        数组里面所有数字合为s
        target 测试 p-(s-p) => 2p = s+t =? p = s+t>>1
        问题变为在数组中找到一些数字 而他们的合等于p
        '''
        n = len(nums)
        target += sum(nums)
        # 如果target是负数或者奇数， 因为奇数除以2不再是整数了。
        if target < 0  or (target & 1) or (target % 2):
            return 0
        
        target //= 2


        
        dp = [[0] * (target+1) for _ in range(n + 1)]
        # f[i][j] 前i个数总数等于j时候的种类
        dp[0][0] = 1

        for i in range(1,n+1):
            for j in range(target + 1):
                # can't pick
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:# not pick + pick
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
        return dp[n][target]


# 一维动态解法
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        假设所有正数合为p
        数组里面所有数字合为s
        target 测试 p-(s-p) => 2p = s+t =? p = s+t>>1
        问题变为在数组中找到一些数字 而他们的合等于p
        '''
        n = len(nums)
        target += sum(nums)
        # 如果target是负数或者奇数， 因为奇数除以2不再是整数了。
        if target < 0  or (target & 1) or (target % 2):
            return 0
        
        target //= 2

        dp = [0] * (target+1)
        dp[0] = 1

        # 二维转变过程
        '''
        简化式：
        f[i+1][j] = f[i][j] + f[i][j-nums[i]] => f[j] = f[j] + f[j-nums[i]]
        '''
        for i, v in enumerate(nums):
            # 因为从小到大会影响数组更新，所以从大到小来更新数组
            for j in range(target, v - 1, -1):
                dp[j] += dp[j-v]

        return dp[target]
