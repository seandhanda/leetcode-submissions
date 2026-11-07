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
        map = {} # value : pointer
        map[None] = None
        
        curr = head
        curr2 = solution
        

        while curr:
            curr2.next = Node(x = curr.val)
            curr2 = curr2.next
            map[curr] = curr2
            curr = curr.next
        
        curr = head
        curr2 = solution.next
        while curr:
            curr2.random = map[curr.random]
            curr2 = curr2.next
            curr = curr.next

        return solution.next

        #O(n) time
        #O(n) space