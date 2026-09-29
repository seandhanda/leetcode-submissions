# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # if not head:
        # #     return False
        
        # slow = head
        # fast = head

        # while fast and fast.next:   #we only care about fast.next.next here, and to ensure it exists, we check fast.next, but in order to check fast.next, we need to also check fast!

        #     fast = fast.next.next
        #     slow = slow.next

        #     if fast == slow:
        #         return True
            
        # return False
        # #O(1) space
        # #O(n) time









        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False














