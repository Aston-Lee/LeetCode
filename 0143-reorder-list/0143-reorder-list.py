# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## reverse second half 
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
    
        ## linked 2 list up
        list1, list2 = head, prev
        while list1 and list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2
        if list2:
            list1.next = list2
        return head
            