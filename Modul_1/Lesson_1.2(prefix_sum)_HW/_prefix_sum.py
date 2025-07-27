# 1588, 2485, 2389, 1413, 2680, 1310, 2318(алфавит в аски), 1124
# || 1590(не сделана) ||
# || 826, 862 (не сделана) ||
# || 1126 (еще раз разобрать) ||
# || разобрать задачку ||


hours = [9, 9, 6, 0, 6, 6, 9, 9, 9, 1]
n = len(hours)
prefix_sum = 0
ans = 0
pos = {}
# r, l: prefix[r] - prefix[l - 1] > 0, r - l + 1 -> max
for i in range(n):
    if hours[i] > 8:
        prefix_sum += 1
    else:
        prefix_sum -= 1

    if prefix_sum > 0:
        ans = max(ans, i + 1)
    else:
        if not (prefix_sum in pos):
            pos[prefix_sum] = i
        if prefix_sum - 1 in pos:
            ans = max(ans, i - pos[prefix_sum - 1])
print(prefix_sum)
print(ans)
