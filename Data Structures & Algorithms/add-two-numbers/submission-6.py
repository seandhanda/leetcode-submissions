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
        
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            res = v1 + v2 + carryover
            curr.next = ListNode(res % 10)
            carryover = res // 10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        # while l1 and l2:
        #     res = l1.val + l2.val + carryover
        #     curr.next = ListNode(val = res % 10)
        #     carryover = res // 10
        #     l1 = l1.next
        #     l2 = l2.next
        #     curr = curr.next

        # while l1:
        #     res = l1.val + carryover
        #     curr.next = ListNode(res % 10)
        #     carryover = res // 10
        #     l1 = l1.next
        #     curr = curr.next

        # while l2:
        #     res = l2.val + carryover
        #     curr.next = ListNode(res % 10)
        #     carryover = res // 10
        #     l2 = l2.next
        #     curr = curr.next

        #final carryover
        if carryover:
            curr.next = ListNode(carryover)

        return dummy.next

        #O(n) runtime
        #O(1) space