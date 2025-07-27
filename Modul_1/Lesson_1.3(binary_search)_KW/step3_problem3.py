# codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 3: C) коровы в стойла

#ну вроде так: если необходимо минимизировать, то мы сдвигаем в if'e правую границу, в else'e - левую, иначе наоборот
#а также если нужно минимизировать, то в ok() мы ретернем <=, а если нужно максимизировать то x >= k, как в данной задаче
def ok(mid, arr, k):
    cnt = 1
    left = arr[0]
    for i in range(1, len(arr)):
        right = arr[i]
        if right - left >= mid:
            cnt += 1
            left = arr[i]

    return cnt >= k


n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 10**9
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, arr, k):
        # r = mid - 1
        l = mid + 1
        ans = mid
    else:
        # l = mid + 1
        r = mid - 1

print(ans)