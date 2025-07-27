# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 2 » E) отрезки с небольшим множеством

n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
cnt = 0
ans = 0
my_dict = {}

for r in range(n):
    if arr[r] in my_dict:
        my_dict[arr[r]] += 1
    else:
        my_dict[arr[r]] = 1
    
    while l < n and len(my_dict) > k:
        my_dict[arr[l]] -= 1
        if my_dict[arr[l]] == 0:
            del my_dict[arr[l]]
        l += 1

    ans += r - l + 1

print(ans) 

    






