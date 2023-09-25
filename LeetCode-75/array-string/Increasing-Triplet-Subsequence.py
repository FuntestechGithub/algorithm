'''
LeetCode: 334 https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        '''
        any three elements being incremental
        greedy
        '''
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
