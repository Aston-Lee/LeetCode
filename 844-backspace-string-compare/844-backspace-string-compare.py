class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1, stack2 = [], []
        
        def gen(stack, string):
            for char in string:
                if char == '#':
                    if len(stack)>0:
                        stack.pop()
                    else: 
                        continue
                else:
                    stack.append(char)
            return stack
        
        stack1 = gen(stack1, s)
        stack2 = gen(stack2, t)
        
        return stack1 == stack2
        