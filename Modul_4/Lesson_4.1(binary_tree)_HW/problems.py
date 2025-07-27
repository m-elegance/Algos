# 617, 653, 144, 101, 2415, 958, 1325, 652, 98
# не сделано:
# || 427 ||
# || 2581 ||

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)),
    TreeNode(3, None, None),
)

target = 3
def dfs(root, target):
    if root:
        root.left = dfs(root.left, target)
        root.right = dfs(root.right, target)
        if root.val == target and root.left == None and root.right == None:
            root = None
    
    return root     #необходимо для фильтрации None значений 
                    #(т.е. когда мы попадаем в None узел, то возвращаем None узел)


dfs(root, target)
print(root.val)




