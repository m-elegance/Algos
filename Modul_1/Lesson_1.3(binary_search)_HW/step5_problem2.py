# codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 5: B) таблица умножения
def ok(mid, k, n):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    return cnt < k

n, k = map(int, input().split())

l = 0
r = 10**10
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, k, n):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans + 1)













