# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        solution = 0

        def dfs(root: TreeNode, maximum: int) -> None:
            nonlocal solution
            
            if not root:
                return
            
            if root.val >= maximum:
                solution += 1
            
            dfs(root.left, max(maximum, root.val))
            dfs(root.right, max(maximum, root.val))

        dfs(root, float('-inf'))
        return solution

        #O(n) time
        #O(h) space