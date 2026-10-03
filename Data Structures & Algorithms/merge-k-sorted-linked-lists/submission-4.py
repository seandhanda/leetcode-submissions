# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

#Brute Force does not even stem from merging 2 lists (where we take minimum value between head of two lists each time), rather we just pick a random lists and merge it into solution sorted list by performing an n traversal, and for k sized lists, this will be n * n time =  inefficient.
#Another thing is taking all node values and sorting them, creating new linked list with this sorted values list


        # Optimal = Mergesort log k times, running merge between 2 lists each level = O(n), together O(n*log k) time.

        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for j in range(0,len(lists),+2):
                mergedLists.append(self.mergeLists(lists[j], lists[j+1] if (j+1) <= len(lists)-1 else None))
            
            lists = mergedLists
        
        return lists[0]


    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
            
        return dummy.next



    #O(n*logk) Time
    #O(k) Space
                