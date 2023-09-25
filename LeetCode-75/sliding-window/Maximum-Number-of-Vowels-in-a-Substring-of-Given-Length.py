'''
LeetCode 1456题 https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/ 
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''

        '''
        lookupDict = ['a','e','i','o','u']
        ans = 0
        curr = 0
        for i, v in enumerate(s):
            if v in lookupDict:
                curr += 1

            if i >= k:
                if s[i-k] in lookupDict:
                    curr -= 1

            # update the ans
            if i >= k - 1:
                ans = max(ans, curr)

        return ans
