# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0)
        pointer = prev
        prev.next = head
        slow = fast = prev
    
        for i in range(n):
            fast = fast.next

        while fast:
            if not fast.next:
                slow.next = slow.next.next
            fast = fast.next
            slow = slow.next
        
        return pointer.next
    
