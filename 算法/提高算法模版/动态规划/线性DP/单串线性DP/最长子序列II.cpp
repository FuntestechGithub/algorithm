/*
q[i] 表示在i长度的上升子序列中，最小的结尾数

核心思想：当i长度时候找到给长度的最小值， 如果找到了，那么长度+1接着找长度为i+1的最小值。做比较的时候就是利用q数组的单调性，二分查找。如果a[i]比q数组中的最大值还大，那么就直接加入到q数组中，否则替换掉q数组中的最后个数。

举例
3 1 2 1 8 5 6

逻辑
在 q[0] = -2e9的前提下， 先检测3 因为它比现有数组的最大值还要所以len变为1并且q[1] = 3
再检测1 因为它比现有数组的1号位的最大值小，但是比0号位的数值大。所以替换掉q[1] = 1 并且len不变
再检测2 因为它比现有数组的最大值还大，len变为2并且q[2] = 2
再检测1 因为它比现有数组的最大值还要小,比在0位置的最小的值大所以替换掉q[1] = 1 并且len不变
以此类推

*/

#include <iostream>
#include <algorithm>

using namespace std;
const int N = 100100;

int n;
int a[N], q[N];

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    int len = 0;
    q[0] = -2e9; // 保证小于某个数的最大值一定存在 我们把第一个值设为负无穷
    for (int i = 0; i < n; i++)
    {
        int l = 0, r = len;
        while (l < r)
        {
            // 求上中位数
            int mid = l + r + 1 >> 1;
            // 二分出来找小与a[i]的最大的数 然后替换掉那个数右边的数。
            if (q[mid] < a[i])
                l = mid;
            else
                r = mid - 1;

            // 所以return的是r
        }
        len = max(len, r + 1);
        // 在下一个长度中，最小的结尾数为a[i]
        q[r + 1] = a[i];
    }

    for (int i = 0; i < len; i++)
        printf("%d ", q[i]);
    printf("%d\n", len);
    return 0;
}