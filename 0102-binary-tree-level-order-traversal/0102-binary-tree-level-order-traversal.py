# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        # mydict = collections.defaultdict(list)
        lst = []
        
        def traverse(node, depth):
            if node == None:
                return
            
            # mydict[depth].append(node.val)
            if depth+1 > len(lst):
                lst.append([])
            lst[depth].append(node.val)
            
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
            return 
        
        traverse( root , 0 )
        return lst
            