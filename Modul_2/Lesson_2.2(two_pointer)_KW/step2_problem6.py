# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 2 » F) отрезки с небольшим разбросом
n, k = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
cnt = 0
ans = 0

for i in range(n):
    max_elem = arr[i]
    min_elem = arr[i]
    while j < n and max_elem - min_elem <= k:
        max_elem = max(max_elem, arr[j])
        min_elem = min(min_elem, arr[j])
        
        if max_elem - min_elem > k:
            break

        j += 1
        cnt += 1
    
    ans += cnt
    cnt -= 1
    
print(ans)

