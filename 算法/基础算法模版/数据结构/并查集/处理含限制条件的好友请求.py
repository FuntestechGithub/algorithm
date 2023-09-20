'''
Leetcode 2076题： https://leetcode.com/problems/process-restricted-friend-requests/description/

利用并查集， 将所有的人放入并查集中， 然后遍历所有的requests， 如果两个人的父字节不同则好友添加成功， 同时将两个人的父字节设为同一个。
'''


class UnionFind:
    def __init__(self,N):
        # 初始化
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        # 将Y的父字节设为X的父字节
        self.p[xr] = yr

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        '''
        restrictions array meaning xi and yi can't be friend

        requests array meaning xi and yi requests to be friend

        return based on requests array and showing if request is successful. 

        NOTE: in direct friend matters

        solve following problems:
        1. 如何发现 indirect friend （非常想飞机票的题目）
        2. 如何从 restrictions列表里发现限制

        用合并集来实现
        '''
        uf = UnionFind(n)
        ans = []

        for x, y in requests:
            # 查找并与restriction中的进行判断
            xP, yP = uf.find(x), uf.find(y)
            ifSuccess = True
            for a, b in restrictions:
                aP, bP = uf.find(a), uf.find(b)
                # 利用set来排序从而进行比较。 如果遇到direct或者indirect的restriction， 修改ifSuccess的数值
                if set([aP,bP]) == set([xP,yP]):
                    ifSuccess = False
                    break
            ans.append(ifSuccess)
            if ifSuccess: uf.union(x, y)
        return ans