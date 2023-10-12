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
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        ## reverse second half  None->LastNode or LastNode->Node
        curr = slow.next
        prev = slow.next = None
        while curr: ##can we further implement an improvment
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
            
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
    

            
        
        

            
        