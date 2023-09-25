'''
Leetcode 643 https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        '''
        sliding window practice
        '''
        sums = 0
        ans = float('-inf') 
        for i, v in enumerate(nums):
            sums += v
            if i >= k:
                sums -= nums[i-k]
            #只要大于k-1（sums包括k个字符）就更新ans一次
            if i >= k-1:
                ans = max(ans, sums)
        return ans / k
