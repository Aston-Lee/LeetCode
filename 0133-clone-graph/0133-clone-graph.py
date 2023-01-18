"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == [] or node == None:
            return None
        
        oldtonew = {}
        def createnode(node):
            if node in oldtonew:
                return
            oldtonew[node] = Node(node.val)
            for neighbor in node.neighbors:
                createnode(neighbor)
            return
        
        
        seen = set()
        def linknode(node):
            if node in seen:
                return
            oldtonew[node].neighbors = [oldtonew[neighbor] for neighbor in node.neighbors]
            seen.add(node)
            for neighbor in node.neighbors:
                linknode(neighbor)
            
        
        createnode(node)
        linknode(node)
        return oldtonew[node]
    