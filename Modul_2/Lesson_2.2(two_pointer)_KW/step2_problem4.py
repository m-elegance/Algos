# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 2 » D) Число отрезков с большой суммой

n, s = map(int, input().split())
a = list(map(int, input().split()))

i = 0
sum = 0
cnt = 0
ans = 0
for j in range(n):
    sum += a[j]
    while i < n and sum >= s:
        cnt += 1
        sum -= a[i]
        i += 1
    ans += cnt


print(ans)


