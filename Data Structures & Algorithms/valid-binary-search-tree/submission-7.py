# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root: Optional[TreeNode], min: int, max: int) -> bool:
            if not root:
                return True

            if root.val >= max or root.val <= min:
                return False
            else:
                return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)


        return dfs(root, float('-inf'), float('inf'))

        #O(n) time
        #O(h) space
