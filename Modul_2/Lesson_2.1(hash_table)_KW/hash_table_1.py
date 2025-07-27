my_dict = {}

s = ["abcd", "wq", "xyz", "qwe"]

#my_dict[s[0]] = True
# for st in s:
#     my_dict[st] = True

# O(1) вставка ключа
for i in range(len(s)):
    my_dict[s[i]] = i
print(my_dict)

t = "abc"
if t in my_dict:    #O(1) ??
    print("y")
else:
    print("no")


for key in my_dict:
    k = my_dict[key]
