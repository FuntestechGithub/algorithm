'''
leetcode 1871题： https://leetcode.com/problems/jump-game-vii/description/
'''
import re
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        start at index 0
        have minJump and maxJump

        i + minJump <= j <= min(i + maxJump, s.length - 1)
        can't jump to whereever == 1

        '''
        n = len(s)

        def dfs(i):
            if i == n-1:
                return True
            
            if i + minJump > n-1 or s[i] == "1":
                return False
            
            for j in range(i + minJump, min(i + maxJump, n-1)+1):
                if dfs(j):
                    return True
            return False
        
        if s[-1] == '1':
            return False

        # 超时其实主要是因为存在连续长度大于最大跳跃距离的超长的case. 解决超时只要判断最长的0间距,如果超过max就return False。
        if len(max(re.split('0+',s),key=len)) >= maxJump:
            return False


        return dfs(0)


# DP
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # 数组初始化为0 = False 而dp[0] = 1因为其实位置可能可以到达
        # dp[i]代表就是在i位是否能够被到达
        n = len(s)
        dp = [1] + [0] * (n-1)


        for i in range(1,n):
            '''
            同时满足以下三个条件才能是视为此距离可以被到达
            1. 到i的距离已经达到minJump的要求
            2. s[i]为0
            3. 到i的距离没有超过maxJump， 或着i>maxJump同时 i-maxJump 到 i-minJump 直接任何一位可以到达（代表着当前i的位置可以被到达）
            
            dp[i-minJump]-dp[i-maxJump-1] >= 1
            因为是前缀和，所以dp[i-minJump]（代表的是i-minJump的位置是否可以被到达）-dp[i-maxJump-1]（代表的是i-maxJump-1的位置是否可以被到达）的区间合>=1
            就代表i-maxJump-1到i-minJump之间有可以被到达的位置。
            '''
            dpVal = s[i] == "0" and i >= minJump and (i<= maxJump or dp[i-minJump]-dp[i-maxJump-1] >= 1)
            # 前缀和的操作
            dp[i] = dp[i-1] + dpVal
        return dpVal



