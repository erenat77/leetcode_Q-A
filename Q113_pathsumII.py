# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        solution = []
        current_path = []

        def dfs( node: TreeNode):
            if not node:
                return

            # update current path
            current_path.append(node.val)

            # check root-to-leaf path's summation is met or not
            if not node.left and not node.right and sum(current_path) == total:
                solution.append(list(current_path))

            # DFS down to next level, divide and conquer
            dfs( node.left )
            dfs( node.right )
            # DFS of this subtree is completed
            current_path.pop()

        #---------------------------------------
        dfs(root)
        return solution

class Solution1(object):
    def pathSum(self, root, sum):
        res=[]
        def dfs(r, s, path):
            if not r: return
            if not r.left and not r.right:
                if not (s-r.val): res.append(path+[r.val])
                return
            if r.left:  dfs(r.left,  s-r.val, path+[r.val])
            if r.right: dfs(r.right, s-r.val, path+[r.val])
        dfs(root, sum, [])
        return res
