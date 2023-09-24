'''
leetcode 443题 https://leetcode.com/problems/string-compression/description/

要求返回压缩后的数组长度并且还要修改原数组

'''

class Solution:
    def compress(self, chars: list[str]) -> int:
        '''
        三指针解法
        i 为主指针引导
        j 为快指针定义同一字符的长度
        write 为修改坐标位置
        '''
        n = len(chars)
        i = 0
        write = 0
        while i < n:
            j = i
            # 将j移动到同一字符的最后一位 + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            if j - i > 1:
                # 将距离j-i 转换为string然后把不同的位置分别写成不同下坐标里
                for c in str(j-i):
                    chars[write] = c
                    write += 1
            i = j
        return write