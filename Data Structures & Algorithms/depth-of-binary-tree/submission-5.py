# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        solution = 0

        stack = [(root,1)]

        while stack:
            popTuple = stack.pop()
            solution = max(solution, popTuple[1])
            if popTuple[0].left:
                stack.append((popTuple[0].left, popTuple[1]+1))
            if popTuple[0].right:
                stack.append((popTuple[0].right, popTuple[1]+1))

        return solution

        #O(n) time
        #O(h) space