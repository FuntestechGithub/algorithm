'''
题目地址： https://www.acwing.com/problem/content/description/787/

变异的快速排序， 需要找到第k个最小的数。 可以使用快速排然后找到第K个数的值。 模版为了实现在排序中直接找到K个数的值。
'''

def quickSort(nums, start, end, k):
    # 递归终止条件， 当start >= end时， 说明只有一个元素， 而这个数就是K的值
    if start == end: return nums[start]

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
        
    # 判断第K个数在左边还是右边, 如果在左边， 则递归左边， 否则递归右边. sl为左右分界点       
    sl = right - start + 1
    if sl >= k:
        return quickSort(nums, start, right, k)
    return quickSort(nums, right + 1, end, k - sl)