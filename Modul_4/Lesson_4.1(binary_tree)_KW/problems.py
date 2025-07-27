# 1022, 104, 112, 543, 2583, 2368, 1382, 129, 654


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


diam = 0
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)),
    TreeNode(3, None, None),
)


ans = []


def dfs_postord(root: TreeNode):
    global ans
    if root != None:
        print(root.val)
    ans.append(root.val)
    if root.left:
        dfs_postord(root.left)
    if root.right:
        dfs_postord(root.right)
    print(ans)


dfs_postord(root)

n = None
m = 2
n = 0
print(n + m)
