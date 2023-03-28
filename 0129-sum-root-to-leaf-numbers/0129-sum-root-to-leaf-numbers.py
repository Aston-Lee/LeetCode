# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        allList = []
        
        def dfs(node, currList):
            if node == None:
                return
            currList.append(node.val)
            if node.left == None and node.right == None:
                allList.append(currList[:])
            dfs(node.left, currList)
            dfs(node.right, currList)
            currList.pop()
            return
            
        dfs(root, [])
        print(allList)
        
        res = 0
        for valList in allList:
            tmpVal = 0
            for val in valList:
                tmpVal *= 10
                tmpVal += val
            res += tmpVal
            
        return res
                