'''
模版一： 并查代替搜索， 将关联的节点放入并查集中进行合并。最后返回数组的长度。 适用于矩阵
'''
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