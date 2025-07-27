from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


root = Node(2, [Node(3, [Node(5, None), Node(7, None)]), Node(4, None)])
ans = []


def dfs(root):
    if not root:
        return
    global ans
    child = root.children
    if child != None:
        for i in child:
            dfs(i)
        ans.append(root.val)
    else:
        ans.append(root.val)


dfs(root)
print(ans)
