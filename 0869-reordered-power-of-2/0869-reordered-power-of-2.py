class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
    

        ## generate list of reordered
        numbers = [i for i in str(n)]  
        nlist = list(int(''.join(p)) for p in permutations(numbers))
          
        ## run through nlist, 

        ## if num inside nlist is power of 2, then append to res list
        # res = []
        for num in nlist:
            if (len(str(n)) == len(str(num))) and num!=0 and (num&(num-1) == 0):
                return True
            
        return False
                
                
        # check leading digit is not zero
        
        
       