# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root):
            # no root
            if not root:
                return 0
            # no left
            if not root.left:
                return dfs(root.right) + 1
            # no right
            if not root.right:
                return dfs(root.left) + 1
            # both exist
            else:
                return min(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)
