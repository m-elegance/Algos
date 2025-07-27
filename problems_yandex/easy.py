s = "abbbbbbabcde"
my_dict = {}
ans = 0
l = 0
for i in s:
    if i not in my_dict:
        my_dict[i] = 1
        ans = max(ans, len(my_dict))
    else:
        my_dict[i] = 2
        while my_dict[i] != 1:
            my_dict[s[l]] -= 1
            if my_dict[s[l]] == 0:
                del my_dict[s[l]]
            l += 1

print(ans)
