class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        
        c1, c2 = 0, 0
        for char in s1:
            if char in vowels:
                c1 += 1
        
        for char in s2:
            if char in vowels:
                c2 += 1
        
        return c1 == c2