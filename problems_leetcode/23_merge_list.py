class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list_1 = ListNode(1, ListNode(4, ListNode(5)))
list_2 = ListNode(1, ListNode(3))
list_3 = ListNode(3, ListNode(6))
arr = [list_1, list_2, list_3]


def none_plus(list):
    while list.next:
        list = list.next
    list.next = ListNode(None)


def create_ans(ans, list_1, list_2):

    if list_1.next or list_2.next:
        if list_1.next == None:
            ans.next = ListNode(list_2.val)
            list_2 = list_2.next
            create_ans(ans.next, list_1, list_2)
        elif list_2.next == None:
            ans.next = ListNode(list_1.val)
            list_1 = list_1.next
            create_ans(ans.next, list_1, list_2)
        else:
            if list_1.val > list_2.val:
                ans.next = ListNode(list_2.val)
                list_2 = list_2.next
                create_ans(ans.next, list_1, list_2)
            else:
                ans.next = ListNode(list_1.val)
                list_1 = list_1.next
                create_ans(ans.next, list_1, list_2)


# none_plus(list_1)
# none_plus(list_2)


# if list_1.val > list_2.val:
#     ans = ListNode(list_2.val)
#     list_2 = list_2.next
#     create_ans(ans, list_1, list_2)
# else:
#     ans = ListNode(list_1.val)
#     list_1 = list_1.next
#     create_ans(ans, list_1, list_2)
ans = arr[0]
for i in range(1, len(arr)):
    none_plus(ans)
    none_plus(arr[i])
    if ans.val > arr[i].val:
        temp = ListNode(arr[i].val)
        arr[i] = arr[i].next
        create_ans(temp, ans, arr[i])
    else:

        temp = ListNode(ans.val)
        ans = ans.next
        create_ans(temp, ans, arr[i])
    ans = temp


while ans.next:
    print(ans.val, end=" ")
    ans = ans.next
print(ans.val)
