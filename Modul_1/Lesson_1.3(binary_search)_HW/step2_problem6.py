#codeforces: ITMO Academy: пилотный курс » Двоичный поиск » Шаг 2: F) игра со строкой
def ok(mid, arr, s1, s2):
    delete_pos = [0] * len(s1)
    for i in range(mid):
        delete_pos[arr[i] - 1] = 1
    
    ind = 0
    for i in range(len(s1)):
        if delete_pos[i] == 1:
            continue
        if ind >= len(s2):
            return True 

        if s1[i] == s2[ind]:
            ind += 1
    return ind >= len(s2)

    # new_s = ''
    # for i in range(len(s1)):
    #     if delete_pos[i] == 1:
    #         continue
    #     new_s += s1[i]

    # return s2 in new_s



s1 = input()
s2 = input()
arr = list(map(int, input().split()))

l = 0
r = len(arr) - 1
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, arr, s1, s2):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)









