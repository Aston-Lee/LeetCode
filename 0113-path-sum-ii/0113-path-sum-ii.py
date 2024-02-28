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
            # print(ls, pathSum, node.val)
            # if pathSum > targetSum:
            #     return
            if pathSum == targetSum and not node.left and not node.right:
                self.ans.append(ls[:])
            
            if node.left:
                dfs(node.left, ls+[node.left.val], pathSum+node.left.val)
            if node.right:
                dfs(node.right, ls+[node.right.val], pathSum+node.right.val)
            
        if root:   
            dfs(root, [root.val], root.val)
        
        return self.ans