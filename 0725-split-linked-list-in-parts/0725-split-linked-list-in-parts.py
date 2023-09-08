# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        bucketSize = [0] * k
        totalLength = 0
        pointer = head
        while head:
            totalLength += 1
            head = head.next
            
        head = pointer 
        num = 0
        for i in range(totalLength):
            bucketSize[num] += 1
            num += 1
            if num == k:
                num = 0
            
                
        ans = [None] * k
        num = 0
        # Split the linked list
        for i, bs in enumerate(bucketSize):
            currentCount = 0
            tmpNode = tmpPointer = ListNode(0)
            for s in range(bs):
                tmpNode.next = pointer
                if pointer:
                    pointer = pointer.next
                tmpNode = tmpNode.next
            if tmpNode:
                tmpNode.next = None  # Sever the link
            ans[i] = tmpPointer.next
            
        return ans
        
            
        
        