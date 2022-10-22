# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def validate(node, subnode):
            if node == None and subnode:
                return False
            elif node and subnode == None:
                return False
            elif node == None and subnode == None:
                return True
            if node.val == subnode.val:
                return validate(node.left, subnode.left) and validate(node.right, subnode.right)
        
        def traverse(node):
            if node == None:
                return False
            
            if node.val == subRoot.val: ## begin traverse
                found = validate(node, subRoot)
                print(found)
                if found == True:
                    return True
            
            return traverse(node.left) or traverse(node.right)
                
        return traverse(root)
            
        