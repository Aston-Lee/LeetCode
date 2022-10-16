# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # @ two pointer
        def traverse(node1, node2):
            if node1 == None and node2 == None:
                return True
            if  (node1 and node2 == None) or (node1==None and node2) or node1.val != node2.val :
                return False
            return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
        
        return traverse(p, q)