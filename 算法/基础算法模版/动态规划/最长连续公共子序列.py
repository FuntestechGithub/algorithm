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


text1 = "abcde"
text2 = "1223abacde3123123"

print(longestCommonSubsequence(text1, text2))