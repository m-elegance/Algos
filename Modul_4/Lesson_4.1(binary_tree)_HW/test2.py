class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, None, None), None),
    TreeNode(3, TreeNode(2, TreeNode(4, None, None), None), TreeNode(4, None, None)),
)

ans = []


def dfs(root, my_dict):
    if not root:
        return ""
    s = "[" + dfs(root.left, my_dict) + str(root.val) + dfs(root.right, my_dict) + "]"
    if s not in my_dict:
        my_dict[s] = [root]
    elif s in my_dict and len(my_dict[s]) <= 1:
        my_dict[s].append(root)
    return s


my_dict = {}
dfs(root, my_dict)
# for i in my_dict:
#     if len
ans = [i[0] for i in my_dict.values() if len(i) > 1]


print(ans)
