'''
题目地址： https://www.acwing.com/problem/content/description/785/

快速排序是一种常用的排序算法，其时间复杂度为 O(nlogn)。
'''

def quickSort(nums, start, end):
    # 递归终止条件， 当start >= end时， 说明只有一个元素， 不需要排序
    if start >= end: return 

    # 定义左右指针, 边界条件为 start - 1, end + 1 所以开始排序时候首先都是要推进一个位置
    left, right = start - 1, end + 1
    # 定义基准值 pivot
    pivot = nums[(start + end) >> 1]

    # 开始排序
    while left < right:
        # 每次循环， 都要先推进一个位置，因为上次的节点已经比较过了
        left += 1
        while nums[left] < pivot:
            left += 1
        right -= 1
        while nums[right] > pivot:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    
    # 递归调用
    quickSort(nums, start, right)
    quickSort(nums, right + 1, end)

