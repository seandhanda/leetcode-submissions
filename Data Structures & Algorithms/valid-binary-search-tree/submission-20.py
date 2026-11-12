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
        
        def dfs(root: Optional[TreeNode], max: int, min:int) -> bool:
            if not root:
                return True
            
            if root.val >= max or root.val <= min:
                return False
            
            return dfs(root.left, root.val, min) and dfs(root.right, max, root.val)

        return dfs(root, float('inf'), float('-inf'))
        
        #O(n) time
        #O(height) space
    

        