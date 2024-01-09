# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        '''
        dfs left mid right -> preorder ?
        '''
        list1, list2 = [], []
        def dfs(node, ls):
            if not node:
                return 
            dfs(node.left, ls)
            if not node.left and not node.right:
                ls.append(node.val) 
                return
            dfs(node.right, ls)

        dfs(root1, list1)
        dfs(root2, list2)
        
        return list1 == list2