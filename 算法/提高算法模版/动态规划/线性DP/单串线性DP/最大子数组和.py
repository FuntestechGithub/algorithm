class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [ -inf for _ in range(n)]
        
        dp[0] = nums[0]
        
        for i in range(1,n):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)
                