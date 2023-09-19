'''
leetcode 2812题： https://leetcode.com/problems/find-the-safest-path-in-a-grid/
求最高系数的路径 

两个cell的绝对距离 |x1-x2| + |y1 + y2|

需要首先知道小偷位置， 其次需要寻找曼哈顿距离最短的路径
也需要知道是否能走得通


二分答案

最大化离1的最近距离
1. 标记不能的格子（也就是1格周围到二分答案的值范围内所有格子都是不能走的）
2. 如何判断能走到右下角

接近O(n^2)
把距离1的格子按距离表上数值
'''


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # 多源bfs:

        # 标有距离的矩阵
        dis = [[-1] * n for _ in range(n)]
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0

        # 利用滚动数组去做多源bfs
        groups = [q]
        while q:
            temp = q
            q = []
            for x, y in temp:
                for dx,dy in zip([-1,0,1,0], [0,-1,0,1]):
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and dis[nx][ny] == -1:
                        dis[nx][ny] = dis[x][y] + 1
                        q.append((nx,ny))
            # 这里会将每次计算出的新坐标加入group中。
            groups.append(q)

        # 并查集模板
        fa = list(range(n * n))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        # 因为最后一个group是空的所以从倒数第二个开始，如果在d的距离能走到右下角就返回d。
        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    # 除了判断边界， 还得确保能走的格子是大于等于自己的 dis[x][y] >= dis[i][j]
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        fa[find(x * n + y)] = find(i * n + j) # merge的操作
            if find(0) == find(n * n - 1):  # 写这里判断更快些
                return d
        return 0