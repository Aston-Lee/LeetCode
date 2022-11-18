# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def traverse(node, maxValue):
            
            if node == None:
                return
            
            if maxValue < node.val:
                maxValue = node.val
                self.counter += 1
            elif maxValue == node.val:
                self.counter += 1
            
            traverse(node.left, maxValue)
            traverse(node.right, maxValue)
            
            return 
        
        traverse(root, -float('inf'))
        
        return self.counter
                
            
            
            
            