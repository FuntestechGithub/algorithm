'''
LeetCode 2215 https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # method 1: using set operation
        nums1 = set(nums1)
        nums2 = set(nums2)

        # method 2: iterating through the list
        inter = set(nums1) & set(nums2)
        ans1 = []
        for i in set(nums1):
            if i not in inter:
                ans1.append(i)

        ans2 = []
        for i in set(nums2):
            if i not in inter:
                ans2.append(i)


        return [list(nums1 - nums2),list(nums2 - nums1)]
