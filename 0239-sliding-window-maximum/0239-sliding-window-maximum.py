class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        
        res = []
        
        for i, n in enumerate(nums):

            if q and q[0][1] <= i-k:
                q.popleft()      

            while q and n > q[-1][0]:
                q.pop()
            q.append([n, i])
            
            if i >= k-1:
                res.append(q[0][0])
                
        return res
