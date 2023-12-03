# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = node = ListNode(0)
        num = 0
        inc = 0
        while l1 and l2:
            num = (l1.val + l2.val + inc)
            if num >= 10:
                num %= 10
                inc = 1
            else:
                inc = 0
            node.next = ListNode(num)
            l1 = l1.next
            l2 = l2.next
            node = node.next
            
        ## one not ended
        if l1 and not l2:
            while l1:
                num = (l1.val + inc)
                if num >= 10:
                    num %= 10
                    inc = 1
                else:
                    inc = 0
                node.next = ListNode(num)
                l1 = l1.next
                node = node.next
            node.next = None
            
        elif not l1 and l2:
            while l2:
                num = (l2.val + inc)
                if num >= 10:
                    num %= 10
                    inc = 1
                else:
                    inc = 0
                node.next = ListNode(num)
                l2 = l2.next
                node = node.next
            node.next = None
            
        if not l1 and not l2:
            if inc == 1:
                node.next = ListNode(1)
                node = node.next
            node.next = None
        else:
            print('how')
        
        return ptr.next