# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         I'm thinking about stack solution
        
#         k will always keep track if the part needed to reverse or not,
#         if now the part is to be reversed,
        
#         localpointer:
#         store every "value" into a stack
#         iterate until _k runs out 
#             if the localpointer reach to list end while _k still have remained, 
#             we know this part should not be reversed, 
#             thus just use original pointer to run to the end
        
#         stack pop to provide each nodes new value
        
        stack = []
        _k = k
        reverse = False
        prev = None
        pointer = head
        local_pointer = head
        
        while head:
        
            stack.append(local_pointer.val)
            local_pointer = local_pointer.next
            _k -= 1
            
            if _k != 0 and local_pointer == None: ## handle error
                while head:
                    head = head.next
            
            if _k == 0:
                for i in range(k):
                    head.val = stack.pop()
                    head = head.next
                _k = k
                local_pointer = head 
     
        return pointer
        
                
                
            
        
        
    
            