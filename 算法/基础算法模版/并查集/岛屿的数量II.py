'''
leetcode 305题： https://leetcode.com/problems/number-of-islands-ii/
'''


class UnionFind:
    # O(m*n), O(m*n)
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [-1] * size
        self.cnt = 0
        self.size = size
    
    # O(1), O(1)
    # x = i * n + j
    def addLand(self, x):
        # 如果格子也有父节点 不予以改动
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.cnt += 1
    
    def isLand(self, x):
        if self.parent[x] >= 0:
            return True
        return False
    
    def getCount(self):
        return self.cnt
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                xroot, yroot = yroot, xroot
            self.parent[yroot] = self.find(xroot)
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
            self.cnt -= 1
    
 


class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        '''
        每次添加一个岛屿格子， 计算一次当前岛屿数量

        如果添加的岛屿周围没有岛屿格子 那肯定是+1

        如果添加的岛屿周围有岛屿格子则需要重新计算
        '''
        uf = UnionFind(m*n)
        ans = []
        for x, y in positions:
            land = x*n+y
            uf.addLand(land)

            for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+i, y+j
                nland = nx*n+ny
                if 0 <= nx < m and 0 <= ny < n and uf.isLand(nland):
                    uf.union(land,nland)
            ans.append(uf.getCount())
        return ans
