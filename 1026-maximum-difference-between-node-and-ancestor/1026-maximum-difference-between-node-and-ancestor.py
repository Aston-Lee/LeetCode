# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''Ancestor
        brute force, pass down all the ancestor 
        optimal, record currMax, currMin
        '''
        self.maxDiff = 0
        def dfs(node, currMax, currMin):
            if not node:
                self.maxDiff = max(self.maxDiff, currMax - currMin)
                return 
            
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)
            dfs(node.left, currMax, currMin)
            dfs(node.right, currMax, currMin)
            return 
        
        dfs(root, root.val, root.val)
        
        return self.maxDiff
        
        
#         ## brute force, AC 
#         self.maxDiff = 0
#         def dfs(node, anc):
#             if not node:
#                 return 
            
#             for a in anc:
#                 diff = abs(a-node.val)
#                 self.maxDiff = max(self.maxDiff, diff)
            
#             dfs(node.left, [node.val] + anc )
#             dfs(node.right, [node.val] + anc )
            
#             return 
        
#         dfs(root, [])
        
#         return self.maxDiff