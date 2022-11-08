# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## why the fuck list can be fine and integer will have Local variable referenced problem?
        if root==None: return 0
        output = [] 
        def pre(level, node):
            if node == None: return
            output.append(level)
            pre(level+1, node.left)
            pre(level+1, node.right)
        
        pre(1,root)
        return max(output)