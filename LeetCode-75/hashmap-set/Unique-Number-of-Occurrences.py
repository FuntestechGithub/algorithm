'''
LeetCode: 1207 https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
'''

# Method 1: count the duplicates, then compare duplicates value
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashmap = Counter()
        for i in arr:
            hashmap[i] += 1
        
        return len(set(hashmap.values())) == len(hashmap)

# Method 2: same concept, but using one line
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return len(Counter(arr).values()) == len(set(Counter(arr).values()))