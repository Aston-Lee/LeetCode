class Solution:
    def calculate(self, s: str) -> int:
        # Function to apply the operation based on the last sign
        def apply_operation(left, right, op):
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return int(left / right)  # Integer division that truncates towards zero

        # Stack to handle parentheses and operators
        stack = []
        current_num = 0
        last_operation = '+'

        for char in s + '+':
            if char.isdigit():
                # Construct the current number
                current_num = current_num * 10 + int(char)
            elif char in '+-*/':
                # Apply the last operation
                if stack and stack[-1] in '*/':
                    # Apply the last high precedence operation
                    last_high_precedence_operation = stack.pop()
                    last_num = stack.pop()
                    current_num = apply_operation(last_num, current_num, last_high_precedence_operation)

                if char in '+-' or char == '+':
                    # Apply the last low precedence operation and reset current_num
                    while stack and stack[-1] in '+-':
                        last_low_precedence_operation = stack.pop()
                        last_num = stack.pop()
                        current_num = apply_operation(last_num, current_num, last_low_precedence_operation)

                # Update the operation and push to stack
                last_operation = char
                stack.append(current_num)
                stack.append(last_operation)
                current_num = 0

            elif char == '(':
                # Push the last operation and reset for new context
                stack.append('(')
            elif char == ')':
                # Resolve the current context
                while stack and stack[-1] != '(':
                    last_operation = stack.pop()
                    last_num = stack.pop()
                    current_num = apply_operation(last_num, current_num, last_operation)
                stack.pop()  # Pop the '('

        # Final operation, if any
        while stack:
            last_operation = stack.pop()
            last_num = stack.pop()
            current_num = apply_operation(last_num, current_num, last_operation)

        return current_num