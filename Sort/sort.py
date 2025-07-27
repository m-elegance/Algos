nums = [2, 3, 2, 5, 3, 7]
bord_right = max(nums)
bord_left = min(nums)

my_dict = {}
for i in range(len(nums)):
    if nums[i] in my_dict:
        my_dict[nums[i]] += 1
    else:
        my_dict[nums[i]] = 1

ans = []

for i in range(bord_left, bord_right + 1):
    while i in my_dict and my_dict[i] != 0:
        ans.append(i)
        my_dict[i] -= 1

print(nums)
print(ans)


# print(my_dict)
