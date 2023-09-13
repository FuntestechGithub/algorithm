'''
二维前缀和中 s[i][j]的含义是：原数组中从(0,0)到(i,j)的所有元素的和。
当给与整数 x1,y1,x2,y2的时候, 我们所求的元素和就是： s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]


leetcode 304题
'''

def Prefix2dSum(x,y,nums):
    s = [[0] * (y+1) for _ in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            # 添加模式也是通过遍历过的元素合来计算。以下公式前提就是先横向遍历
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + nums[i-1][j-1]
    return s


# 预处理完S矩阵后
s = Prefix2dSum(3,3,[[1,2,3],[4,5,6],[7,8,9]])

# 计算(1,1)到(2,2)的区间和 (注意这里的坐标和之前S矩阵的坐标不一致 所以都得加上1)
x1,y1,x2,y2 = 1,1,2,2 # => 2,2,3,3

sumResult = s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]



# lettcode 304解题

class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix[0]), len(matrix)
        # created 1 level larger matrix for sum
        self.prefixSum = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + self.prefixSum[i][j-1] - self.prefixSum[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 + 1][col1] - self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]