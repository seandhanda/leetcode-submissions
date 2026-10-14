# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS Recursive in order
        sorted = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return

            dfs(root.left)
            sorted.append(root)
            dfs(root.right)

            return

        dfs(root)

        return sorted[k-1].val

        #O(n) time
        #O(h) space