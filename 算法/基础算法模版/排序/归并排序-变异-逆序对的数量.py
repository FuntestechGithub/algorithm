'''
题目地址： https://www.acwing.com/problem/content/description/788/

归并排序的同时 计算逆序数对。
'''
temp = [0] * 100010 # 临时数组, 长度为数组长度

def mergeSort(nums, start, end):
    if start >= end: return 0

    mid = start + end >> 1
    res = mergeSort(nums,start, mid) + mergeSort(nums, mid + 1, end)

    left, right, k = start, mid + 1, 0
    # 归并过程
    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            temp[k] = nums[left]
            k += 1
            left += 1
        else:
            # 如果在右边，就已经可以计算所有左边的逆对数了
            temp[k] = nums[right]
            k += 1
            right += 1
            # 在右边的单一位数（right位置） 要比所有左边单一位置（left位置）的数以及其右边所有数小（到mid位置）， 
            # 所以逆对数要加上左边剩余的数的个数（mid - left + 1）
            res += mid - left + 1
        
    # 扫尾
    while left <= mid:
        temp[k] = nums[left]
        k += 1
        left += 1
    while right <= end:
        temp[k] = nums[right]
        k += 1
        right += 1
        
    # 物归原主
    k, left = 0, start
    while left <= end:
        nums[left] = temp[k]
        left += 1
        k += 1
            
    return res


