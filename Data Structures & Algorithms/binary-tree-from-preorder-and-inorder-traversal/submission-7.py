# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        inorderMap = defaultdict(int)
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        
        def dfs(preorderLeft: int, preorderRight: int, inorderLeft: int, inorderRight: int) -> Optional[TreeNode]:
            nonlocal preorder
            nonlocal inorder
            
            if preorderLeft > preorderRight or inorderLeft > inorderRight:
                return None

            root = TreeNode(preorder[preorderLeft])

            inorderIndex = inorderMap[preorder[preorderLeft]]

            preorderLeftSize = inorderIndex - inorderLeft
            root.left = dfs(preorderLeft+1, preorderLeft+preorderLeftSize, inorderLeft, inorderIndex-1)
            root.right = dfs(preorderLeft+1+preorderLeftSize, preorderRight, inorderIndex + 1, inorderRight)

            return root

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
        
        #O(n) time, not O(n^2)
        #O(n+h) space