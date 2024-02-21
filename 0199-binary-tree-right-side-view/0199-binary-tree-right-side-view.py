# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # @bfs
        
        dq = deque([root])
        res = []
        while dq:
            thisLevel = []
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node:
                    continue
                thisLevel.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
            res.append(thisLevel[-1]) if thisLevel else None
        return res