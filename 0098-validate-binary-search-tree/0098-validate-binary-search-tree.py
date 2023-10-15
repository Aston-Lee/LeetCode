# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def traverse( node, leftbound, rightbound ) -> bool:
            
            if node == None:
                return True
            
            if leftbound < node.val and node.val < rightbound:
                
                return traverse(node.left, leftbound, node.val) \
                    and traverse(node.right, node.val, rightbound)
        
            else:
                return False
            
            
        
        return traverse( root, -float('inf'), float('inf') )