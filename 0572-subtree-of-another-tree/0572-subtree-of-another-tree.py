# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
#         Time complexity: O(MN)O(MN). For every NN node in the tree, we check if the tree rooted at node is identical to subRoot. This check takes O(M)O(M) time, where MM is the number of nodes in subRoot. Hence, the overall time complexity is O(MN)O(MN).

#         Space complexity: O(M+N)O(M+N).

#         There will be at most NN recursive call to dfs ( or isSubtree). Now, each of these calls will have MM recursive calls to isIdentical. Before calling isIdentical, our call stack has at most O(N)O(N) elements and might increase to O(N + M)O(N+M) during the call. After calling isIdentical, it will be back to at most             O(N)O(N) since all elements made by isIdentical are popped out. Hence, the maximum number of elements in the call stack will be M+NM+N.
        
        
        def validate(node, subnode):
            if node == None and subnode:
                return False
            elif node and subnode == None:
                return False
            elif node == None and subnode == None:
                return True
            if node.val == subnode.val:
                return validate(node.left, subnode.left) and validate(node.right, subnode.right)
        
        def traverse(node):
            if node == None:
                return False
            
            if node.val == subRoot.val: ## begin traverse
                found = validate(node, subRoot)
                if found == True:
                    return True
            
            return traverse(node.left) or traverse(node.right)
                
        return traverse(root)
            
        