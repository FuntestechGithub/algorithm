'''
题目链接： https://www.acwing.com/problem/content/description/791/

'''

def main():
    # 读入数据 （可忽略不属于模版一部分）
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))


    left, right = 0, len(nums) - 1
    # 寻找左边界
    while left < right:
        mid = left + right >> 1
        # 首先考虑的是我们要找到target的起始位(左边界) 所以我们把check的条件设置为nums[mid] >= q
        if nums[mid] >= q:
            # 因为条件限制了答案是在右边的区间，且mid是可能包括答案，所以right = mid
            right = mid
        else:
            left = mid + 1
    
    # 此时left和right的状态为left == right， 所以无论用left或者right哪个都可以
    if nums[left] != q:
       print(-1, -1)
    # 如果找到了左边界，那么我们就可以接右边界
    else:
        print(left, end=' ')
        left, right = 0, len(nums) - 1
        # 寻找右边界
        while left < right:
            mid = left + right + 1 >> 1
            if nums[mid] <= q:
                left = mid
            else:
                right = mid - 1
        print(left)

        