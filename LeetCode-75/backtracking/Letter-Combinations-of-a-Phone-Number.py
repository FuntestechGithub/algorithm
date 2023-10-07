'''
LeetCode 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=leetcode-75
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        # edge case
        if not digits:
            return res
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtracking(index, path):
            # when path has enough chars
            if len(path) == n:
                res.append("".join(path))
                return
            
            if index >= n:
                return
            

            possChars = letters[digits[index]]
            for char in possChars:
                path.append(char)
                backtracking(index+1, path)
                path.pop()
        
        backtracking(0,[])
        return res

