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

        def valid(root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
            if not root:
                return True

            if root.val >= maximum or root.val <= minimum:
                return False
            
            #THIS IS SO WRONG AND WILL DESTROY YOUR ALGORITHM
            # maximum = max(maximum, root.val)
            # minimum = min(minimum, root.val)

            #THIS WILL ALSO DESTROY YOUR ALGORITHM
            #return valid(root.left, minimum, max(maximum, root.val)) and valid(root.right, min(minimum, root.val), maximum)

            return valid(root.left, minimum, min(maximum, root.val)) and valid(root.right, max(minimum, root.val), maximum)
            

        return valid(root, float('-inf'), float('inf'))

        #O(n) time
        #O(h) space









        
        # CANNOT ONLY CHECK IMMEDIATE CHILDREN!!!!!!!!
        # #preorder DFS

        # if not root:
        #     return True

        # if root.left.val > root.val or root.right.val < root.val:
        #     return False

        # return self.isValidBST(root.left) and self.isValidBST(root.right)

        # #O(n) time
        # #O(h) space



        