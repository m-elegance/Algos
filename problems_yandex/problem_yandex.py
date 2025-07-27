nums = [-5, -4, -1, 0, 3, 4, 7, 9]
n = len(nums)
j = n - 1

ans = []

for i in range(n):
    while j >= i and nums[i] * nums[i] < nums[j] * nums[j]:
        ans.append(nums[j] * nums[j])
        j -= 1
    if j >= i:
        ans.append(nums[i] * nums[i])

ans.reverse()

print(ans)

