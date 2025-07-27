#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 1: B) ближайшее слева

n, k = map(int, input().split())

arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

def ok(arr, mid, x):
    return arr[mid] <= x


for i in arr_k:
    l = 0
    r = n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if ok(arr_n, mid, i):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    
    if arr_n[0] > i:
        print(0)
    else:
        print(ans + 1)



    











