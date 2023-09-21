'''
leetcode 151题 https://leetcode.com/problems/reverse-words-in-a-string/description/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        go through the s from back.
        detect the last substring and put the string to ans when " " is encountered.
        edge case 1: hit " " when there is substring -> ignore
        edge case 2: need to put last detected substring to answer 
        '''
        ans = ""
        # as we need extra " " to put last piece back to ans, so we add one more " " in front of initial s     
        s = " " + s
        l = len(s)-1
        while l >= 0:
            curAns = ""
            while s[l] != " ":
                tmp = curAns
                curAns = s[l] + tmp
                l -= 1

            if s[l] == " " and curAns != "":
                if ans:
                    ans += " " + curAns
                else:
                    ans += curAns
            l -= 1

        return ans