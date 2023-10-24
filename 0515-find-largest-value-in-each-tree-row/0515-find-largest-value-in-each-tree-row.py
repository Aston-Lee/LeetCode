# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            currmax = -float('inf')
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node:
                    continue
                currmax = max(currmax, node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(currmax) if currmax != -float('inf') else None
            
        return res
            
            