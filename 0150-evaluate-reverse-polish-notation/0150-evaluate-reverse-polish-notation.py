class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        '''
        stack 9
        *
        
        '''
        stack = []
        for t in tokens:
            if t.isdigit():
                # print(t)
                stack.append(int(t))
            elif t[0] == '-' and len(t)>1 and t[1].isdigit():
                stack.append(-int(t[1:]))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '+':
                    stack.append(n1+n2)
                elif t == '-':
                    stack.append(n1-n2)
                elif t == '*':
                    stack.append(n1*n2)
                elif t == '/':
                    stack.append(int(n1/n2))
            # print(stack)
                    
        return stack[0]
                
            
            