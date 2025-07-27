#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: D) детский праздник
m, n = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]


def x_i(mid, arr):
    x = 0
    block = arr[1] * arr[0] + arr[2]
    cntBlock = mid // block
    x += cntBlock * arr[1]
    x += min(mid % block // arr[0], arr[1])

    return x


def ok(mid, arr, m):
    sum = 0
    for i in range(len(arr)):
        sum += x_i(mid, arr[i])
    
    return sum >= m


l = 0
r = 10**10
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, arr, m):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)
for i in range(len(arr)):
    cnt = x_i(ans, arr[i])
    print(min(cnt, m), end=' ')

    m -= cnt
    m = max(m, 0)














