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
        #Pass 1 Deep Copy + HashMap
        oldToCopy = {}
        curr = head
        while curr:
            copy = Node(x = curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        

        #Pass 2 next pointers and random pointers
        curr = head
        while curr:
            oldToCopy[curr].next = oldToCopy[curr.next] if curr.next else None
            oldToCopy[curr].random = oldToCopy[curr.random] if curr.random else None    #REVIEW!
            curr = curr.next
        
        return oldToCopy[head] if head else None
        #O(n) space
        #O(n) time

#if no Random Pointers - leave copy.next unitialized enitrely.
# dummy = Node()
# curr = head
# copy = dummy

# while curr:
#     copy.next = Node(curr.val)
#     copy = copy.next
#     curr = curr.next
# return dummy.next