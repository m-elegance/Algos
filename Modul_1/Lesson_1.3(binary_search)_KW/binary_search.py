


def ok(a, mid, x):
    return a[mid] <= x

a = [1, 1, 3, 4, 7, 8]
l = 0
r = len(a) - 1
ans = 0
x = 7

while l <= r:
    mid = (l + r) // 2
    if ok(a, mid, x):
        #Вы хотите найтии максимум или минимум
        #Если хотим минимизировать, то сдвигаем левую границу, иначе правую
        #рассмотрим МАКСИМИЗАЦИЮ
        #r = mid - 1
        l = mid + 1
        ans = mid
    else: 
        #l = mid + 1
        r = mid - 1

print(ans, a[ans])
