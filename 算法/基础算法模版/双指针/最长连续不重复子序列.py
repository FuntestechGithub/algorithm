'''
双指针模版很简单 但是很多题目需要运用其他的方式辅助， 也可以被其他方式替代。例如 最长连续不重复子序列题目。
链接有：
https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solutions/
https://www.acwing.com/problem/content/801/


思路为： 通过hashmap记录每个字符出现的次数, 当出现重复字符时, 移动左指针到重复字符的右边一位然后更新最长的子序列长度
核心为： 控制hashmap里相同key的value不超过1

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        n = len(s)
        j = 0 
        res = 0
        for i in range(n):
            # 先初始化temp 使每个对应位置的数值变为1
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

            # 当相同数字出现，通过以上步骤将hashmap[s[i]的值加了1，一下while loop被启动
            while j <= i and hashmap[s[i]] > 1:
                # 我们将移动j到第一个重复数字的右边一位
                hashmap[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res