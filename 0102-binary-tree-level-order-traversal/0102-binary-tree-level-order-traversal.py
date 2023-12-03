# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        dq = deque()
       
        
        if root:
            dq.append(root)
        
        while dq:
            n = len(dq)
            print(n)
            tmp = deque()
            tmpres = []
            for i in range(n):
                node = dq.popleft()
                if node:
                    tmpres.append(node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            res.append(tmpres)
            dq = tmp
            tmp = []
            tmpres = []
            
        return res
            
                
            
        