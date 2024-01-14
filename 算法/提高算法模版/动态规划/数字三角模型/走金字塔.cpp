#include <iostream>
#include <algorithm>

using namespace std;

const int N = 510;

int w[N][N], f[N][N];
int n;

// f(i,j) 存的是最大值  集合是从上往下走到(i,j)位置的所有方式
// 这道题目从下往上考虑不需要考虑边界问题。 除了最后一排，其他的都可以有两种走法

int main()
{
    scanf("%d", &n);
    // 从上往下 第一行最少每行逐次增加一个元素
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++)
            scanf("%d", &w[i][j]);

    // 初始化最后行
    for (int i = 1; i <= n; i++)
        f[n][i] = w[n][i];

    for (int i = n - 1; i; i--) // i>=0 简写成i
        for (int j = 1; j <= i; j++)
            f[i][j] += max(f[i + 1][j] + w[i][j], f[i + 1][j + 1] + w[i][j]);

    printf("%d\n", f[1][1]);
    return 0;
}
