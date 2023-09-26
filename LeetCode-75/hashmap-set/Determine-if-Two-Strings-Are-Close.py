'''
LeetCode: 1657 https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
'''

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        op 1: meaning if charaters are the same
        op 2: cnt of duplicate is the same
        '''
        return Counter(word1).keys() == Counter(word2).keys() and sorted(Counter(word1).values()) == sorted(Counter(word2).values())