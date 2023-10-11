class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ""
        for char in s:
            char = char.lower()
            if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9') :
                string += char
                
        i = 0
        n = len(string)
        for i in range(n//2):
            if string[i] != string[n-1-i]:
                return False
        return True