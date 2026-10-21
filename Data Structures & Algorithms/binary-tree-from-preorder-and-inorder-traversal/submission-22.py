# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderLookup = {}
        for i in range(len(inorder)):
            inorderLookup[inorder[i]] = i


        def helper(preorderStart: int, preorderEnd, inorderStart: int, inorderEnd: int) -> Optional[TreeNode]:
            if preorderStart > preorderEnd or inorderStart > inorderEnd:
                return None
            
            
            root = TreeNode(preorder[preorderStart])
            index = inorderLookup[root.val]
            root.left = helper(preorderStart+1,(preorderStart + 1) + (index-inorderStart) - 1, inorderStart, index-1)
            root.right = helper(((preorderStart + 1) + (index-inorderStart) - 1) + 1, preorderEnd, index+1, inorderEnd)
            return root

        return helper(0, len(preorder)-1,0, len(inorder)-1)

        #O(n) time
        #O(n) space
