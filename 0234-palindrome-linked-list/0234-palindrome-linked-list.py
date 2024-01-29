# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # not stack

#         # just store to an array and check
#         ## two pointer
#         # maybe with reversed linked list
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next

#         n = len(arr)
#         for i in range(n//2):
#             if arr[i] != arr[n-1-i]:
#                 return False
            
#         return True
        
  
        
        # stack solution
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        
        return True