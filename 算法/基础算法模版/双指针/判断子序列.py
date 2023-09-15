'''
题目链接： https://www.acwing.com/problem/content/2818/

解题思路：
arr1 = [1,3,5]
arr2 = [1,2,3,4,5]

同时向右移动p2(长数组)持续加1。当遇到相同数值时候， p1(短数组)向右移动用以检测下一个arr1里的数组。 

当遍历完成，检查arr1里所有数字都找到匹配。

'''

def subSequence():
    arr1 = [1,3,5]
    arr2 = [1,2,3,4,5]

    m,n = len(arr1), len(arr2)
    p1, p2 = 0, 0
    while p1 < m  and p2 < n:
        if arr1[p1] == arr2[p2]:
            p1 += 1
        p2 += 1
    if p1 == m: print("True")
    else: print("False")

subSequence()

    