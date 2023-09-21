'''
https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
'''

# O(n+(m-n)) = O(longestStr) solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sarray, larray = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        slen, llen = len(sarray), len(larray)
        res = []
        for i in range(slen):
            res.append(word1[i])
            res.append(word2[i])
        
        if slen < llen:
            for j in range(slen, llen):
                res.append(larray[j])

        return "".join(res)

# O(longestStr) solution   
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1),len(word2)
        llen = max(m,n)
        res = []
        for i in range(llen):
            if i < m:
                res += word1[i]
            if i < n:
                res += word2[i]
        return "".join(res)
    
# O(n+m) solution Two Pointer
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i,j = 0,0
        res = []

        while i < m or j < n:
            if i < m:
                res += word1[i]
                i += 1
            if j < n:
                res += word2[j]
                j += 1
        return "".join(res)
