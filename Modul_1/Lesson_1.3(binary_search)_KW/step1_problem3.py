#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 1: С) ближайшее справа
n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

def ok(arr, mid, x):
    return arr[mid] >= x

for x in arr_k:
    l = 0
    r = n - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if ok(arr_n, mid, x):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1

    if arr_n[n - 1] < x:
        print(n + 1)
    else:
        print(ans + 1)