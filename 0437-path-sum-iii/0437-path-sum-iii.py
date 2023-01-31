# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ## prefix sum / dfs traverse
        counter = 0
        
        def dfs(node, preSumDict, preSum):
            if not node:
                return
            nonlocal counter
            preSum += node.val
            counter += preSumDict[preSum-targetSum]
            preSumDict[preSum] += 1
            # print(preSumDict, counter)
            dfs(node.left, preSumDict, preSum)
            dfs(node.right, preSumDict, preSum)    
            preSumDict[preSum] -= 1
            preSum -= node.val
            return
            
            
        preSumDict = defaultdict(int)
        preSumDict[0] = 1
        dfs(root, preSumDict, 0)
        
        return counter