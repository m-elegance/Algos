from random import *


def merge(nums1, nums2):
    ind1 = ind2 = 0
    res = []
    while ind1 < len(nums1) and ind2 < len(nums2):
        if nums1[ind1] < nums2[ind2]:
            res.append(nums1[ind1])
            ind1 += 1
        else:
            res.append(nums2[ind2])
            ind2 += 1

    if ind1 < len(nums1):
        res += nums1[ind1:]
    else:
        res += nums2[ind2:]

    return res


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    n = len(arr)
    middle_ind = n // 2

    left_arr = arr[:middle_ind]
    right_arr = arr[middle_ind:]

    return merge(mergeSort(left_arr), mergeSort(right_arr))


n = 10
arr = [randint(-10, 10) for i in range(n)]

print(mergeSort(arr))
