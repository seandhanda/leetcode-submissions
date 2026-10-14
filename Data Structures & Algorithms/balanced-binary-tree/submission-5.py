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

            heightLeft = dfs(root.left)
            heightRight = dfs(root.right)

            if abs(heightLeft - heightRight) > 1:
                solution = False

            return max(heightLeft, heightRight) + 1

        dfs(root)

        return solution

        #O(n) time
        #O(h) space