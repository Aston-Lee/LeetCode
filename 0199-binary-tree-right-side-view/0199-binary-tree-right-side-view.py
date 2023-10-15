# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []

        lst = []
        
        def traverse(node, depth):
            if node == None:
                return

            if depth+1 > len(lst):
                lst.append([])
            lst[depth].append(node.val)
            
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
            return 
        
        traverse( root , 0 )
        res = []
        for l in lst:
            res.append(l[-1])
        return res