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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        ## reverse it, super important to know how to reverse
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp
            first = tmp
            second = tmp2
        

            
        