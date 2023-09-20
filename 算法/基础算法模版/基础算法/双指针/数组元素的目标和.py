'''
双指针目的是优化暴力算法从而加快时间复杂度

双指针解法的切入点是考虑如何利用单调性. 在这道题目中(https://www.acwing.com/problem/content/802/), 单调性为p1数组单调递增, p2数组单调递减。

'''


def twoSum():
    arr1 = [1,2,4,7]
    arr2 = [3,4,6,8,9]
    target = 6


    p2 = len(arr1) - 1
    for p1 in range(len(arr1)):
        while p2 >= 0 and arr1[p1] + arr2[p2] > target:
            p2 -= 1
        if arr1[p1] + arr2[p2] == target:
            return [p1,p2]
        
a1, a2 = twoSum()
print(a1,a2)