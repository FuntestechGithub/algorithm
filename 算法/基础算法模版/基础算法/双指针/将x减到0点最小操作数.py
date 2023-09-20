'''
leetcode 1658题 https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/?envType=daily-question&envId=2023-09-20
'''


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        '''
        remove leftmost or the rightmost, make target - popout value

        逆向思维， 把问题改变成为从数组中移除一个最长的子数组使得总和等于sum-total

        two pointer
        '''

        target = sum(nums) - x
        if target < 0: return -1  # 全部移除也无法满足要求
        
        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:
                s -= nums[left]
                left += 1
            
            if s == target:
                ans = max(ans, right - left + 1)
        
        # 当s始终没等于target的时候， ans是没有被更新过的
        return -1 if ans < 0 else len(nums) - ans