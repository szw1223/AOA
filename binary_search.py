# Coding: UTF-8
# Author: Zhewei Song
# Time: 2020/6/26
# Project:  AOA
import numpy as np

def binSear(l, a):
    left = 0
    right = len(l) - 1
    while right >= left:
        mid = left + (right - left)//2
        if l[mid] == a:
            return mid
        elif l[mid] > a:
            right = mid - 1
        else:
            left = mid + 1
    return -1
l = [1,3,5,6,7,8,9,13,14,15,17,19]


def binSearInMatrix(l, a):
    left = 0
    right = len(l[0]) * len(l) - 1
    while right >= left:
        mid = left + (right - left)//2
        r = mid // len(l)
        c = mid % len(l)
        if l[r, c] == a:
            return [mid//len(l), mid%len(l)]
        elif l[r, c] > a:
            right = mid - 1
        else:
            left = mid + 1
    return -1
l2 = np.array([[1,2,3,4],[5,7,8,9],[12,13,14,16]])


def findClosest(l, a):
    left = 0
    right = len(l) - 1
    if len(l) == 1:
        return l[0]
    elif len(l) == 0:
        return print('none')
    else:
        while left < right - 1:
            mid = left + (right - left) // 2
            if l[mid] == a:
                return [mid]
            elif l[mid] > a:
                right = mid
            else:
                left = mid
        return [left, right]

def find(l, a):
    li = findClosest(l, a)
    if len(li) == 1:
        return li[0]
    return li[0] if abs(li[0] - a) < abs(li[1] - a) else li[1]

def findK(l, a, k):
    n = find(l, a)
    left = n - 1
    right = n + 1
    for i in range(k):
        if abs(l[left] - a) > abs(l[right] - a):
            right += 1
        else:
            left -= 1
    return l[left: right + 1]

print(l)
print(find(l, 6))
print(findK(l, 7, 4))


def leftTarget(l, a):
    left = 0
    right = len(l) - 1
    while right - 1 > left:
        mid = left + (right - left) // 2
        if l[mid] >= a:
            right = mid
        else:
            left = mid
    if l[left] == a:
        return left
    elif l[right] == a:
        return right
    else:
        return -1
