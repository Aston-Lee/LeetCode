# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def _check(ls):
            l, r = 0, len(ls) - 1
            while l <= r:
                if ls[l] != ls[r]:
                    return False
                l += 1
                r -= 1
            return True

        dq = deque([root])

        while dq:
            level_size = len(dq)
            tmp = []
            for _ in range(level_size):
                current = dq.popleft()
                if current:
                    tmp.append(current.val)
                    dq.append(current.left)
                    dq.append(current.right)
                else:
                    tmp.append(None)  # Use None as the placeholder for null nodes

            if not _check(tmp):
                return False

        return True

        
        