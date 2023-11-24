class Solution:
    def decodeString(self, s: str) -> str:
        '''
        2[abc]3[cd]ef
        
        tmp = 
        stack = cbacba, dcdcdc, e, f
        
        fecdcdcdcbacba
        
        abcabcdcdcdcef
        
         
        '''   
        num = 0
        stack = []
        
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)

            elif c == '[':
                stack.append(num)
                num = 0
                stack.append('[')

            elif c == ']':
                tmp = ""
                while stack[-1] != '[':
                    tmp += stack.pop()
                stack.pop()
                stack.append(tmp*stack.pop())
            else:
                stack.append(c)
                
        ans = ""
        while stack:
            ans += stack.pop()
        
        return ans[::-1]
        ## in the end pop all from stack, concat them and reverse