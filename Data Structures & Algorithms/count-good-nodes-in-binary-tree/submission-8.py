# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        solution = 0

        # if not root:
        #     return solution

        def dfs(root: TreeNode, maximum: int) -> None:
            nonlocal solution
            
            if not root:
                return None
            
            if root.val >= maximum:
                solution += 1
            
            maximum = max(maximum, root.val)
            dfs(root.left, maximum)
            dfs(root.right, maximum)
            return

        dfs(root, float('-inf'))
        return solution
        
        #O(n) time
        #O(h) space