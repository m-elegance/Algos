#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 1: E) уравнение
from math import *


def ok(mid, c):
    return mid*mid + sqrt(mid) <= c


c = float(input())
l = 0
r = 10**10
ans = 0

for i in range(100):
    mid = (l + r) / 2
    if ok(mid, c):
        l = mid
        ans = mid 
    else:
        r = mid
    
print(ans)