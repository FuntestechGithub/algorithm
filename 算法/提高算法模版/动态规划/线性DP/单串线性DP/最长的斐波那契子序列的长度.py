class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''
        定义状态  dp[i][j] 表示为：以 arr[i]、 arr[j] 为结尾的斐波那契式子序列的最大长度。 
        arr[i] + arr[j] = arr[k]
        状态转移方式 dp[j][k] = max(arr[i]+arr[j]=arr[k], i<j<k)
        '''
        size = len(arr)
        
        dp = [[0]*size for _ in range(size)]
        ans = 0
        
        for i in range(size):
            for j in range(i+1, size):
                dp[i][j] = 2
        
        idx_map = {}
        # 将 value : idx 映射为哈希表，这样可以快速通过 value 获取到 idx
        for idx, value in enumerate(arr):
            idx_map[value] = idx
        
        for i in range(size):
            for j in range(i+1,size):
                if arr[i] + arr[j] in idx_map:
                    # 获取 arr[i] + arr[j] 的 idx，即斐波那契式子序列下一项元素
                    k = idx_map[arr[i]+arr[j]]
                                        
                    dp[j][k] = max(dp[j][k],dp[i][j]+1)
                    ans = max(ans, dp[j][k])
        
        if ans >= 3:
            return ans
        return 0