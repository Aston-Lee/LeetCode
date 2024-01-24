# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ''' note this is an binary tree '''
        
        if p.val > q.val:
            p, q = q, p
        
        while True: 
            if p.val == root.val or q.val == root.val:
                return root
            
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root 
            
        