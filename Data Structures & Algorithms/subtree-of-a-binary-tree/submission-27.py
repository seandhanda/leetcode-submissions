# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or not subRoot:
            return True
        if not root:
            return False        

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and not q):
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            else:
                return dfs(p.left, q.left) and dfs(p.right, q.right)


        curr = root
        if dfs(curr, subRoot):
            return True
        else:
            return self.isSubtree(curr.left, subRoot) or self.isSubtree(curr.right, subRoot)
        

        #O(nm) time
        #O(hRoot + hSubRoot) space
        




        