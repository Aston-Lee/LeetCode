class Solution:
    def countPairs(self, root, distance: int) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]  # Leaf node found, return distance as 1

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Check all pairs from left and right for valid distance
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.ans += 1

            # Increment distances by 1 (one level up) and return
            return [d + 1 for d in left_distances + right_distances]

        dfs(root)
        return self.ans



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         '''
#         [43,32,22,72,34,null,28,null,null,null,70]
#         2
#         '''
#         self.ans = 0

#         def dfs(node):  # Returns a tuple (min_dist_to_leaf, leaf_count)
#             if not node:
#                 return float('inf'), 0  # No leaf and infinite distance if the node is None

#             if not node.left and not node.right:
#                 return 1, 1  # Leaf node with distance 1 and count 1

#             left_dist, left_count = dfs(node.left)
#             right_dist, right_count = dfs(node.right)

#             # Check pairs only if both sides have leaves
#             if left_count and right_count:
#                 if left_dist + right_dist <= distance:
#                     self.ans += left_count * right_count

#             # Combine counts from both sides but keep the minimum distance
#             combined_count = left_count + right_count
#             min_dist = 1 + min(left_dist, right_dist)

#             return min_dist, combined_count

#         dfs(root)
#         return self.ans