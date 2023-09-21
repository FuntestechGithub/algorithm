'''
LeetCode: 238. Product of Array Except Self
'''

# O(n) time O(1) space
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prod = [1]*n
        # prod[i] presents product of all elements before  i - 1, so there will be last element missing from prod list
        for i in range(1,n):
            prod[i] = prod[i-1]*nums[i-1]
        
        # core purpose of prod list is keeping product before i - 1, so next loop we will need to * totall product i + 1 to end, 
        right = nums[-1]
        for i in range(n-2, -1, -1):
            prod[i] *= right
            right *= nums[i]
        
        return prod
    