class Solution:
    def calculate(self, s: str) -> int:
        def operate(op: str, second: int, first: int) -> int:
            if op == '+': return first + second
            if op == '-': return first - second
            if op == '*': return first * second
            if op == '/': return int(first / second)  # Truncate toward zero

        def precedence(op: str) -> int:
            if op in ('+', '-'): return 1
            if op in ('*', '/'): return 2
            return 0

        def apply_operation(ops, values):
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            values.append(operate(op, right, left))

        # Stack for numbers and operators
        numbers = []
        operators = []

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                numbers.append(num)
                continue

            if s[i] in "+-*/":
                while operators and operators[-1] != '(' and precedence(operators[-1]) >= precedence(s[i]):
                    apply_operation(operators, numbers)
                operators.append(s[i])

            elif s[i] == '(':
                operators.append(s[i])

            elif s[i] == ')':
                while operators[-1] != '(':
                    apply_operation(operators, numbers)
                operators.pop()  # pop '('

            i += 1

        while operators:
            apply_operation(operators, numbers)

        return numbers[-1]