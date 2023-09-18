'''
leetcode 1306题： https://leetcode.com/problems/jump-game-iii/description/
'''

# 递归
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        '''
        给出start的位置

        index +/- arr[i]

        '''
        
        n = len(arr)
        deadend = set()
        def dfs(i):
            if i < 0 or i >= n:
                return False

            if arr[i] == 0:
                return True

            if i in deadend:
                return False
            
            # 任何访问过的数都不应该再被访问
            deadend.add(i)
            next1 = i + arr[i]
            next2 = i - arr[i]
            # 用or来检索True
            return dfs(next1) or dfs(next2)
        return dfs(start)

# DFS
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        '''
        给出start的位置

        index +/- arr[i]

        '''
        
        n = len(arr)
        tocheck = [start]

        while tocheck:
            node = tocheck.pop()
            if arr[node] == 0:
                return True
            # 检查过的arr元素不会给tocheck添加新的所以任何会引导至这个结果的元素都会hit deadend
            if arr[node] < 0:
                continue
            
            for i in [node - arr[node], node + arr[node]]:
                if 0 <= i < n:
                    tocheck.append(i)
            # 检查过的数字谁为负数 下次遇到会自动从tocheck里删除
            arr[node] = -arr[node]
        
        return False