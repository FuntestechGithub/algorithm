'''
LeetCode 933 https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

using list and binery search

from bisect import bisect_left, bisect_right
class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        ranMin, ranMax = t-3000, t
        return bisect_right(self.requests, ranMax) - bisect_left(self.requests, ranMin) 



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''
from collections import deque

# using deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t-3000:
            self.requests.popleft()
        
        return len(self.requests)