class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        '''
        teams = 7 -> 6/2  +1 = 3 (if odd)
        teams = 4 -> 4/2     = 2
        teams = 2 -> 2/2     = 1
        
        '''
        
        
        teams = n
        matches = 0
        while teams!=1:
            if teams % 2 == 1:
                matches += (teams-1)/2
                teams = teams//2 + 1
            else:
                matches += (teams)/2
                teams = teams//2
        return int(matches)
            