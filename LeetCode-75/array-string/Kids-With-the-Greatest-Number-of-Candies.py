'''
leetcode 1431题 https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
'''
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        '''
        finding if candies[i] + extraCandies >= max
        '''
        maxNum = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxNum:
                candies[i] = True
            else:
                candies[i] = False
        return candies