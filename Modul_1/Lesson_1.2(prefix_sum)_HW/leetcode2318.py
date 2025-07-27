s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

n = len(s)
m = len(shifts)
alphavet = 'abcdefghijklmnopqrstuvwxyz'

prefix_sum = [0] * (n + 1)
temp_next = [0] * (n + 1)
temp_prev = [0] * (n + 1)
for i in range(m):
    if shifts[i][2] == 1:
        temp_next[shifts[i][0]] += 1
        temp_next[shifts[i][1] + 1] -= 1
    else:
        temp_next[shifts[i][0]] -= 1
        temp_next[shifts[i][1] + 1] += 1

prefix_sum[0] = temp_next[0]
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + temp_next[i]
ans = ''
for i in range(n):
    ans += chr((ord(s[i]) - ord('a') + prefix_sum[i]) % 26 + ord('a'))
