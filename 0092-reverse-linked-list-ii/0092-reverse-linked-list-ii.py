# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
         
            curr = head
            prev = ListNode(0)
            count = 1
            prev.next = curr
            while curr and count != left:
                curr = curr.next
                prev = prev.next
                count += 1
            
            FRONT = prev
            FRONTLINK = curr
            later = curr.next
            while curr and count-1 != right:
                curr.next = prev
                prev = curr 
                curr = later
                if later:
                    later = later.next
                else:
                    later = None
                    break
                count += 1
            BACK = curr
            
            # FRONT.next = prev
            # FRONTLINK.next = BACK
            FRONT.next = prev
            if left == 1:
                head = prev
            FRONTLINK.next = BACK
            
            return head