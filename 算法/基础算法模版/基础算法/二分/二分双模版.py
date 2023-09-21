'''
单调性的题目一定能二分， 但是二分的条件不一定是单调性。
二分的本质是定义一个性质的边界，然后二分这个边界。

这套模版适合用整数二分。
'''


def check(x: int) -> bool:
    return

def bssearch_1(left: int, right: int) -> int:
    while left < right:
        mid = left + right // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

def bssearch_2(left: int, right: int) -> int:
    while left < right:
        mid = left + right + 1 // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left