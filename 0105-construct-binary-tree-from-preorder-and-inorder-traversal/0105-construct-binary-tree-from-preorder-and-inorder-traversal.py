# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)
        
        posdict = {} ## store the index
        for i, n in enumerate(inorder):
            posdict[n] = i
            
        def buildTree2(inorder, left, right):
            node = TreeNode(preorder[0])
            preorder.popleft()
            if posdict[node.val] > left:
                node.left = buildTree2(inorder, left, posdict[node.val]-1)
            elif posdict[node.val] < left:
                node.left = None
                
            if posdict[node.val] < right:
                node.right = buildTree2(inorder, \
                                        posdict[node.val]+1, \
                                        right)
            
            elif posdict[node.val] > right:
                node.right = None
            
            return node
        
        
        return buildTree2(inorder, 0, len(inorder)-1)