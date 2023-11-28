class Solution:
    def calculate(self, s: str) -> int:
        '''
        "2*(5+5*2)/3+(6/2+8)@"
        prevsign +
        num = 11
        stack = [10,]
        '''
        
        def _calculate(num, sign):
            if sign == '+':
                return num
            elif sign == '-':
                return -num
            elif sign == '*':
                n = stack.pop()
                return int(n*num)
            elif sign == '/':
                n = stack.pop()
                return int(n/num)
            else:
                print("how?")
            
            
        num = 0
        prevsign = '+'
        stack = []
        s += '@'
        
        for char in s:
            
            if char.isdigit():
                num = num*10 + int(char)
                
            elif char in "+-*/":
                stack.append(_calculate(num, prevsign))
                num = 0
                prevsign = char
                
            elif char == '(':
                stack.append(prevsign)
                stack.append('(')
                num = 0
                prevsign = '+'
                
            elif char == ')':
                stack.append(_calculate(num, prevsign))
                num = 0
                # prevsign = '+'
                while stack[-1] != '(':
                    num += stack.pop()
                stack.pop()
                prevsign = stack.pop()
                
            else: #'@'
                stack.append(_calculate(num, prevsign))
                
        return sum(stack)