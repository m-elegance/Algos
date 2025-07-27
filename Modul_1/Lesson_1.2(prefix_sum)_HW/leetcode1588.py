arr = [1,4,2,5,3]
n = len(arr)
prefix_sum = [0] * (n + 1)
prefix_sum[1] = arr[0]
for i in range(1, n):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]
print(prefix_sum)
sum = 0
for i in range(1, len(prefix_sum), 2):
    for j in range(len(prefix_sum)):
        if i + j < len(prefix_sum):
            sum += prefix_sum[i + j] - prefix_sum[j]
        else:
            break

print(sum)