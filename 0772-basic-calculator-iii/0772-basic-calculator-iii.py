class Solution:
    def calculate(self, s: str) -> int:
        
        def evaluate(x, y, operand):
            if operand == '+':
                return x
            if operand == '-':
                return -x
            if operand == '*':
                return x*y
            return int(x/y)
            
        stack = []
        previous = '+'
        curr = 0
        s += '@'
        
        for c in s:
            # print(c, stack)
            if c == " ":
                continue
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c == '(': # elif in here crucial?
                stack.append(previous)
                previous = '+'
            else:
                if previous in '*/':
                    stack.append(evaluate(stack.pop(), curr, previous))
                else:
                    stack.append(evaluate(curr, 0, previous))
                
                curr = 0
                previous = c
                if c == ')':
                    while type(stack[-1]) is int:
                        curr += stack.pop()
                    previous = stack.pop()
                    
                    
        return sum(stack)
                    
                    
                
                