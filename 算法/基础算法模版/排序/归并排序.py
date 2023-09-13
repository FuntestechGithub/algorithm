'''
题目地址： https://www.acwing.com/problem/content/description/787/

归并排序是一种稳定的排序算法，其时间复杂度为 O(nlogn)。
'''

temp = [0] * 100010 # 临时数组, 长度为数组长度

def mergeSort(nums, start, end):
    # 递归终止条件， 当start >= end时， 说明只有一个元素， 不需要排序
    if start >= end: return
    # 定义中间值
    mid = (start + end) >> 1
    # 递归调用, 推进到最深的情况
    mergeSort(nums, start, mid)
    mergeSort(nums, mid + 1, end)

    # 定义左右指针, 左边为start -> mid, 右边为 mid + 1 -> end
    left, right, k = start, mid + 1, 0
    # 合并数组， 因为有长短之分目前 先合并左右同一长度的部分
    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            temp[k] = nums[left]
            k += 1
            left += 1
        else:
            temp[k] = nums[right]
            k += 1
            right += 1
    
    # 加入剩余部分
    while left <= mid:
        temp[k] = nums[left]
        k += 1
        left += 1

    while right <= end:
        temp[k] = nums[right]
        k += 1
        right += 1

    # 重置k 和 left 的值 为下面的循环做准备
    k, left = 0, start
    # 将临时数组的值赋值给原数组
    while left <= end:
        nums[left] = temp[k]
        left += 1
        k += 1


    

