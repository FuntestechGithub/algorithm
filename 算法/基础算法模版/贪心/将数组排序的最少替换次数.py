'''
leetcode 2366题 https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
'''

class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        '''
        只要不是降序的数组就行
        提示： 从后面开始便利 因为如果从前开始便利那么后面的变化会直接影响前面变化过的数值。
        贪心： 设置拆分后的最小数值为m 如果 nums[i]>m 则我们需要对nums[i]进行拆分成x份.x=nums[i]//m 操作次数k=x-1
        '''
        
        ans, m = 0, nums[-1]
        for num in reversed(nums):
            k = (num-1) // m # 拆分出对个数必须为上取整， 公式为 ceil(nums[i]/m) =（num[i] + m - 1)/m = (nums[i]-1/m + 1)。因为k = x - 1所有这里最终公式为 (num-1) // m
            ans += k
            m = num // (k + 1) # x = k+1 
        return ans