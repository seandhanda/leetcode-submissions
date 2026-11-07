# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow
        
        # Reverse Middle 
        curr = middle.next
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head2 = prev
        middle.next = None

        #merge
        while head and head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head.next.next = temp1
            head = temp1
            head2 = temp2


        return 

        #O(n) time
        #O(1) space