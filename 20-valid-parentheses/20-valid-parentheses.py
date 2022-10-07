class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # @stack
#         stack = []
#         subdict = {'(':')', '[':']', '{':'}'}
#         for c in s:
#             if c=='{' or c=='[' or c=='(':
#                 stack.append(c)
#             elif c =='}' or c==']' or c==')':
#                 if len(stack)>0 and c == subdict[stack[-1]]:
#                     stack.pop(-1)
#                 else: return False
            
#         if len(stack) == 0: return True
#         else:
#             print("how")
#             return False
            
        ## using stack, we pop the last one fi it matches with mapped Parenthesis
        stack = []
        
        ##use dict to store the pair
        mapPar = { ')':'(', "]":"[", "}":"{" }
        
        ## iterate each character and see if it maps
        for char in s:
            if char in mapPar.keys():
                if stack and mapPar[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: ## keys
                stack.append(char)

        return True if not stack else False
        