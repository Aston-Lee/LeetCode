# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.targetNode = None
        def makeParent(node):
            if not node:
                return
            
            if node.val == target.val:
                self.targetNode = node
            
            if node.left:
                node.left.parent = node
                makeParent(node.left)
            if node.right:
                node.right.parent = node
                makeParent(node.right)
        
        self.root = TreeNode(root.val)
        self.root.left = root.left
        self.root.right = root.right
        makeParent(self.root)
        
        ## bfs find
        visited = set()
        dq = deque([self.targetNode])
        visited.add(self.targetNode)
        
        degree = 0
        while dq and degree != k:
            degree += 1
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node:
                    continue
                if node.left and node.left not in visited:
                    dq.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    dq.append(node.right)
                    visited.add(node.right)
                if node.parent and node.parent not in visited:
                    dq.append(node.parent)
                    visited.add(node.parent)

        res = []
        for node in dq:
            res.append(node.val)
        
        return res 
        
        