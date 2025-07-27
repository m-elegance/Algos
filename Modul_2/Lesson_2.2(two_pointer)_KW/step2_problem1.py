# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 2 » A) отрезок с небольшой суммой
n, s = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
cnt = 0
max_len = 0
i = 0

for j in range(n):
    
    while i < n and sum + a[i] <= s:
        cnt += 1
        sum += a[i]
        max_len = max(max_len, cnt)
        i += 1    
    cnt -= 1
    sum -= a[j]

print(max_len)






