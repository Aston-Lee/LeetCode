# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            n = len(dq)
            tmpdq = deque()
            tmpres = []
            for _ in range(n):
                node = dq.popleft()
                if node:
                    tmpres.append(node.val)
                    tmpdq.append(node.left)
                    tmpdq.append(node.right)
            if tmpres:
                res.append(tmpres[-1])
            dq = tmpdq
        return res
            
            