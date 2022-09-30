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
        nodedict = {}
        while(head):
            if head not in nodedict.keys():
                nodedict[head] = 1
            else:
                return head
            head = head.next
        return None
        