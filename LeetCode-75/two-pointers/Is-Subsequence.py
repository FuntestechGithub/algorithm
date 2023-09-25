'''
leetcode: # 392 https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        p1 = p2 = 0

        while p2 < len(t):
            if p1 < len(s) and s[p1] == t[p2]:
                p1 += 1
            
            p2 += 1
        
        return True if p1 == len(s) else False
