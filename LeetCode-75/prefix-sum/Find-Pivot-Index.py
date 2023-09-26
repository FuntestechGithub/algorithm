'''
LeetCode 724 https://leetcode.com/problems/find-pivot-index/
'''
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumLeft, sumRight = 0, sum(nums)

        for i in range(len(nums)):
            sumRight -= nums[i]
            if sumLeft == sumRight:
                return i
            
            sumLeft += nums[i]
        return -1
