class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        Res = []
        def backtrack(candidates, target, tmpRes, start ):
            if target == 0:
                # The [:] slice notation is used to create a new list that is a copy of the original list, which can be modified without affecting the original list.
                Res.append(tmpRes[:]) 
            
            if target <= 0:
                return 
            
            for i in range(start, len(candidates)):
                tmpRes.append(candidates[i])
                backtrack(candidates, target-candidates[i] , tmpRes, i )
                tmpRes.pop()
            return 

        backtrack(candidates, target, [], 0)
        return Res
        

