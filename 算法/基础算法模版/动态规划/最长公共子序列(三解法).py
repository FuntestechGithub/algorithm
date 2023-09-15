'''
leetcode: https://leetcode.com/problems/longest-common-subsequence/description/

'''
# 解法一： 递归
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        @cache
        def backtracking(pm,pn):
            # 递归终止条件
            if pm < 0 or pn < 0: return 0
            # 从后往前递归， 当两个字符相等时候，返回1
            if text1[pm] == text2[pn]:
                return backtracking(pm-1,pn-1) + 1
            # 一次递归两个字符串 找到最大值
            return max(backtracking(pm-1,pn), backtracking(pm,pn-1))
        return backtracking(m-1,n-1)

# 解法二： 动态规划二维数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i, v1 in enumerate(text1):
            for j, v2 in enumerate(text2):
                if v1 == v2:
                    # dp[i][j]表示的是：到达前一个字符是最长的字符串数。 
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    # 如若不一致，更新原则为从 “上个数值已达到的公共子序列长度” 和 “正在运算的数值已达到的公共子序列长度” 选择大的那个数
                    # 这步的实际意义仅仅是确保下一行运算时能保持 “上个数值已达到的公共子序列长度”！
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        # 上述表达已经含括所有edge case, dp[i][j], dp[i][j+1],dp[i+1][j]的运用已经包含了所有情况
        return dp[m][n]

# 解法三： 动态规划一维数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longs, shorts = (text1, text2) if len(text1) > len(text2) else (text2, text1)
        m,n = len(longs), len(shorts)
        #必须要用长的字符串来初始化dp数组
        dp = [0] * (m+1)

        for i in range(1,m+1):
            # 用currArr来记录上一行的dp数组
            currArr = [0] * (m+1)
            for j in range(1,n+1):
                if longs[i-1] == shorts[j-1]:
                    currArr[j] = dp[j-1] + 1
                else:
                    currArr[j] = max(dp[j], currArr[j-1])
            dp = currArr
        return dp[n]



