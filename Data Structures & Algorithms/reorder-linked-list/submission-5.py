# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #[0, n-1, 1, n-2, 2, n-3, ...]
        
        # Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow


        #Reverse Middle.next to end of list
        curr = middle.next
        middle.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head2 = prev

        #Merge

        while head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head = temp1
            head2 = temp2
        
        return
        #O(n) time
        #O(1) space

        #even/odd loop strategy for adding that middle to solution (reorder array, but return type can be new list [or existing])
        # left = 0
        # right = len(array)

        # while left <= right:
        #     solution.append(left)

        #     if left !+ right:
        #         solution.append(right)
        
        # return solution


        # Return None reorder array (not linked list, and not return array)
        # def reorder(nums):
        # left = 1
        # right = len(nums) - 1

        # while left < right:
        #     x = nums.pop(right)
        #     nums.insert(left, x)

        #     left += 2
        #     right -= 1



#Case 1: New linked list, point head to it = both head and new linked list destoryed, old head points to old linked list
#Case 2: Same linked list, same header (but this is pass by value, so different header POINTING TO OLD linked list), any changes will be permanent, but new header will be destroyed = correct approach.



