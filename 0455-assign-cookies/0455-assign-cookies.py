class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        g = [1,2,3], s = [1,1]
               gp          sp
        count = 0
        '''
        
        g.sort()
        s.sort()
        count = 0
        gp, sp = 0,0
        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                count += 1
                gp += 1
                sp += 1
            elif g[gp] > s[sp]:
                sp += 1

        return count