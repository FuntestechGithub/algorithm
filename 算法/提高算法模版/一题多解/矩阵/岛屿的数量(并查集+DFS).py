'''
题目链接： https://leetcode.com/problems/number-of-islands/description/

类似于题目“被围绕的区域”

核心就是把需要搜索的格子都标记成为海洋
'''

# DFS
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i,j):
            grid[i][j] = "0"

            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+x, j+y
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    dfs(ni,nj)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        
        return ans

# 并查集
class UnionFind:
    def __init__(self,grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n) #记录父字节的数组
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                # 初始化所有岛屿格的父字节为自己, 并计算岛屿格数量
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        # 如果两格父字节不相同， 先检查rank永远将rank低的格子的父字节设为rank高的格子的父字节
        # NOTE 这样做能使公共格子（和很多岛屿格子相邻）有更高的rank。
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            # 如果rank相同，在合并完将该格子的rank提升1
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            # 合并完后减少count的数量
            self.count -= 1

    def getCount():
        return self.count


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n = len(grid), len(grid[0])
        f = UnionFind(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni, nj = i+x, j+y
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                            f.union(i*n+j, ni*n+nj)
        
        return f.count