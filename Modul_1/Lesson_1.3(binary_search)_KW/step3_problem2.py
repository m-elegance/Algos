# codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 3: B) разделение массива
def ok(mid, arr, k):
    cnt = 1
    sum = 0
    for i in range(len(arr)):
        # if sum + arr[i] > mid:
        #     cnt += 1
        #     sum = arr[i]
        # else:
        #     sum += arr[i]
        sum += arr[i]
        if sum > mid:
            cnt += 1
            sum = arr[i]

    return cnt <= k


n, k = map(int, input().split())

arr = list(map(int, input().split()))
l = max(arr)
r = sum(arr)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, arr, k):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)
