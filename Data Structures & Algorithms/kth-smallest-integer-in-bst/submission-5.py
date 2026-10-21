# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted = []

    


        def dfs(root: Optional[Treeode]) -> None:
            #in order traversal

            if not root:
                return

            dfs(root.left)
            sorted.append(root.val)
            dfs(root.right)
            return
                
        dfs(root)

        return sorted[k-1]

        #O(n) time
        #O(n) space