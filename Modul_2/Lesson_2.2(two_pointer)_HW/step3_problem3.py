# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » C) город че
n, d = map(int, input().split())
arr = list(map(int,input().split()))

ans = 0
l = 0
for r in range(n):
    while l < n and arr[r] - arr[l] > d:
        l += 1
        if n - r - 1 > 0:
            ans += n - r
        else:
            ans += 1

print(ans)
