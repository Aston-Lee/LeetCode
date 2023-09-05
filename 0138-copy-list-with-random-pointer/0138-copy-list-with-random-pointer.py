"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        posDict = {None: None}
        inithead = head
        newhead = initnode = Node(0)
        while head:
            tmp = Node(head.val)
            newhead.next = tmp
            posDict[head] = tmp
            head = head.next
            newhead = newhead.next
            
        head = inithead
        newhead = initnode.next
        while head:
            newhead.random = posDict[head.random]
            head = head.next
            newhead = newhead.next
            
        return initnode.next
            
        
        
            
        
        