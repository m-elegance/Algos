my_dict = {}
n = 33

for i in range(1, n + 1):
    my_dict[i] = chr((i - 1) % 32 + ord("а"))

print(my_dict)
