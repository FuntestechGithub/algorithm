'''
题目链接: https://www.acwing.com/problem/content/2/

vol = [1, 2, 3, 4, 5] # 物品体积
val = [2, 3, 4, 5, 6] # 物品价值
当背包体积为 target 时，最大价值是多少？

二维时候，状态转移思路：
f[i][j] 表示前i个物品，总体积是j的情况下，总价值最大是多少
result = max(f[n][0~target])

不选第i个物品： f[i][j] = f[i-1][j] 就等于前一个物品数量的最大价值
选第i个物品： f[i][j] = f[i-1][j-vol[i]] + val[i] 就等于前一个物品数量的最大价值加上当前物品的价值

f[i][j] = max(f[i-1][j], f[i-1][j-vol[i]] + val[i])
f[0][0] = 0
'''


# 二维动态解法
def main():
    vol = [1, 2, 3, 4]
    val = [2, 4, 4, 5]
    target = 5

    n = len(vol)
    f = [[0]*(target + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(target+1):
            #不选
            f[i][j] = f[i-1][j]
            #选， 需要控制条件是背包总额大于当前物品体积。因为如果小于，就不能选。
            if(j >= vol[i-1]):
                f[i][j] = max(f[i-1][j], f[i-1][j-vol[i-1]]+val[i-1])

    print(f[n][target])

main()