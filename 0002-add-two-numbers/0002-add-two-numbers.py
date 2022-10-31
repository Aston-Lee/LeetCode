# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = 0
        l3 = pointer = ListNode(0)
        while(l1 or l2):
            if l1: n1 = l1.val
            else: n1 = 0
            if l2: n2 = l2.val
            else: n2 = 0    
            
            total = n1 + n2 + tmp
            tmp = 0
            if total >= 10:
                tmp = 1
                total %= 10
            l3.next = ListNode(total)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if tmp == 1:
            l3.next = ListNode(1)
            l3.next.next = None
        
        return pointer.next
            
            
            