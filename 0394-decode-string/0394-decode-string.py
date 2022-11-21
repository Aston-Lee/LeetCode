class Solution:
    def decodeString(self, s: str) -> str:

        num = 0
        stack = []
        for char in s:
            if char.isdigit():
                num *= 10
                num += int(char)
            elif char == '[': ## char is '[', ']'
                stack.append(num)
                num = 0
                stack.append(char)
                
            elif char == ']':

                tmpStr = ""
                while(stack[-1] != '['):
                    tmpStr += stack.pop()[::-1]
                   
                stack.pop()
                times = stack.pop()
                tmpStr *= times #caca
                stack.append(tmpStr[::-1])
                # print(stack)
                
            else:
                stack.append(char)
        
        res = ""
        for item in stack:
            res += item
        
        return res
                
        # "3[a]2[bc]"
        
        stack:   aaa
            
                  
                    