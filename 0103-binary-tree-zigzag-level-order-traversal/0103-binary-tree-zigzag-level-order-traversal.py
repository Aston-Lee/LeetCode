# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q= deque([root])
        output = []
        reverse = False
        
        while q:
            size =len(q)
            local_res = deque([])
            for _ in range(size):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                if reverse:
                    local_res.appendleft(currNode.val)
                else:
                    local_res.append(currNode.val)
            output.append(local_res)
            reverse = not reverse
        
        return output