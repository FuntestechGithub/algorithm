'''
给与一个 0,1矩阵 输出一个距离矩阵。

dist(A[i][j],A[k][l])=|i−k|+|j−l|

B[i][j]=min1≤x≤N,1≤y≤M,A[x][y]=1dist(A[i][j],A[x][y])

做法 分别以每个1为起点遍历一遍保存最小值即可。 逻辑基础是由图论中产生

'''


n, m = map(int, input().split())

mat = [list(map(int, input())) for _ in range(n)]

# 如果输入矩阵为0 那dis[i][j]为-1 不然就为0
# 这个矩阵是距离矩阵（答案）
dis = [[0 if i else -1 for i in row] for row in mat ]

# 将mat里面所有1的位置放入q队列中
q = [(i, j) for i, row in enumerate(mat) for j, v in enumerate(row) if v == 1]

while q:
    nq = []
    for x,y in q:
        # dx和dy 代表的是上下左右四个方向
        for dx, dy in zip((-1, 0, 1, 0), (0, -1, 0, 1)):
            nx, ny = x + dx, y + dy
            # 当nx，ny完全有效的时候。重点在于dis中没有被更新过。
            # Note 因为两段行以及单调性，后插入q的永远距离大过最前段的
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0 and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                nq.append((nx,ny))
    
    q = nq

[print(' '.join([str(i) for i in row])) for row in dis]