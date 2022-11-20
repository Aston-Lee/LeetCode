class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        Res = []
        def backtrack(candidates, target, tmpRes):
            if target == 0:
                tmpRes = sorted(tmpRes)
                if tmpRes[:] not in Res:
                    Res.append(tmpRes[:])
            
            if target <= 0:
                return 
            
            for n in candidates:
                tmpRes.append(n)
                backtrack(candidates, target-n , tmpRes )
                tmpRes.pop()
            return 

        backtrack(candidates, target, [])
        return Res
        

