# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » B) общая длина
n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
sum = 0
ans = 0

for r in range(n):
    sum += a[r]
    while l < n and sum > s:
        sum -= a[l]
        l += 1
    len_otr = r - l + 1
    ans += (len_otr * (len_otr + 1)) // 2

print(ans)
