'''
差分二维处理方式与前缀和方式类似,只是在计算时需要考虑x2,y2到矩阵最右角到子矩阵,对其进行更新

S[x1][y1] += c, S[x2 + 1][y1] -= c, S[x1][y2 + 1] -= c, S[x2 + 1][y2 + 1] += c

LeetCode 2536题 https://leetcode.com/problems/increment-submatrices-by-one/description/
'''
n = 10 # 矩阵大小
finiteDiffMtx = [[0] * n for _ in range(n)]

def insert(x1,y1,x2,y2,value):
    finiteDiffMtx[x1][y1] += value
    finiteDiffMtx[x2+1][y1] -= value
    finiteDiffMtx[x1][y2+1] -= value
    finiteDiffMtx[x2+1][y2+1] += value

# LeetCode 2536题 解题
class Solution:
    def rangeAddQueries(self, n: int, queries: list) -> list:
        # 因为差分和恢复前缀和都需要阔一层边界 所以初始化边界为n+2
        finiteDiffMtx = [[0]*(n+2) for _ in range(n+2)]

        def insert(x1,y1,x2,y2,value):
            finiteDiffMtx[x1+1][y1+1] += value
            finiteDiffMtx[x2+2][y1+1] -= value
            finiteDiffMtx[x1+1][y2+2] -= value
            finiteDiffMtx[x2+2][y2+2] += value
        
        m = len(queries)

        while m:
            x1,y1,x2,y2 = queries[m-1]
            insert(x1,y1,x2,y2,1)
            m -= 1

        # 恢复前缀和
        for i in range(1,n+1):
            for j in range(1,n+1):
                finiteDiffMtx[i][j] += finiteDiffMtx[i-1][j] + finiteDiffMtx[i][j-1] - finiteDiffMtx[i-1][j-1]

        # 把size还原成n。 步骤先缩减行 再缩减列
        finiteDiffMtx = finiteDiffMtx[1:-1]
        for i, row in enumerate(finiteDiffMtx):
            finiteDiffMtx[i] = row[1:-1]
        
        return finiteDiffMtx








