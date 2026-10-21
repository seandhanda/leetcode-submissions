# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0


        diameter = float('-inf')

        def dfs(root: Optional[TreeNode]):
            nonlocal diameter
          
            if not root:
                return 0


            heightLeft, heightRight = dfs(root.left), dfs(root.right)
            
            diameter = max(diameter, heightLeft + heightRight)
            
            return 1 + max(heightLeft, heightRight)

        dfs(root)
        return diameter

        #O(n) time
        #O(h) space



