class Solution:
    def calculate(self, s: str) -> int:
        def operate(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b)  # truncate towards zero

        def precedence(op):
            if op in ('+', '-'): return 1
            if op in ('*', '/'): return 2
            return 0

        def apply_operation(operators, values):
            right = values.pop()
            left = values.pop()
            op = operators.pop()
            values.append(operate(left, right, op))

        # Stacks for operators and values
        operators, values = [], []

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                val = 0
                while i < len(s) and s[i].isdigit():
                    val = (val * 10) + int(s[i])
                    i += 1
                values.append(val)
                continue
            if s[i] == '(':
                operators.append(s[i])
            elif s[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operation(operators, values)
                operators.pop()  # pop the '('
            else:  # operator
                while operators and precedence(operators[-1]) >= precedence(s[i]):
                    apply_operation(operators, values)
                operators.append(s[i])
            i += 1

        # Apply remaining operations
        while operators:
            apply_operation(operators, values)

        return values[0]