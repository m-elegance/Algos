#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 1: A) двоичный поиск

n, k = map(int, input().split())

arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

def ok(arr, mid, x):
    return arr[mid] <= x

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if ok(arr, mid, x):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    if arr[ans] == x:
        return True
    else:
        return False
    
for i in range(k):
    if binary_search(arr_n, arr_k[i]):
        print("YES")
    else:
        print("NO")
