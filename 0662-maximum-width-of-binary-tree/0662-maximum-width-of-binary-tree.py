# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
#         0
#         2*0 + 2*0+1
#         0 1
        
#         2*0 2*0+1   2*1 2*1+1   
#         0 1 2 3
        
#         2*0 2*0+1 || 2*1 2*1+1 || 2*2 2*2+1 || 2*3 2*3+1
        
#         0 1          2.  3.       4.  5.       6.   7
        
        
        
        dq = deque([(root, 0)])
        maxlength = 0
        while dq:
            # print(dq)
            minIndex, maxIndex = float('inf'), -float('inf')
            for _ in range(len(dq)):
                node, index = dq.popleft()
                minIndex = min(minIndex, index)
                maxIndex = max(maxIndex, index)
                if node.left:
                    dq.append((node.left, 2*index))
                if node.right:
                    dq.append((node.right, 2*index+1))
            
            maxlength = max(maxlength, maxIndex-minIndex+1)
            
        return maxlength
        
        