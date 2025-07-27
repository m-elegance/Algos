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


ans = []
queue = deque([root])
print(queue[0])
while queue:
    node = queue.popleft()

    left = node.left
    right = node.right

    ans.append(node.val)

    if left != None:
        queue.append(node.left)
    if right != None:
        queue.append(node.right)
print(ans)