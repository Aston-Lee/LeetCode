# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = node = ListNode(0)
        addon = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            num = n1 + n2 + addon
            addon = num//10
            node.next = ListNode(num%10)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if addon:
            node.next = ListNode(addon)

        return head.next
            
            