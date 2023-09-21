'''
LeetCode: 345. https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        lookupDict = ["a","e","i","o","u","A","E","I","O","U"]
        s = list(s)
        
        l, r = -1, len(s)
        while l < r:
            l += 1
            r -= 1
            while l < len(s) -1 and s[l] not in lookupDict:
                l += 1
            while r > -1 and s[r] not in lookupDict:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
            else:
                break

            
        
        return "".join(s)
    
# same logic and one action at a time

class Solution:
    def reverseVowels(self, s: str) -> str:
        lookupDict = ["a","e","i","o","u"]
        s = list(s)
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l].lower() not in lookupDict:
                l += 1
            elif s[r].lower() not in lookupDict:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1            
 
        return "".join(s)