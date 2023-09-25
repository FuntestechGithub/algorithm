'''
LeetCode 1004题 https://leetcode.com/problems/max-consecutive-ones-iii/
'''
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        cntZero, res = 0, 0 
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                cntZero += 1
            while cntZero > k:
                if nums[l] == 0:
                    cntZero -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
