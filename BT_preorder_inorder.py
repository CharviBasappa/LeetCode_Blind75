from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root

from collections import deque

def level_order_traversal(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

# Sample test cases
sol = Solution()

# Test case 1
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
tree1 = sol.buildTree(preorder1, inorder1)
print(level_order_traversal(tree1))  # Output: [3, 9, 20, None, None, 15, 7]

# Test case 2
preorder2 = [-1]
inorder2 = [-1]
tree2 = sol.buildTree(preorder2, inorder2)
print(level_order_traversal(tree2))  # Output: [-1]
