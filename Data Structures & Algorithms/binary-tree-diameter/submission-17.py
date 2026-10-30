# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        maxDiameter = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter

            if not root:
                return -1

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            height = 1 + max(leftHeight, rightHeight)
            diameter = leftHeight + rightHeight + 2
            if diameter > maxDiameter:
                maxDiameter = diameter
            return height
        
        dfs(root)
        return maxDiameter

        #O(n) time
        #O(1) space