#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 4: C) выбор пар
def ok(mid, a, b, k):
    n = len(a)
    c = [0] * n
    for i in range(n):
        c[i] = a[i] - mid * b[i]
    c.sort(reverse=True)

    sum = 0
    cnt = 0
    for i in range(n):
        if c[i] >= 0:
            sum += c[i]
            
            cnt += 1
    
    for i in range(n):
        if c[i] < 0:
            sum += c[i]
            if sum < 0:
                break
            cnt += 1


    return cnt >= k





n, k = map(int, input().split())

a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

l = 0
r = 10**10
ans = 0

while (r - l) >= 10**(-8):
    mid = (l + r) / 2
    if ok(mid, a, b, k):
        l = mid
        ans = mid
    else:
        r = mid

print(ans)






