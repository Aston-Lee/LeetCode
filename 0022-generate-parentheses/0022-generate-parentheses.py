class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 3
        
        () n=2

        (()) n=1,                  ()() n=1
        
        ((())) n=0, (()()) n=0     (())() n=0,  ()(()) n=0  ()()() n=0
        
        '''
        
        ans = set()
        def addPar(shape, tn):
            if tn == 0:
                ans.add(shape)
                return
            for i, s in enumerate(shape):
                if s == '(':
                    addPar(shape[:i+1]+'()'+shape[i+1:], tn-1)
                    
            addPar(shape+'()', tn-1)
            return 
                    
                    
        addPar("", n)
        return list(ans)
                    
            