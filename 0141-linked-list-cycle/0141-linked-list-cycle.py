# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while(slow and fast):
            if slow.next and fast.next:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    break
                if not slow or not fast:
                    break
            else:
                break
            if slow == fast:
                 return True
            

            
        return False