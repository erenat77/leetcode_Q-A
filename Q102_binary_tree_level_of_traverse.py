# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # dfs definition
        def dfs(root, level, res):
            # not root
            if not root:
                return
            # length of list should be less than level+1
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            # divide and conquer
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)
        # call the DFS
        res = []
        dfs(root, 0, res)
        return res
