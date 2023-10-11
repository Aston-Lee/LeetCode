class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            if t[0] == '-' and len(t)>1:
                stack.append(-int(t[1:]))
            elif t.isnumeric():
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '*':
                    stack.append(n1*n2)
                elif t == '/':
                    stack.append(int(n1/n2))
                elif t == '+':
                    stack.append(n1+n2)
                elif t == '-':
                    stack.append(n1-n2)
        return stack[0]