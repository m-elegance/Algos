class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def ap(list, date):
    new_elem = ListNode(date)
    list = new_elem
    while list.next:
        list = list.next
    list.next = new_elem


cnt = 0


def deep_plus(list, s, cnt):
    list.next = ListNode(int(s[cnt]))
    cnt += 1
    if cnt < len(s):
        deep_plus(list.next, s, cnt)


ans = ListNode()
s = "89990001"
deep_plus(ans, s, cnt)
# while ans.next:
#     print(ans.val)
#     ans = ans.next
# print(ans.val)
print(ans)
