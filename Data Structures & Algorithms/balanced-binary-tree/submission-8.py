# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        solution = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal solution

            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            height = 1 + max(leftHeight, rightHeight)

            if abs(leftHeight-rightHeight) > 1:
                solution = False

            return height
        
        dfs(root)
        return  solution

        #O(n) time
        #O(1) space

        
