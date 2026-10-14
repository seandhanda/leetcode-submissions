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
        
    


        def dfs(root: Optional[TreeNode], max: int) -> int:
            if not root:
                return 0

            res = 0

            if root.val >= max:
                res += 1
                return res + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return res + dfs(root.left, max) + dfs(root.right, max)


        max = float('-inf')

        return dfs(root, max)

        #O(n) time
        #O(h) space








