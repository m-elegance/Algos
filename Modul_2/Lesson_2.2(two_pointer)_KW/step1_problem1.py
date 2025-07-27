# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 1 » A) слияние массивов 
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ind1 = 0
ind2 = 0

res = []

while ind1 < n and ind2 < m:
    if a[ind1] < b[ind2]:
        res.append(a[ind1])
        ind1 += 1
    else:
        res.append(b[ind2])
        ind2 += 1

if ind1 < n:
    res += a[ind1:]
else:
    res += b[ind2:]

print(*res)