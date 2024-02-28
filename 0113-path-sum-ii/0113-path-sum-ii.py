# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        
        def dfs(node, ls, pathSum):
            
            if not node:
                return 
            
            ls.append(node.val)
            pathSum += node.val
            
            if pathSum == targetSum and not node.left and not node.right:
                self.ans.append(ls[:]) 
            
            if node.left:
                dfs(node.left, ls, pathSum)
            if node.right:
                dfs(node.right, ls, pathSum)                
                
            ls.pop()
            pathSum -= node.val
         
        
        
        dfs(root, [], 0)
        
        return self.ans