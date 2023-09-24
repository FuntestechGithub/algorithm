'''
leetcode # 283 https://leetcode.com/problems/move-zeroes/description/
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead. Two pointers

        fast搜索非0的数将它与慢指针指向的数字进行交换（慢指针在快指针指向数字不为零时候会随着移动
        """
        fast = slow = 0
        n = len(nums)
        while fast < n:
            # 维护状态是只有当fast不为0时进行位置交换 确保所有大于0的数都移动到slow左边
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1