'''
题目链接： https://leetcode.com/problems/surrounded-regions/

思路都是从边角的O开始把相邻的格子都标记为不能走。最后将没有被标记的O都变成X。
'''

# DFS
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        if up down left right is x, it is surrounded
        """
        
        m, n = len(board), len(board[0])
        # dfs to turn all boarder O and its connections to B
        def dfs(i,j):
            board[i][j] = "B"
            for x, y in zip([1,0,-1,0],[0,1,0,-1]):
                ni, nj = i+x, j+y
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O":
                    dfs(ni,nj)

        # first and last col
        for i in range(m):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][n-1]=="O":
                dfs(i,n-1)

        # first and last row
        for j in range(n):
            if board[0][j]=="O":
                dfs(0,j)
            if board[m-1][j]=="O":
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"


#  并查集
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        if up down left right is x, it is surrounded
        """
        
        f = {}
        def find(x):
            # 初始化父字节都是自己, 这也是为了在KEY不存在的时候添加KEY和VALUE
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        # 把x的父字节设为y的父字节
        def merge(x,y):
            f[find(y)] = find(x)

        m, n = len(board), len(board[0])
        # dummy是用来存放子字节的
        dummy = m * n
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    # O在边缘时候, 将board[i][j]设为dummy设为父字节
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        # 这么做的好处就是所有边缘O的父节点都会最后指向最后一个边缘O
                        merge(i * n + j, dummy)
                        print(f)
                    else:
                        # O不在边缘的时候， 我们把board[i][j]设为她周围O格子的父节点
                        for x,y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                merge(i * n + j, (i + x) * n + (j + y))


        for i in range(m):
            for j in range(n):
                # 边缘O的父字节是自己而dummy
                if find(dummy) == find(i * n + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"