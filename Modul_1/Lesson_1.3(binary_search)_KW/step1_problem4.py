#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 1: D) быстрый поиск в массиве
def ok_left(arr, mid, left):
    return arr[mid] >= left

def min_left(arr, left):
    l = 0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if ok_left(arr, mid, left):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    
    return ans

def ok_right(arr, mid, right):
    return arr[mid] <= right

def max_right(arr, right):
    l = 0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if ok_right(arr, mid, right):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    
    return ans


n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()

ans = []

k = int(input())
for i in range(k):
    left, right = map(int, input().split())
    min_l = min_left(arr_n, left)
    max_r = max_right(arr_n, right)
    if arr_n[min_l] >= left and arr_n[max_r] <= right:
        ans.append(max_r - min_l + 1)
    else:
        ans.append(0)
print(*ans)



