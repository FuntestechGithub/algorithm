'''
Leetcode 1337: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/?envType=daily-question&envId=2023-09-18

题目需要用到其他算法， 我们则着重注释堆队列在题目中的作用。
'''
import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        '''
        weaker when:
        1. less 1
        2. same i but smaller index

        steps:
        get number of 1s from each row and convert array to 1d array (binary search find most left 0)
        find kth smallest number from the preprocessed array. using heapq
        '''

        def findOnes(arr: list[int]) -> int:
            l, r = 0, len(arr)
            while l < r:
                m = l + r >> 1
                if arr[m] == 0:
                    r = m
                else:
                    l = m + 1
            return l
        
        # generate 1d array with A info
        for i in range(len(mat)):
            ones = findOnes(mat[i])
            mat[i] = [ones, i]
        
        ans = []
        # heapify会将mat中的每个元素组都按照组内第一个元素进行排序
        heapq.heapify(mat)
        print(mat)
        for i in range(k):
            # heappop会将mat中的第一个元素弹出，即最小的元素. 例如 元素[2, 3]和[2, 0]，则[2, 0]会先被弹出
            x = heapq.heappop(mat)
            ans.append(x[1])


        return ans