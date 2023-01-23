class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        def is_valid(pal):
            n = len(pal)
            for i in range(n//2):
                if pal[i] != pal[n-1-i]:
                    return False
            return True
        
        i = 0
        while i<len(palindrome):
            if ord(palindrome[i]) > ord('a'):
                modifiedStr = palindrome[:i] + 'a' + palindrome[i+1:]
                if is_valid(modifiedStr) == False:
                    return modifiedStr
            i+=1
        
        i-=1
        while i>-1:
            if ord(palindrome[i]) < ord('z'):
                modifiedStr = palindrome[:i] + chr(ord(palindrome[i])+1) + palindrome[i+1:]
                if is_valid(modifiedStr) == False:
                    return modifiedStr
            i-=1
               
        return ""