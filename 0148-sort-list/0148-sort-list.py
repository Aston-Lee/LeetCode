# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # brute force
        mem = []
        node = head
        
        while node:
            mem.append(node.val)
            node = node.next
           
        mem.sort()
        
        resptr = res = ListNode(0)
        for num in mem:
            res.next = ListNode(num)
            res = res.next
        
        return resptr.next