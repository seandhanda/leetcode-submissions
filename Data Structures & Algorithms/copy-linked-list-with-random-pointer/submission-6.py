"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        solution = Node(0)
        curr = head
        currCopy = solution

        map = {}
        map[None] = None

        while curr:
            copyNode = Node(curr.val)
            currCopy.next = copyNode
            currCopy = currCopy.next
            map[curr] = currCopy
            curr = curr.next

        curr = head
        currCopy = solution.next
        while curr:
            currCopy.random = map[curr.random]
            curr = curr.next
            currCopy = currCopy.next

        return solution.next

        #O(n) time
        #O(n) space