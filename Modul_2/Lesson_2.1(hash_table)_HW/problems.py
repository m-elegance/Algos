# 205(инъекция с помощью хеш-таблицы)
# 217, 219, 242
# 2615 (расстояние между одинаковыми числами в массиве)
# 2799, 1577
# nums = [2, 3, 4, 5, 3]

# l = nums.index(nums[-2:-1])

# print(l)


from random import *

nums = [7, -3, 0, 7, 0, 0, 4, 7, -4, -7]
n = len(nums)
prefix_sum = [0] * (n + 1)

my_dict = {}

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]


ans = 0
for i in range(n + 1):
    if prefix_sum[i] in my_dict:
        ans += my_dict[prefix_sum[i]]

    if prefix_sum[i] in my_dict:
        my_dict[prefix_sum[i]] += 1
    else:
        my_dict[prefix_sum[i]] = 1

print(ans)



print(nums)

print(prefix_sum)
