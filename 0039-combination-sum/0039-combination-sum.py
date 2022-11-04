class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(arr, val):
            if val == target:
                if  sorted(arr) not in res:
                    res.append(sorted(list(arr)))
                return
            if val > target:
                return
            
            for i in range(len(candidates)):
                arr.append(candidates[i])
                backtrack(arr, val+candidates[i])
                arr.pop()

        for n in candidates:
            arr = [n]
            backtrack(arr, n)
            arr.pop()

        return res
