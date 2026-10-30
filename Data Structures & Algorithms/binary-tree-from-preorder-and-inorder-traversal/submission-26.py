# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        def dfs(preorderStart: int, preorderEnd: int, inorderStart: int, inorderEnd: int) -> Optional[TreeNode]:
            if (preorderStart > preorderEnd or inorderStart > inorderEnd):
                return None
            
            root = TreeNode(preorder[preorderStart])

            # index = inorder.index[preorder[preorderStart]]
            index = inorderMap[preorder[preorderStart]]
            root.left = dfs(preorderStart+1, (preorderStart+1) + (index-inorderStart) - 1, inorderStart, index-1)
            root.right = dfs((preorderStart+1) + (index-inorderStart), preorderEnd, index+1, inorderEnd)
            return root


        return dfs(0,len(preorder)-1, 0, len(inorder)-1)
        
        #O(n) time
        #O(n) space