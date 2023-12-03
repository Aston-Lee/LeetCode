class Solution:
    def calculate(self, s: str) -> int:
        def helper(stack, i):
            num = 0
            sign = '+'

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] in '+-*/':
                    update_stack(stack, num, sign)
                    num = 0
                    sign = s[i]
                elif s[i] == '(':
                    num, i = helper([], i + 1)
                elif s[i] == ')':
                    update_stack(stack, num, sign)
                    return sum(stack), i
                i += 1

            update_stack(stack, num, sign)
            return sum(stack), i

        def update_stack(stack, num, sign):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)

        return helper([], 0)[0]