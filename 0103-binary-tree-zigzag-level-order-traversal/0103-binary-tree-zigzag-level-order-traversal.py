# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         dq 9 20
#         direction = -1
        
        direction = 1
        
        dq = deque([root])
        res = []
        while dq:
            # print(dq)
            tmp = []
            for _ in range(len(dq)):
                node = dq.popleft()
                
                if not node:
                    continue
                tmp.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                    
            if direction == 1:
                direction = -1
                res.append(tmp) if tmp else None 
            else:
                direction = 1
                res.append(tmp[::-1]) if tmp else None 

        
        return res 
        