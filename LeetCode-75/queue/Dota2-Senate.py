'''
Leetcode 649 https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
'''

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, v in enumerate(senate):
            if v == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0]+n)
            else:
                dire.append(dire[0]+n)
            radiant.popleft()
            dire.popleft()        

        return "Radiant" if radiant else "Dire"