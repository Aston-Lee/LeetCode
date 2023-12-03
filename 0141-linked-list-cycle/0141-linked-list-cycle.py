# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        How big is the size of the input? ans:10**10
        How big is the range of values? 0-10**4
        What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs?
        Are there duplicates within the input?
        What are some extreme cases of the input?
        '''
        
        if not head:
            return False
        
        slow = fast = head
        fast = fast.next
        
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if not fast:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                return False
            
        return False
        
        