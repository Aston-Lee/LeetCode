class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # [[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]]
        
        lose0, lose1 = set(), set()
        loseMore = set()
        
        for winner, loser in matches:
            
#             if winner not in lose1 and winner not in loseMore:
#                 lose0.add(winner)
        
#             if loser in lose0:
#                 lose0.remove(loser)

#             if loser not in lose1:
#                 lose1.add(loser)
#             else:
#                 lose1.remove(loser)
#                 loseMore.add(loser)
                
            if winner not in lose1 and winner not in loseMore:
                lose0.add(winner)
            
            if loser not in lose1 and loser not in loseMore:
                lose1.add(loser)
                if loser in lose0:
                    lose0.remove(loser)
            else:
                if loser in lose1:
                    lose1.remove(loser)
                # if loser not in loseMore: 
                loseMore.add(loser)
            if loser in lose0:
                lose0.remove(loser)
            # print(lose0, lose1, loseMore)
                
        return [sorted(list(lose0)), sorted(list(lose1))]
        