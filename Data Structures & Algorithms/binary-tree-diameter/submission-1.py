# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        if not root:
            return self.diameter

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight + 2)

            return max(leftHeight, rightHeight) + 1 


        dfs(root)

        return self.diameter

        #O(n) time
        #O(h) space