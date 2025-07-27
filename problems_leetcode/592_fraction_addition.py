expression = "7/3+5/2-3/10"
n = len(expression)
den = []
num = []
flag = False
for i in range(n):
    if expression[i] == "/":
        if i - 2 >= 0:
            num.append(expression[i - 2] + expression[i - 1])
        else:
            num.append(expression[i - 1])
        den.append(expression[i + 1])
print(num)
print(den)
NOK = 0
for i in range(1, len(num)):
    NOK = max(int(den[i - 1]), int(den[i]))
    while True:
        if (NOK % int(den[i - 1]) == 0) and (NOK % int(den[i]) == 0):
            break
        NOK += 1
    num[i] = str(
        int(num[i - 1]) * NOK // int(den[i - 1]) + int(num[i]) * NOK // int(den[i])
    )
    den[i] = str(NOK)

print(den, num)

if int(num[-1]) < 0:
    flag = True

k = abs(int(num[-1]))
m = int(den[-1])

for i in range(2, k + 1):
    while m % i == 0 and k % i == 0:
        m = m // i
        k = k // i

if flag:
    k = -k
    print(str(k) + "/" + str(m))
elif k == 0:
    print("0/1")
else:
    print(str(k) + "/" + str(m))
