'''
leetcode 2770题： https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/submissions/
'''

# 递归
class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        def dfs(i):
            if i == 0:
                return 0

            res = -inf
            for j in range(i):
                if abs(nums[j]-nums[i]) <= target:
                    res = max(res, dfs(j)+1)
            return res

        ans = dfs(n-1)
        return ans if ans >= 0 else -1

# 递归转数组
class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # dp[i] 表示到达i时，最大跳跃次数. 因为没有边界问题所以list的长度是n。
        dp = [-inf] * n
        dp[0] = 0 # 因为dfs中i==0时候返回0，所以这里也要设置为0

        # 因为是从第二位开始才能算nums[i]-nums[j]，所以从1开始
        for i in range(1,n):
            for j in range(i):
                if abs(nums[j]-nums[i]) <= target:
                    # 遍历所有i内的j，找到最大的dp[j]+1
                    dp[i] = max(dp[i], dp[j]+1)
        return -1 if dp[-1] < 0 else dp[-1]