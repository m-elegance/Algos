# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » A) зацикленный плейлист
n, p = map(int, input().split())
a = list(map(int, input().split()))

all_sum = sum(a)

l = 0
sum = 0
cnt = 0

ans = p + 1

for r in range(n):
    rnd = p // all_sum
    sum = all_sum * rnd
    cnt = rnd * n

    l = r
    while l < n and sum < p:
        sum += a[l]
        l += 1
        cnt += 1

    l = 0
    while l < n and sum < p:
        sum += a[l]
        l += 1
        cnt += 1

    if ans > cnt:
        ans = cnt
        pos_start = r + 1


print(pos_start, ans)
