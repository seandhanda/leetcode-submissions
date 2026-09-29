# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None

        # while head:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        #     head = temp
        
        # return prev
        # #O(n) runtime
        # #O(1) space

        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev    
        # #O(n) runtime
        # #O(1) space



        # Recursive 
        #O(n) runtime
        #O(n) space 
        #suboptimal
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    # Why O(n) space?
    #Because every recursive call creates a new function stack frame, and those frames all remain in memory until the recursion starts returning.



