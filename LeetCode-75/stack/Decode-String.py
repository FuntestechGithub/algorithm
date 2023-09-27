'''
LeetCode 394 https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi = 0

        for c in s:
            if c == "]":
                temp = ""
                while stack and isinstance(stack[-1],str):
                    curr = stack.pop()
                    if curr != "[":
                        temp = curr + temp
                currMulti = stack.pop()
                temp = currMulti * temp
                stack.append(temp)
                
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
                
            else:
                if multi != 0:
                    stack.append(multi) 
                    multi = 0
                stack.append(c)
                
        return "".join(stack)