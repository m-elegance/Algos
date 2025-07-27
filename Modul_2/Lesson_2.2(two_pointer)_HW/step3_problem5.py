# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » E) рюкзак на отрезке

n, s = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))


l = 0

weight = 0
sum_otr = 0

ans_sum = 0

for r in range(n):
    weight += w[r]
    sum_otr += c[r]
    while l < n and weight > s:
        weight -= w[l]
        sum_otr -= c[l] 
        l += 1

    ans_sum = max(ans_sum, sum_otr)

print(ans_sum)
