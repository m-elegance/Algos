#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: В) веревочки

def ok(arr, mid, k):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i] / mid)
    
    return sum >= k
    

n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
l = 0
r = max(arr)


for i in range(100):
    mid = (l + r) / 2
    if ok(arr, mid, k):
        l = mid
        ans = mid 
    else:
        r = mid
    

print(ans)


