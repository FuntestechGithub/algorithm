'''
来自张丁的模版：

将所有的数值放入一个set中去重，然后排序。
映射，使用二分查找，找到数值在数组中的位置，这个位置就是数值的离散化后的值。

a = sorted(set(arr))
ans = []
for x in arr:
    ans.append(bisect_left(a, x))
return ans 

如果不用bisect_left，可以自己写。
a = sorted(set(arr))
ans = []

def find(x):
    l, r = 0, len(a) - 1
    while l < r:
        mid = l + r >> 1
        if a[mid] >= x:
            r = mid
        else:
            l = mid + 1
    ans.append(l)

leetcode 1311题: https://leetcode.com/problems/rank-transform-of-an-array/description/  
'''

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        a = sorted(set(arr))
        ans = []
        for x in arr:
            ans.append(bisect_left(a, x) + 1)
        return ans

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # 将所有的数值放入一个set中去重
        a = sorted(set(arr))
        ref = []

        for x in a:
            l, r = 0, len(a) - 1
            while l < r:
                m = l + r >> 1
                if a[m] >= x:
                    r = m
                else:
                    l = m + 1
            ref.append(l+1)

        return ref

