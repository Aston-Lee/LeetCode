# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.par = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        ## dfs find and make parent 
        def dfs(node, par):
            if not node:
                return            
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)
            return 
            
        dfs(root, None)
        
        res = []
        def find(node, distance, seen):
            if not node:
                return 
            if node in seen:
                return
            if distance == 0:
                res.append(node.val)
                return
            seen.add(node)
            find(node.par, distance-1, seen)
            find(node.left, distance-1, seen)
            find(node.right, distance-1, seen)
            seen.remove(node)
            return
              
        find(target, k, set())
        return res