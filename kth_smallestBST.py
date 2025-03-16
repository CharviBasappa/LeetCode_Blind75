from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        inorder_list = inorder_traversal(root)
        return inorder_list[k - 1]

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def construct_bst_from_list(values):
    root = None
    for val in values:
        if val is not None:
            root = insert_into_bst(root, val)
    return root

# Sample Test Cases
sol = Solution()

# Test Case 1
root1 = construct_bst_from_list([3,1,4,None,2])
k1 = 1
print(sol.kthSmallest(root1, k1))  # Output: 1

# Test Case 2
root2 = construct_bst_from_list([5,3,6,2,4,None,None,1])
k2 = 3
print(sol.kthSmallest(root2, k2))  # Output: 3
