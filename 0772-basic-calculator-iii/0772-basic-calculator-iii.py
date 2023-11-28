class Solution:
    def calculate(self, s):
        def update(op, num):
            if op == '+': stack.append(num)
            elif op == '-': stack.append(-num)
            elif op == '*': stack.append(stack.pop() * num)
            elif op == '/': stack.append(int(stack.pop() / num))  # truncate towards zero

        it, num, stack, sign = iter(s), 0, [], "+"
        for c in it:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                update(sign, num)
                num, sign = 0, c
            elif c == '(':
                num = self.calculate(it)  # Recurse for parentheses
            elif c == ')':
                update(sign, num)
                return sum(stack)  # return the result of the expression within the parentheses
            # Skip whitespaces
        update(sign, num)
        return sum(stack)