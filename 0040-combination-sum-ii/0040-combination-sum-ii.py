class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## use copy.deepcopy 
        def backtrack(comb, remain, curr, counter, results):
            if remain == 0 :
                #  make a deep copy of the current combination
                #  rather than keeping the reference.
                results.append(copy.deepcopy(comb))
                return 
            elif remain < 0:
                return
            
            for i in range(curr, len(counter)):
                candidate, freq = counter[i]
                
                if freq <= 0:
                    continue
                    
                comb.append(candidate)
                counter[i] = (candidate, freq-1)
                backtrack(comb, remain-candidate, i, counter, results)
                comb.pop()
                counter[i] = (candidate, freq)
                    
        results = []
        counter = collections.Counter(candidates)
        counter = [ (c, counter[c]) for c in counter]
        
        
        
        backtrack( comb = [], remain = target, curr = 0, counter = counter, results = results )
        
        return results
        