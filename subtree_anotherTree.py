class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def isSame(a, b):
            if not a and not b: return True
            if not a or not b or a.val != b.val: return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)
        
        if not root: return False
        if isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def build(vals):
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Test cases
root1 = build([3, 4, 5, 1, 2])
sub1 = build([4, 1, 2])
print(Solution().isSubtree(root1, sub1))  # True

root2 = build([3, 4, 5, 1, 2, None, None, None, None, 0])
sub2 = build([4, 1, 2])
print(Solution().isSubtree(root2, sub2))  # False
