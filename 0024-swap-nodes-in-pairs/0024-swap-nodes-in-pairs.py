# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        ptr = dummyNode = ListNode(0)
        dummyNode.next = head
        head = dummyNode
        
        while head.next and head.next.next:
            
            fn = head.next
            sn = head.next.next
            tn = head.next.next.next
            
            head.next = sn
            sn.next = fn
            fn.next = tn
            head = fn
            
        return ptr.next