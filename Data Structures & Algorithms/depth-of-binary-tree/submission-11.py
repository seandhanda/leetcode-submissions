# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Iterative BFS
        if not root:
            return 0
        
        q = deque()
        q.append(root) 

        height = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
            height += 1

        return height

        #O(n) time
        #O(w) where w is max width of the tree


        # #Recursiove DFS
        # if not root:
        #     return 0

        # height = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # return height

        # #O(n) space
        # #O(h) space