# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        solution = 0 

        if not root:
            return 0


        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal solution

            if not root:
                return -1
            
            heightLeft = dfs(root.left)
            heightRight = dfs(root.right)
            height = 1 + max(heightLeft, heightRight)

            diameter = 2 + heightLeft + heightRight
            if diameter > solution:
                solution = diameter

            return height

        dfs(root)
        return solution
        
        #O(n) time
        #O(h) space
