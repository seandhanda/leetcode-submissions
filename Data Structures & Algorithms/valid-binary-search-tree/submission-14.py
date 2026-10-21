# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        solution = True

        if not root: 
            return True

        def dfs(root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
            if not root:
                return True
            
            if root.val >= maximum or root.val <= minimum:
                return False
            
            return dfs(root.left, minimum, min(maximum, root.val)) and dfs(root.right, max(minimum, root.val), maximum) 

        return dfs(root, float('-inf'), float('inf'))

        #O(n) time
        #O(h) space
