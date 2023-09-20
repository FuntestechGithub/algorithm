'''
leetcode 2856题： https://leetcode.com/problems/minimum-array-length-after-pair-removals/submissions/

这道题如果用堆的特性来说可以做但会超时。 不过思路还是不错的。
'''


class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        '''
            所以我们找到出现次数最大的两个,将二者的次数都减去一,代表消去
            如果最后只剩下一个元素,则无法操作,否则一直操作
        '''
        from collections import Counter
        import heapq as hp
        # 按照重复数字多少进行排列并转化为map
        dict1 = Counter(nums)
        heap=[]
        for i,j in dict1.items():
            # 由于python中的heapq弹出的都是最小元素,而我们要的是最大元素,所以加负号
            hp.heappush(heap,-j)
            
        print(heap)
        while len(heap)>1:
            # 重复数字最大的两个数
            x = -hp.heappop(heap)
            y = -hp.heappop(heap)
            # 因为任何两个数字都能消除所以不用考虑pop出来的数字具体是什么。 如果数字还有多虑则放回heap中
            if x>1:
                hp.heappush(heap,-x+1)
            if y>1:
                hp.heappush(heap,-y+1)
            print(heap)
        
        if heap:
            return -heap.pop()
        else:
            return 0


'''
换个思路不再使用堆

如果只考虑数字出现最多的1个数字

假设出现最多的数字为x 出现次数为countx

如果countx大于长度的一半则无法消除, 那剩余必然是countx*2-n
如果countx小于长度的一半则可以消除, 那剩余得按照奇数偶数考虑，如果是偶数剩余为0，如果是奇数剩余为1
'''
from collections import Counter
class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        max_cnt = cnt.most_common(1)[0][1]
        # 判断奇数还是偶数 我们可以简单用 n%2
        return max(2*max_cnt-n, n%2)

'''
如果有数字超过一半以上的数字，那么这个数字必然是中位数 所以我们不需要遍历整个数组，只需要找到中位数即可
'''
from bisect import bisect_left, bisect_right   
class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        x = nums[n//2]
        max_cnt =  bisect_right(nums, x) - bisect_left(nums,x)
        return max(2*max_cnt -n, n%2)