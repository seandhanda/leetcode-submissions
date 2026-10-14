# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS in order traversal

        if not root:
            return []

        solution = []

        queue = collections.deque([root])

        while queue:
            tempSolution = []

            for i in range(len(queue)):
                node = queue.popleft()
                tempSolution.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            solution.append(tempSolution)

        return solution

        #O(n) tim
        #O(max width)

