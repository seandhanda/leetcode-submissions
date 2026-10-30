# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        
        def dfs(root:Optional[TreeNode]) -> None:
            if not root:
                return
            
            dfs(root.left)
            inOrder.append(root)
            dfs(root.right)
        
        dfs(root)
        return inOrder[k-1].val

        #O(n) time
        #O(n) space because inOrder list, not just height
        