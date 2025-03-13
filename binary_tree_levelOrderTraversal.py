from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_nodes)
        
        return result
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

# Sample Test Cases
def test():
    solution = Solution()

    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"{solution.levelOrder(root1)}")  # Output: [[3], [9, 20], [15, 7]]
    print(f"Max Depth: {solution.maxDepth(root1)}")  # Output: 3

    root2 = TreeNode(1)
    print(f"{solution.levelOrder(root2)}")  # Output: [[1]]
    print(f"Max Depth: {solution.maxDepth(root2)}")  # Output: 1

    print(f"{solution.levelOrder(None)}")  # Output: []
    print(f"Max Depth: {solution.maxDepth(None)}")  # Output: 0

    root3 = TreeNode(5, TreeNode(6, TreeNode(7)), TreeNode(8, TreeNode(9), TreeNode(10)))
    print(f"{solution.levelOrder(root3)}")  # Output: [[5], [6, 8], [7, 9, 10]]
    print(f"Max Depth: {solution.maxDepth(root3)}")  # Output: 3

# Run Tests
test()
