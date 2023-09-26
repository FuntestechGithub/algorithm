'''
LeetCode: 1732 https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gain = [0] + gain
        ans = int('-inf')
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            ans = max(ans, gain[i])
        return ans if ans >= 0 else 0