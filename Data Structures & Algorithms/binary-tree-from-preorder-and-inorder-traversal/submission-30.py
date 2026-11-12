# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for index, value in enumerate(inorder):
            inorderMap[value] = inorderMap.get(value, index) 


        def dfs(pStart: int, pEnd: int, iStart: int, iEnd: int) -> Optional[TreeNode]:
            if pStart > pEnd or iStart > iEnd:
                return None
            root = TreeNode(preorder[pStart])
            index = inorderMap[root.val] 
            leftSize = index - iStart + 1
            root.left = dfs(pStart+1, (pStart+1)+leftSize - 2, iStart, index-1)
            root.right = dfs((pStart+1)+leftSize-1,pEnd,index+1,iEnd)

            return root

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
    
        #O(n) time
        #O(n) space