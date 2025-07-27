#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: G) студенческие советы
def ok(mid, arr, k):
    sum = 0
    for i in range(len(arr)):
        sum += min(mid, arr[i])
    return sum >= mid * k
    
k, n = int(input()), int(input())
arr = [int(input()) for i in range(n)]

l = 0
r = sum(arr)

while l <= r:
    mid = (l + r) // 2
    if ok(mid, arr, k):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1
print(ans)

