# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 1 » B) число меньших
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
i = 0
j = 0

while j < m or i < n:
    if i == n:
        res.append(i)
        j += 1
    elif j == m:
        i += 1
    else:
        if a[i] < b[j]:
            i += 1
        else:
            res.append(i)
            j += 1

print(*res)


# 6 5
# 1 6 9 13 18 18
# 2 3 8 13 15