# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        slow = head
        n = 0
        while slow:
            n += 1
            slow = slow.next
           
        
        if n == 0 or n == 1:
            return head
        k %= n
        if k == 0:
            return head
        
        slow = fast = head 
        for _ in range(k%n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        ptr = slow.next
        slow.next = None
        fast.next = head
        return ptr