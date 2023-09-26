'''
LeetCode 1493 https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
'''
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        '''
        can remove 1 element 
        '''
        n = len(nums)
        res = 0
        left, right = 0, 0
        cnt_zeros = 0 

        while right < n:
            if nums[right] == 0:
                cnt_zeros += 1
            while cnt_zeros > 1:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            res = max(res, right - left)
            right += 1
        return res

