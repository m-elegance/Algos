nums1 = [1, 2, 3, 7, 8]
nums2 = [2, 3, 4]
nums3 = [1, 2, 3]
nums4 = [1, 2, 3]
num = [nums1, nums2, nums3, nums4]



def merge(nums1, nums2):
    nums = []
    n1 = len(nums1)
    n2 = len(nums2)
    ind_1 = 0
    ind_2 = 0
    while ind_1 < n1 or ind_2 < n2:
        if ind_1 == n1:
            nums.append(nums2[ind_2])
            ind_2 += 1
        elif ind_2 == n2:
            nums.append(nums1[ind_1])
            ind_1 += 1
        else:
            if nums1[ind_1] < nums2[ind_2]:
                nums.append(nums1[ind_1])
                ind_1 += 1
            else:
                nums.append(nums2[ind_2])
                ind_2 += 1
    return nums


ans = num[0]
for i in range(1, len(num)):
    ans = merge(ans, num[i])
print(ans)
