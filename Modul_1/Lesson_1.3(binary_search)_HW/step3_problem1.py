#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 3: A) собраться вместе
def ok(mid, x, v):
    n = len(x)
    min_right = x[0] + mid * v[0]
    max_left = x[0] - mid * v[0]
    for i in range(n):
        left = x[i] + mid * v[i]
        right = x[i] - mid * v[i]
        min_right = min(min_right, left)
        max_left = max(max_left, right)

    return max_left <= min_right

n = int(input())
x = [0] * n
v = [0] * n

for i in range(n):
    x[i], v[i] = map(int, input().split())

l = 0
r = 10**10
ans = 0

for i in range(100):
    mid = (l + r) / 2
    if ok(mid, x, v):
        r = mid
        ans = mid
    else:
        l = mid

print(ans)











