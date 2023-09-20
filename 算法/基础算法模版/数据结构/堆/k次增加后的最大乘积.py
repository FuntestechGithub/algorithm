'''
leetcode 2233题 https://leetcode.com/problems/maximum-product-after-k-increments/description/
'''
import heapq

class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        '''
        全正数数组和k

        从数组中选取任意元素加一 返回k次操作后最大的和
        x为大 y为小
        对于较大的元素加一的乘积为(x+1)y = xy+y
        而对较小的元素加一的乘积为(y+1)x = xy+x
        因此对较小的元素加1是我们的目标
        '''

        mod = 10 ** 9 + 7
        heapq.heapify(nums)   # 建立最小堆
        while k:
            k -= 1
            # 每次操作：弹出最小值，增加 1 并重新添加
            num = heapq.heappop(nums)
            heapq.heappush(nums, num + 1)
        res = 1
        for num in nums:
            res *= num
            res %= mod
        return res