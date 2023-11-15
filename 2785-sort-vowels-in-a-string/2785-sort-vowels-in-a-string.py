class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        vowelset a e i o u A E I O U
        s   lEetcOde 
        appear E e O e -> E O e e 
        PosSet 1 2 5 7 
        
        charArr = ['E','e','O','e']
        charArr.sort()
        print(charArr)
        
        '''
        vowelset = set("aeiouAEIOU")
        appeared = []
        PosSet = set()
        for i, char in enumerate(s):
            if char in vowelset:
                appeared.append(char)
                PosSet.add(i)
        appeared.sort()
        dq = deque(appeared)
        res = ""
        for i, char in enumerate(s):
            if i in PosSet:
                res += dq.popleft()
            else:
                res += char
        return res
                
        
        
        
        
                
        
            
            
        
                
        
        
        
        
        
        