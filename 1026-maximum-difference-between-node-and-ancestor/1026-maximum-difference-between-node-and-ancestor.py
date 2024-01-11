# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''Ancestor
        brue force, pass down all the ancestor 
        '''
        
        ## brute force 
        self.maxDiff = 0
        def dfs(node, anc):
            if not node:
                return 
            
            for a in anc:
                diff = abs(a-node.val)
                self.maxDiff = max(self.maxDiff, diff)
            
            dfs(node.left, [node.val] + anc )
            dfs(node.right, [node.val] + anc )
            
            return 
        
        dfs(root, [])
        
        return self.maxDiff