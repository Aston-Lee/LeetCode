# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxWidth = 0
        
        # bfs traverse 
        q = deque()
        q.append((root, 0))
        while q:
            minIndex, maxIndex = float('inf'), -float('inf')
            for i in range(len(q)):
                node, index = q.popleft()
                if not node:
                    continue
                minIndex = min(minIndex, index)
                maxIndex = max(maxIndex, index)
                q.append( (node.left, 2*index) )
                q.append( (node.right , 2*index+1)) 
            if  minIndex != float('inf') and maxIndex != -float('inf'):
                maxWidth = max(maxWidth, (maxIndex - minIndex + 1))
                
        return maxWidth
            