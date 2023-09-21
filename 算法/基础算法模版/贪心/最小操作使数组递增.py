'''
leetcode 1827. https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/submissions/
'''

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        '''
        贪心 假设
        nums[i+1]≥max{nums[i]+1,nums[i+1]}
        '''
        
        pre = nums[0] - 1
        ans = 0

        for num in nums:
            pre = max(pre+1, num)
            ans += pre - num
        return ans