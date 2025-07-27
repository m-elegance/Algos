my_dict = {"a": 5, "g": 0, "t": 32, "lol": 32, "omg": 65, "eboy": 15}


def max_numb(my_dict):
    arr = []
    for i in my_dict:
        arr.append(my_dict[i])
    arr.sort()
    max_two = [arr[-2], arr[-1]]
    return max_two


ans = max_numb(my_dict)
print(ans)
for i in my_dict:
    if my_dict[i] in ans:
        ans.remove(my_dict[i])
        print(i)
