# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ## heap 
        res = []
        
        def dfs(node):
            if node == None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        heapq.heapify(res)
       
        
        while(k>0):
            q = heapq.heappop(res)
            k -= 1
        
        return q