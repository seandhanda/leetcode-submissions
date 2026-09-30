# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carryover = 0
        
        while l1 and l2:
            res = l1.val + l2.val + carryover
            curr.next = ListNode(val = res % 10)
            carryover = res // 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            res = l1.val + carryover
            curr.next = ListNode(res % 10)
            carryover = res // 10
            l1 = l1.next
            curr = curr.next

        while l2:
            res = l2.val + carryover
            curr.next = ListNode(res % 10)
            carryover = res // 10
            l2 = l2.next
            curr = curr.next

        #final carryover
        if carryover:
            curr.next = ListNode(carryover)

        return dummy.next

        #O(n) runtime
        #O(1) space