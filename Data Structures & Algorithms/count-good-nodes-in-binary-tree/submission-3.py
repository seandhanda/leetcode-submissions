# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #preorder DFS
        
        if not root:
            return 0
        
    


        def dfs(root: Optional[TreeNode], maximum: int) -> int:
            if not root:
                return 0

            res = 0

            if root.val >= maximum:
                res += 1

            maximum = max(maximum, root.val)            
            return res + dfs(root.left, maximum) + dfs(root.right, maximum)

            


        maximum = float('-inf')

        return dfs(root, maximum)

        #O(n) time
        #O(h) space








