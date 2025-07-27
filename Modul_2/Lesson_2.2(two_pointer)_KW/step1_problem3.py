# ITMO Academy: пилотный курс » Метод двух указателей » Шаг 1 » C) число пар равных
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Решение через два указателя

# i = 0
# res = []

# for j in range(m):
#     cnt = 0
#     while i < n and a[i] <= b[j]:
#         if a[i] == b[j]:
#             cnt += 1
#         i += 1

#     if j > 0 and b[j] == b[j - 1]:
#         res.append(res[-1])
#     else:
#         res.append(cnt)

# print(sum(res))


# Решение через словарь
my_dict = {}
for i in a:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1


cnt = 0
for j in b:
    if j in my_dict:
        cnt += my_dict[j]


print(cnt)





