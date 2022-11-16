# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # possible solution: minheap, 
        # use heap but everytime I store the value and address onto heap
        
#         merge sort 
        
#         merge like 1 and 2 
        
#         create new list 4 the merge wiht 3
        
#         complexity:
            
#         total N nodes 
#         devided to k lists 
#         listsize of N/k
#         Time Complexity: O(Nlogk), Space Complexity: O(1)

        def mergelist(list1, list2):
            head = pointer = ListNode(0)
            while(list1 and list2):
                # print(list1.val, list2.val)
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else: # >=
                    pointer.next = list2 
                    list2 = list2.next
                pointer = pointer.next

            pointer.next = list1 or list2
            return head.next 
        
        def mergersort(lists):
            amount = len(lists)
            interval = 1
            while( interval< amount ):
                for i in range(0, amount-interval, interval*2):
                    lists[i] = mergelist(lists[i], lists[i+interval])
                interval *= 2
                
            return lists[0] if lists else None
        
    
        return mergersort(lists)
                
                
                
                        
                        
                    
                        
            
            
        
        