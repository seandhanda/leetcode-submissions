# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0


        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(dfs(root.left), dfs(root.right))

        return dfs(root)    

        #O(n) time
        #O(h) space, worst case n for skewed, best case is logn for balanced


    