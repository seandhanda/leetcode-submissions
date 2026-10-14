# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS in order traversal

        solution = []

        queue = collections.deque([root])

        while queue:
            tempSolution = []

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    tempSolution.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tempSolution:
                solution.append(tempSolution)

        return solution

        #O(n) tim
        #O(max width)

