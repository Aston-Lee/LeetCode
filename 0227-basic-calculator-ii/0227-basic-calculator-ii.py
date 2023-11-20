class Solution:
    def calculate(self, s: str) -> int:
        
        # " 3+5 / 2 @"

        def evaluate(x, y, operator):
            if operator == '+':
                return x
            if operator == '-':
                return -x
            if operator == '*':
                return x*y
            return int(x/y)
        
        stack = []
        previous = '+'
        curr = 0
        s += "@"
        
        for c in s:
            if c == " ":
                continue
            if c.isdigit():
                curr = curr*10 + int(c)
            else: 
                if previous in "*/":
                    stack.append(evaluate(stack.pop(), curr, previous))
                else: ## +-
                    stack.append(evaluate(curr, 0, previous))
                    
                curr = 0
                previous = c
                
        return sum(stack)
                    
                
                        
        
        
        
                        
                    
                
                    
                
        