# codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 5: C) K-я сумма
def ok(x, k, a, b):
    n = len(a)
    j = 0
    cnt = 0
    for i in range(n):
        while j < n and a[i] + b[j] <= x:
            j += 1
        cnt += j

    return cnt < k


n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()

l = 0
r = 10**10

ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, k, a, b):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans + 1)
