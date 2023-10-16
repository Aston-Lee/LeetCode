class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        charmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"  
        }
        
        res = []
        strings = []
        for dig in digits:
            strings.append(charmap[dig])
            
        def bt(pos, currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return 
            for i, c in enumerate(strings[pos]):
                bt(pos+1, currstr+c)
            return 
            
        if digits == "":
            return []
        
        bt(0, "")
        return res
    
        