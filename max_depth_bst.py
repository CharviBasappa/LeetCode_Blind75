from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# Sample Test Cases
def test():
    solution = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(f"{solution.maxDepth(root1)}")

    root2 = TreeNode(1, None, TreeNode(2))
    print(f"{solution.maxDepth(root2)}")

    print(f"{solution.maxDepth(None)}")

    root3 = TreeNode(5)
    print(f"{solution.maxDepth(root3)}")

    root4 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    print(f"{solution.maxDepth(root4)}")

    root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
    print(f"{solution.maxDepth(root5)}")

# Run Tests
test()
