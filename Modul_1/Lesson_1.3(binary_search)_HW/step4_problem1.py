#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 4: A) максимальный средний отрезок

def ok(mid, arr, d):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    prefix_sum[1] = arr[0] - mid
    for i in range(1, n):
        prefix_sum[i + 1] = prefix_sum[i] + (arr[i] - mid)

    prefix_min = [0] * (n + 1)
    pos_min = [0] * (n + 1)

    prefix_min[1] = prefix_sum[1]
    for i in range(1, n):
        if prefix_sum[i + 1] > prefix_min[i]:
            prefix_min[i + 1] = prefix_min[i]
            pos_min[i + 1] = pos_min[i]
        else:
            prefix_min[i + 1] = prefix_sum[i + 1]
            pos_min[i + 1] = i + 1  

    for r in range(d, n + 1):
        if prefix_sum[r] >= prefix_min[r - d]:
            return [pos_min[r - d], r]
    
    return [-1, 1]

    


n, d = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = sum(arr)
ans_l = ans_r = -1
for i in range(100):
    mid = (l + r) / 2
    pos = ok(mid, arr, d)
    if pos[0] != -1:
        l = mid
        ans_l = pos[0]
        ans_r = pos[1]
    else:
        r = mid

print(ans_l + 1, ans_r)







