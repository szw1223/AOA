# Coding: UTF-8
# Author: Zhewei Song
# Time: 2020/7/8
# Project: 

def selectSort(l):
    length = len(l)
    if length == 1 or length == 0:
        return l
    for i in range(length):
        huge = -1111
        for j in range(i, length):
            if l[j] > huge:
                huge = l[j]
                index = j
        l[i],l[index] = l[index],l[i]
    return l





def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid:]
    mer_l = merge_sort(left)
    mer_r = merge_sort(right)
    return merge(mer_l, mer_r)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
         try:
             if left[0] > right[0]:
                 result.append(right.pop(0))
             else:
                 result.append(left.pop(0))
         except:
             if type(left[0]) is not int:
                 result.append(left.pop(0))
             else:
                 result.append(right.pop(0))
    result += left
    result += right
    print(result)
    return result

l = [34, 99, 33, 69, 'k', 77, 88, 55, 11, 3, 36, 39, 66, 'c', 44, 22, 'a', 'b', 'd']
merge_sort(l)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def partition1(arr, low, high):
    i = low - 1    # left pointer
    j = high - 1   # right pointer
    pivot = arr[high]
    while j > i:   # this element is smaller than pivot, i++.
        if arr[i + 1] <= pivot:
            i += 1
        else:      # this element is bigger than pivot, replace elements from i to j, j -
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            j -= 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition1(arr, low, high)
        quickSort(arr, low, pi - 1 )
        quickSort(arr, pi + 1, high)

arr = [2, -1, 10, 7, 8, 9, 1, 5, 2, 123, 2, 123, 222, 23, 324, 45, 56676, 89, 9]
quickSort(arr, 0, len(arr) - 1)