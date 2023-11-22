class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        mult = 1
        score = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                if i + 1 < len(s) and s[i + 1] == '(':
                    mult *= 2
                else:
                    score += mult
                    i += 1
            else:
                mult //= 2
            i += 1
        return score