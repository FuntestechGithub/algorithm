'''
LeetCode 2390 https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i, v in enumerate(s):
            if v == "*" and ans:
                ans.pop()
            else:
                ans.append(v)
        return "".join(ans)