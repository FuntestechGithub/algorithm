'''
leetCode 2300 https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # reduce the cacluation
        potions.sort()
        n = len(potions)
        
        def cal(i):
            l,r = 0,n
            while l < r:
                m = l + r >> 1
                if potions[m] * spells[i] >= success:
                    r = m
                else:
                    l = m + 1
            
            return n - l
        

        for i in range(len(spells)):
            spells[i] = cal(i)

        return spells     