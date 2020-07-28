# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # depth first search
        def dfs(root,sum):
            # if not root
            if not root:
                return False
            else:
                # if there is a root, extract the root values
                sum-=root.val
            # if it is leaf node and sum becomes zero, then path is existed
            if root.left is None and root.right is None and sum==0:
                return True
            left = dfs(root.left,sum)
            right = dfs(root.right,sum)
            return left or right

        return dfs(root,sum)
