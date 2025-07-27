#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: A) упаковка прямоугольников
def ok(w, h, mid, n):
    return (mid // w) * (mid // h) >= n


w, h, n = map(int, input().split())

l = 1
r = n * max(w * h)
ans = 0
    
while l <= r:
    mid = (l + r) // 2
    if ok(h, w, mid, n):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)





