# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » H) A-B рюкзак
n, m, s, A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)


W = 0
ans = 0
sum = 0
for i in range(m):
    W += B
    sum += b[i]
    if W <= s:
        ans += b[i]


j = m - 1
for x in range(n):
    W += A
    sum += a[x]
    while j >= 0 and W > s:
        W -= B
        sum -= b[j]
        j -= 1

    if W > s:
        break
    ans = max(ans, sum)


print(ans)
