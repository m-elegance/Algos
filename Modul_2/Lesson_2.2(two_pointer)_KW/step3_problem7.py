# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 3 » G) не очень грубая подстрока
n, c = map(int, input().split())
s = input()

ans = 0
rud = 0
cnt_a = 0
cnt_b = 0
l = 0

for r in range(n):
    if s[r] == 'a':
        cnt_a += 1
    elif s[r] == 'b':
        cnt_b += 1
        rud += cnt_a
    
    while l < n and rud > c:
        if s[l] == 'a':
            rud -= cnt_b
            cnt_a -= 1
        elif s[l] == 'b':
            cnt_b -= 1
        l += 1
    ans = max(ans, r - l + 1)

print(ans)








