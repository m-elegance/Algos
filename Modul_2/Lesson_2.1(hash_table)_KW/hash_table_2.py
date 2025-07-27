#в словари можно добавлять таблы(листы, только их нельзя изменять)


my_dict = {}
s = ["abc", "abc", "qw", "qw", "qw", "y"]
# abc = 2
# qw = 3
# y = 1


for st in s:
    if st in my_dict:
        my_dict[st] += 1
    else:
        my_dict[st] = 1


a = [1, 2, 3]
b = (1, 2, 3)


print(my_dict)



