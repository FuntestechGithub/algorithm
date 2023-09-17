'''
模版适用于任何二维矩阵查找的问题

力扣第 240 题 https://leetcode.com/problems/search-a-2d-matrix-ii/
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # binary search

        def bs(arr:list):
            l, r = 0, len(arr)-1
            while l < r:
                m = l + r >> 1
                if arr[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l
        
        # 可以进行优化减少运算时间，但是此算法最快也只能达到O(mlogn)
        m = len(matrix)
        for i in range(m):
            leftbound = bs(matrix[i])
            if matrix[i][leftbound] == target:
                return True
        return False