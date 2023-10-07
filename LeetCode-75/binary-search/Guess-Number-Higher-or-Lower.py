'''
leetCode 374. https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75

key point: if either using left or right bound, we need to adjust the range to include the most extreme case on the edge.
'''



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == 6:
        return 0
# above is a fake guess function

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = l + r >> 1
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m
            else:
                l = m + 1

# or

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n+1

        while l < r:
            m = l + r >> 1
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m
            else:
                l = m + 1