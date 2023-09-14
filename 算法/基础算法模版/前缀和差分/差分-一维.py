'''
差分(Finite difference)是前缀和的逆运算。

在一维中，构造很简单。 例如差分数列称为b, 那么：
b1 = a1, b2 = a2 - a1, b3 = a3 - a2, ..., bn = an - an-1

换一种思路 当拥有前缀和为a的数组,那原数组B(前缀合a构成的基础)就是a的差分数组。NOTE:类似积分微分的关系

O(n)时间内 从b数组得到a数组 
如果要求是在[l,r]区间上加上c, 那通过差分数组b, 只需要b[l] += c, b[r+1] -= c即可 从而在O(1)时间内完成

举例：
前缀和数组a为: 1,3,6,10,15
差分数组b为: 1,2,3,4,5
l, r = 2, 4
c = 10

当差分数组 b[2] 加上c后 所有再2以后的a数组数值都会自动加上c。 然后再对b[r+1] -= c (打补丁), 就可以保证只有在[l,r]区间上加上了c


应用：
给定a数组 a[1],a[2],...,a[n] 构造差分数组b[N] 满足a[i] = b[1] + b[2] + ... + b[i]
NOTE: 优化在于从包里O(mn)时间复杂度到了O(m+n)时间复杂度

题目链接： https://www.acwing.com/problem/content/description/799/
'''




def insert(left ,right, value):
    finiteDiffArr[left] += value
    finiteDiffArr[right+1] -= value


if __name__ == "__main__":
    nums = [1,2,2,1,2,1]
    n = len(nums)
    m = 1
    # 初始化差分数组为0
    finiteDiffArr = [0] * (n+2)
    
    # 假设a,b数组初始化为0的前提下， 差分数组可以被视为每个位置[i,i]加了a[i]数值.
    # 构建差分数组
    for i in range(n):
        insert(i + 1,i + 1,nums[i])

    # 读取m次操作， 修改的数值使用
    while m:
        l,r,c = map(int,input().split())
        insert(l,r,c)
        m -= 1

    # 将差分数组还原为原数组
    for i in range(1,n+1):
        finiteDiffArr[i] += finiteDiffArr[i-1]

    print(finiteDiffArr[1:-1])


