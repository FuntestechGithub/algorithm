'''
leetcode 1071题 https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        ans must be prefex of the string or "" so we can use slice + multiply method
        '''
        for i in range(min(len(str1),len(str2)),0,-1): # because iterate from longest to shortest, so the first match must be the longest
            if str1[:i]*(len(str1)//i) == str1 and str1[:i]*(len(str2)//i) == str2:
                return str1[:i]
        return ""
    
import math
# optimized solution using 'greatest common divisor' concept
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        ans must be prefex of the string or "" so we can use slice + multiply method
        '''
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''