class Solution:
    def decodeString(self, s: str) -> str:
        '''
        
        3[a]2[bc]
        
        stack aaa cbcb
        
        '''
        integer = 0 # record integer 
        stack = []
        for char in s:
            if char.isdigit():
                integer*=10
                integer+=int(char)
                
            elif char == '[':
                stack.append(integer)
                stack.append('[')
                integer = 0

            elif char == ']':
                string = ""
                while stack[-1] != '[':
                    string += stack.pop()
                stack.pop()
                integer = stack.pop()
                stack.append(string*integer)
                string = ""
                integer = 0
                
            else:
                stack.append(char)

        res = ""
        while stack:
            res += stack.pop()
            
        return res[::-1]
                
                