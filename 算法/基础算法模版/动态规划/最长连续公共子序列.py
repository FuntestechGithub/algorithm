'''
最长连续公共子序列解题思路类似于最长公共子序列，只是在状态转移方程上需要在断连的时候归零处理。
'''

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m,n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    result = 0
    for i, v1 in enumerate(text1):
        for j, v2 in enumerate(text2):
            if v1 == v2:
                dp[i+1][j+1] = dp[i][j]+1
                result = max(result, dp[i+1][j+1])
            else:
                dp[i+1][j+1] = 0
    return result

# 一维解法
def longestComSubstr1D(str1: str, str2: str) -> int:
    longstr, shortstr = (str1, str2) if len(str1) > len(str2) else (str2, str1)
    m, n = len(longstr), len(shortstr)
    # initlize a 1D array for DP
    dp = [0] * (m + 1)

    for i in range(1, n+1):
        temp = [0] * (m + 1)
        for j in range(1,m+1):
            # if match, add 1 to the previous value
            if longstr[j-1] == shortstr[i-1]:
                temp[j] = dp[j-1] + 1
            else:
                temp[j] = 0
        dp = temp
    return dp[m]

# 显示最长连续公共子序列
def printLongestComSubstr1D(str1: str, str2: str) -> int:
    longstr, shortstr = (str1, str2) if len(str1) > len(str2) else (str2, str1)
    m, n = len(longstr), len(shortstr)
    # initlize a 1D array for DP
    dp = [0] * (m + 1)
    curMax = 0
    for i in range(1, n+1):
        temp = [0] * (m + 1)
        for j in range(1,m+1):
            # if match, add 1 to the previous value
            if longstr[j-1] == shortstr[i-1]:
                temp[j] = dp[j-1] + 1
                if temp[j] > curMax:
                    curMax = temp[j]
                    currIndex = j
            else:
                temp[j] = 0
        dp = temp
    return longstr[currIndex-curMax:currIndex]

# test case
str1 = "ABCABC"
str2 = "ABC"
print(printLongestComSubstr1D(str1, str2))
print(longestComSubstr1D(str1, str2))