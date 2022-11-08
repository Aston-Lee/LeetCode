# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## unbalanced: for any leftdeptht and rightdepth have difference more than 1
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def helper(node):
            if (node == None):
                return True
            if (abs(height(node.left) - height(node.right)) > 1):
                return False
            else:
                return helper(node.left) and helper(node.right)
            
        return helper(root)
