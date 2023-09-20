'''
所有add数组里的数对x意思为：在位置x[0]上加上x[1]的值
所有query数组里的数对x意思为：查询区间[x[0], x[1]]的和

思路为： 离散化 + 前缀和
用离散化的目的在于：值域很大却利用非常少的情况下，离散化就有了优势。

在这道题目里， 我们把会用到的坐标(alls)去重后映射到从1开始的自然数数组
'''


def main():
    add = [(1,2),(3,6),(7,5)]
    query = [(1,3),(4,6),(7,8)]
    a = [0] * 100 # 临时数组
    alls = [1, 3, 7, 1, 3, 4, 6, 7, 8] # 所有的索引

    def find(x):
        """二分查找模板，从索引数组alls中找到大于等于x的最小的索引"""
        l = 0
        r = len(alls)-1
        while l<r:
            mid = l+r>>1
            if alls[mid]>=x: r = mid    # ！！！if条件忘记了=号
            else: l = mid+1
        return l+1    # 因为要计算前缀和，所以加1保证索引从1开始


    for addIndex, addValue in add:
        x = find(addIndex)
        a[x] += addValue

    for i in range(1,len(a)):
        a[i] += a[i-1]
    
    for queryL, queryR in query:
        l = find(queryL)
        r = find(queryR)
        print(a[r]-a[l-1])

main()

    
