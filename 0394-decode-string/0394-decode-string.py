class Solution:
    def decodeString(self, s: str) -> str:
        
        num = 0
        stack = []
        for char in s:
            if char.isdigit():
                num *= 10
                num += int(char)
            elif char == '[':
                stack.append(num)
                stack.append('[')
                num = 0
            elif char == ']':
                tmpStr = ""
                while stack[-1] != '[':
                    tmpStr += stack.pop()
                stack.pop()
                times = stack.pop()
                stack.append(times*tmpStr)
                # times = 0
                # tmpStr = ""
            else:
                stack.append(char)
                
        res = ""
        while stack:
            res += stack.pop()
        
        return res[::-1]
            
            
            
                  
                    