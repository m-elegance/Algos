#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: C) Очень легкая задача
n, x, y = map(int, input().split())


def ok(mid, x, y, n):
    return (mid // x) + (mid // y) >= n - 1

l = 0
r = 10**10
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, x, y, n):
        # l = mid + 1
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
        #r = mid - 1


if n == 1:
    print(min(x, y))
else:
    print(ans + min(x, y))









