class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # BFS, check rotten orange 
        q = deque()
        q.append(0)
        seen = set() # record index
        jump = 0
        while q:
            jump += 1
            for i in range(len(q)):
                pos = q.popleft()
                if pos in seen:
                    continue
                seen.add(pos)
                if pos == len(nums)-1:
                    return jump-1
                n = nums[pos]
                for i in range(1,n+1):
                    if pos+i == len(nums):
                        break
                    q.append(pos+i)
            

                    
        
         