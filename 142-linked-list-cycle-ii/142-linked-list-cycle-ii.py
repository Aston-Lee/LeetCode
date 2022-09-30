# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## dict solution
        # nodedict = {}
        # while(head):
        #     if head not in nodedict.keys():
        #         nodedict[head] = 1
        #     else:
        #         return head
        #     head = head.next
        # return None
        
        ## set solution
        visited = set()
        
        while(head):
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return None