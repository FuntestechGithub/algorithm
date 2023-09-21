'''
LeetCode: 605 https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
'''
# 便利
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        '''
        finding the max space of the array
        '''
        count = 0
        flowerbed = [0] + flowerbed + [0] #拓宽左右边界进行遍历
        for i in range(1,len(flowerbed)-1): #从原数组的第一位到最后一位
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False