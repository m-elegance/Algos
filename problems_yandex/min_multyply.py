nums = [-4, -6, -7, -2, -5]

n = len(nums)
min_1 = min(nums)
max_2 = max(nums)

min_2 = nums[0]
flag_min = False

max_1 = nums[0]
flag_max = False

for i in range(n):
    if nums[i] == min_1 and flag_min == True:
        min_2 = min_1
    else:
        if nums[i] > min_1:
            if nums[i] < min_2:
                min_2 = nums[i]

    if nums[i] == max_2 and flag_max == True:
        max_1 = max_2
    else:
        if nums[i] < max_2:
            if nums[i] > max_1:
                max_1 = nums[i]

    if min_1 == nums[i]:
        flag_min = True
    if max_2 == nums[i]:
        flag_max = True


print(min_1, min_2)
print(max_1, max_2)

if min_1 * max_2 <= 0:
    print(min_1 * max_2)
else:
    if min_1 < 0:
        print(max_1 * max_2)
    else:
        print(min_1 * min_2)
