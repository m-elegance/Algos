nums = [[1, 8], [2, 6], [8, 10], [15, 18]]
min_val = nums[0][0]
max_val = nums[0][0]

for i in nums:
    min_val = min(min_val, i[0])
    min_val = min(min_val, i[1])

    max_val = max(max_val, i[0])
    max_val = max(max_val, i[1])

print(max_val)
print(min_val)

helper = [0] * (max_val + 2)
print(helper)
for i in nums:
    helper[i[0]] = 1
    helper[i[1] + 1] = -1
prefix_sum = [0] * len(helper)
prefix_sum[0] = helper[0]
for i in range(1, len(helper)):
    prefix_sum[i] = prefix_sum[i - 1] + helper[i]

ans = []


flag = False
for i in range(len(prefix_sum)):
    if prefix_sum[i] != 0:
        if flag == False:
            start = i
        flag = True
    else:
        if flag:
            end = i - 1
            flag = False
            ans.append([start, end])

print(ans)
