# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        fast = head
        slow = dummy

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        #slow is my nth node from the right   
        slow.next = slow.next.next

        return dummy.next #WRONG! when list is of size 1 and n is 1, head points to deleted node, dummy.next points to correct solutoin (empty list)

        #O(1) space
        #O(n) time 

        #*review