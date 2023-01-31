# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None:
            return None
        elif k == 0:
            return head
        
        currlength = 0
        slow = fast = head
        
        for i in range(k):
            currlength += 1
            fast = fast.next
            if not fast:
                fast = head
                if k >= currlength:
                    k %= currlength
                    if k == 0:
                        return head
                    else:
                        currenlength = 0
                        for i in range(k):
                            currlength += 1
                            fast = fast.next
                            if not fast:
                                if currlength == k:
                                    return head
                                fast = head
                break
                
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        temp = head
        head = slow.next
        slow.next = None
        fast.next = temp
        return head