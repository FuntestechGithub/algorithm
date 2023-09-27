'''
Leetcode 735 https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        '''
        positive and negative collisions
        # watch out when 0
        '''
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] == 0:
                continue

            if not stack:
                stack.append(asteroids[i])
                continue
            
            while stack and stack[-1] * asteroids[i] < 0 and asteroids[i] < 0:
                prev = stack.pop()
                if abs(prev) > abs(asteroids[i]):
                    asteroids[i] = prev
                elif abs(prev) < abs(asteroids[i]):
                    asteroids[i] = asteroids[i]
                else: 
                    asteroids[i] = 0
            if asteroids[i] != 0:
                stack.append(asteroids[i])
        
        return stack