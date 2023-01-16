class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        # val = target - currvalue
        
        def backtrack(val, combination, start ):
            if val == 0:
                output.append(combination[:])
                return
            elif val < 0:
                return 
            else:
                for i in range(start, len(candidates)):
                    combination.append(candidates[i])
                    backtrack(val-candidates[i], combination, i)
                    combination.pop()
        
        backtrack(target, [], 0)
        return output

    
        # candidates = [2,3,6,7], target = 7
        # backtrack(7, [])
        #     backtrack(5, [2])    
        #         backtrack(3, [2,2]) 
        #             backtrack(1, [2,2,2]) 
        #                 backtrack(-1, [2,2,2,2]) return
        #                 backtrack(-2, [2,2,2,3]) return
        #                     ..
        #             backtrack(0, [2,2,3]) -> output.append([2,2,3]) -> output = [[2,2,3]]
        #             backtrack(-3, [2,2,6]) return
        #             ..
        #         backtrack(2, [2,3]) 