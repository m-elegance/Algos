#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: H) гамбургеры
def ok(mid, cntB, cntS, cntC, nB, nS, nC, pB, pS, pC, money):
    generalB = mid * cntB
    generalS = mid * cntS
    generalC = mid * cntC

    if nB < generalB:
        money -= (generalB - nB) * pB
    if nS < generalS:
        money -= (generalS - nS) * pS
    if nC < generalC:
        money -= (generalC - nC) * pC

    return money >= 0


s = input()
n_B, n_S, n_C = map(int, input().split())
p_B, p_S, p_C = map(int, input().split())

money = int(input())

cnt_B = cnt_S = cnt_C = 0

for i in s:
    if i == 'B':
        cnt_B += 1
    if i == 'S':
        cnt_S += 1
    if i == 'C':
        cnt_C += 1

cnt = 0
while cnt_B <= n_B and cnt_S <= n_S and cnt_C <= n_C:
    n_B -= cnt_B
    n_S -= cnt_S
    n_C -= cnt_C

    cnt += 1


l = 0
r = 10**14
res = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, cnt_B, cnt_S, cnt_C, n_B, n_S, n_C, p_B, p_S, p_C, money):    #mid, nB, nS, nC, cntB, cntS, cntC, money
        l = mid + 1
        res = mid
    else:
        r = mid - 1

print(cnt + res)








