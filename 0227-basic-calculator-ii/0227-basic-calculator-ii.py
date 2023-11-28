class Solution:
    def calculate(self, s: str) -> int:
        
        '''
        " 3+5 / 2 "
        num 2
        prevsign /
        stack = [3, 5]
        '''
        def _calculate(num, sign):
            if sign == '+':
                return num
            elif sign == '-':
                return -num
            elif sign == '*':
                n2 = stack.pop()
                return n2 * num
            elif sign == '/':
                n2 = stack.pop()
                return int(n2 / num)
            else:
                print('how')
        
        s = s+'@'
        num = 0
        prevsign = '+'
        stack = []
        for char in s:
            if char == " ":
                continue
            elif char.isdigit():
                    num = num*10 + int(char)
            else:
                stack.append(_calculate(num, prevsign))
                prevsign = char
                num = 0
        return sum(stack)
                
                
        