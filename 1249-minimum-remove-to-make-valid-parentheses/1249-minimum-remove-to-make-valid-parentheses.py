class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
#         Al = 2
#         Ar = 3
#         "))(("
        
        cl = 0
        cr = 0
        
        ans = ""
        cl, cr = 0, 0
        for char in s:
            if char == '(':
                ans += char
                cl += 1
            elif char == ')':
                if cr+1 <= cl:
                    ans += char
                    cr += 1
            else:
                ans += char
        # print(ans)
        res = ""  
        for c in ans[::-1]:
            if c == '(':
                if cl > cr:
                    cl-=1
                else:
                    res += c
            else:
                res += c
        return res[::-1]
                
            
        
        
                