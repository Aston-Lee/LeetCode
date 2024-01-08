# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.ans = 0
        def dfs(node):
            if not node:
                return 
            if node.val > high:
                dfs(node.left)
            elif node.val < low:
                dfs(node.right)
            else:
                self.ans  += node.val 
                dfs(node.left)
                dfs(node.right)
            return 
                
        dfs(root)
        return self.ans
                