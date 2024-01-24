class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, freq):
            if node is None:
                return

            # Update frequency using .get() for elegant handling
            freq[node.val] = freq.get(node.val, 0) ^ 1

            # Check for leaf node
            if not node.left and not node.right:
                if sum(freq.values()) <= 1:
                    self.ans += 1
                freq[node.val] = freq.get(node.val, 0) ^ 1
                return 

            # Traverse left and right subtrees
            dfs(node.left, freq)
            dfs(node.right, freq)
            freq[node.val] = freq.get(node.val, 0) ^ 1

        dfs(root, {})
        return self.ans

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
#         self.ans = 0
        
#         def dfs(node, freq):
            
#             # print(node.val)
            
#             if node.val not in freq:
#                 freq[node.val] = 1
#             elif node.val in freq:
#                 if freq[node.val] == 1:
#                     del freq[node.val]
#                 # elif freq[node.val] == 2:
#                 #     freq[node.val] = 1

#             if not node.left and not node.right:
#                 # print(freq)
#                 if len(freq) <= 1:
#                     self.ans += 1   
#                 if node.val not in freq:
#                     freq[node.val] = 1
#                 elif node.val in freq:
#                     if freq[node.val] == 1:
#                         del freq[node.val]
#                 return 
            
#             if node.left:
#                 dfs(node.left, freq)
                
#             if node.right:
#                 dfs(node.right, freq)
                
#             ##need to do reverse
#             if node.val not in freq:
#                 freq[node.val] = 1
#             elif node.val in freq:
#                 if freq[node.val] == 1:
#                     del freq[node.val]
        
#         dfs(root, {})
#         return self.ans
        
        
        
#         ## brute force 
# #         self.ans = 0
# #         self.memory = {}
        
# #         def _check(ls):
# #             if tuple(ls) in self.memory:
# #                 return self.memory[tuple(ls)]
# #             freq = collections.Counter(ls)
# #             singleSet = set()
# #             for key, val in freq.items():
# #                 if val % 2 != 0:
# #                     singleSet.add(key)
# #                     if len(singleSet) > 1:
# #                         self.memory[tuple(ls)] = False
# #                         return False
# #             self.memory[tuple(ls)] = True
# #             return True
            
# #         def dfs(node, ls):
# #             ls.append(node.val)
# #             if not node.left and not node.right:
# #                 if _check(ls):
# #                     self.ans += 1
# #                 ls.pop()
# #                 return 
                
# #             if node.left:
# #                 dfs(node.left, ls)
            
# #             if node.right:
# #                 dfs(node.right, ls)
# #             ls.pop()
# #             return
            
            
# #         dfs(root, [])
# #         return self.ans 