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
                return -1


            heightLeft, heightRight = dfs(root.left), dfs(root.right)
            
            diameter = max(diameter, 2 + heightLeft + heightRight)
            
            return 1 + max(heightLeft, heightRight)

        dfs(root)
        return diameter

        #O(n) time
        #O(h) space


#Diameter is Rheight + Lheight + 2 OR its number of nodes in left + number of nodes in right


