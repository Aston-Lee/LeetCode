class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = set()
        def dfs(prev, remain, s):
            # print((prev, remain, s))
            if s == target:
                res.add(tuple(prev))
            if not remain:
                return
            for i, r in enumerate(remain):
                if i > 0 and remain[i] == remain[i-1]:
                    continue
                prev.append(r)
                if s+r > target:
                    prev.pop()
                    break
                dfs(prev, remain[i+1:], s+r)
                prev.pop()
            return
        
        dfs([], sorted(candidates), 0)
        return res
        
        
            
        