'''
摩尔投票算法核心就是利用正负抵消，最后剩下的数就是大于一半的数。

当题目不再是大于一半而是大于n/几点时候， 也可以用这个方法，增加候选人数量，只不过最后要判断一下剩下的数是否真的大于n/几点。
'''


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, candidate = 0, None
        for num in nums:
            if candidate == num:
                count += 1
            elif count == 0:
                candidate = num
                count += 1
            else:
                count -= 1
            print(candidate, count)
        
        return candidate