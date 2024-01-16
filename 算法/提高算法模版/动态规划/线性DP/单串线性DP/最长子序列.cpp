/*
f[i] 表示以第i个数结尾的最长上升子序列的长度

转移方程：
f[i] = max(f[i], f[j]+1)  1<=j<i && w[j] < w[i]
*/

#include <iostream>
#include <algorithm>

using namespace std;
const int N = 1010;

int n;
int w[N], f[N];

int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &w[i]);
        f[i] = 1;
    }

    for (int i = 1; i <= n; i++)
        for (int j = 1; j < i; j++)
            if (w[j] < w[i])
                f[i] = max(f[i], f[j] + 1);

    int res = 0;
    for (int i = 1; i <= n; i++)
        res = max(res, f[i]);

    cout << res;
    return 0;
}