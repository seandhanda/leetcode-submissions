# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        solution = True


        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal solution
            
            if not root:
                return -1

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if abs(leftHeight - rightHeight) > 1:
                solution = False
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)

        return solution

        #O(n) time
        #O(h) space
                 