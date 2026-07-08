from typing import Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val

            root = root.right


# Driver Code

# Creating the BST:
#         5
#       /   \
#      3     6
#     / \
#    2   4
#   /
#  1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

k = 3

obj = Solution()
print("The", k, "smallest element is:", obj.kthSmallest(root, k))