"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ## stack
        stack, output = [root], []
        while(stack):
            node = stack.pop(-1)
            if node == None:
                return
            output.append(node.val)
            stack.extend(node.children[::-1])
        
        return output