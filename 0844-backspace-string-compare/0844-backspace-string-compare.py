class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        Sstack = []
        for char in s:
            if char == '#':
                if Sstack:
                    Sstack.pop()
            else:
                Sstack.append(char)
                
        Tstack = []
        for char in t:
            if char == '#':
                if Tstack:
                    Tstack.pop()
            else:
                Tstack.append(char)
                
                
        print(Sstack, )
        if Sstack == Tstack:
            return True
        else:
            return False
        
        
        