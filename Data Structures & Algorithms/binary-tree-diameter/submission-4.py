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
            return solution

        def maxHeight(root: Optional[TreeNode]) -> int:
            nonlocal solution

            if not root:
                return -1
            
            heightLeft = maxHeight(root.left)
            heightRight = maxHeight(root.right)
            height = 1 + max(heightLeft, heightRight)

            solution = max(solution, heightLeft + heightRight + 2)

            return height
        
        maxHeight(root)

        return solution


        #O(n) time
        #O(h) space