# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('INF')  # change the variable to a class variable

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))  # change if statement to max(0, dfs(node.left))
            right = max(0, dfs(node.right)) # change if statement to max(0, dfs(node.right))
            self.res = max(self.res, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return self.res