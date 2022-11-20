class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        Res = []
        def backtrack(candidates, target, tmpRes, start ):
            if target == 0:
                # tmpRes = sorted(tmpRes)
                # if tmpRes[:] not in Res:
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
        

