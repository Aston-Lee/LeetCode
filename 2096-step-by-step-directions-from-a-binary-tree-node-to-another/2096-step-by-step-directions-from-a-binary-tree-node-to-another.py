# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # parent {
        #     3 : 1
        #     1 : 5
        #     2 : 5
        #     6 : 2
        #     4 : 2
        # }
        
        parent = {}
        
        self.startNode, self.endNode = None, None
        def dfs(node):
            if node.val == startValue:
                self.startNode = node
            if node.val == destValue:
                self.endNode = node
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
                
        dfs(root)
        
        dq = deque([(self.startNode, "")])
        visited = set([self.startNode])
        
        while dq:
            for _ in range(len(dq)):
                node, string = dq.pop()
                # print(node, string)
                if node == self.endNode:
                    return string
                if node.left and node.left not in visited:
                    dq.append((node.left, string+'L'))
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    dq.append((node.right, string+'R'))
                    visited.add(node.right)
                if node in parent and parent[node] not in visited:
                    dq.append((parent[node], string+'U'))
                    visited.add(parent[node])
     