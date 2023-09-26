'''
LeetCode 2352 https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
'''
# method 1: O(n^2) creates a new matrix with col as row and row as col
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        g = [list(col) for col in zip(*grid)]
        return sum(row == col for row in grid for col in g)

import collections
# method 2: similar to method 1, but referrencing to a dictionary
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        n = len(grid)

        row_counter = collections.Counter(tuple(row) for row in grid)
        print(row_counter)

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]
        return count
    
