'''
leetcode 799题 https://leetcode.com/problems/champagne-tower/description/

思路模拟香槟塔的流动过程

'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        第i层时候j香槟到数量
        '''
        f = [[0] * 101 for _ in range(101)]
        f[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if f[i][j] > 1:
                    half = (f[i][j] - 1) / 2
                    f[i][j] = 1
                    f[i + 1][j] += half
                    f[i + 1][j + 1] += half
        return f[query_row][query_glass]
        
# 一维数组
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        f = [poured]
        for i in range(1,query_row + 1):
            temp = [0] * (i+1)
            for j, v in enumerate(f):
                if v > 1:
                    half = (v - 1) / 2
                    temp[j] += half
                    temp[j + 1] += half
            f = temp
        return min(1,f[query_glass])
        
