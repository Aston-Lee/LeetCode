class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    
        lastappeared = defaultdict(int)
        appeared = 0
        
        for i, MPG in enumerate(garbage):
            for char in MPG:
                appeared += 1
                lastappeared[char] = i
            
        cumulatedTravel = [0]
        tmp = 0
        for t in travel:
            tmp += t
            cumulatedTravel.append(tmp)
        
        traveltime = 0
        for key, val in lastappeared.items():
            traveltime += cumulatedTravel[val]
            
        return traveltime + appeared
            
                
       
    
#     ["G","P","GP","GG"]
#     G 0 2 3 (0->3) travel 2+4+3 pickup 4 --> 13
#     P 1 2   (0->2) travel 2+4   pickup 2 --> 8
    
#     21

#     travel = [2,4,3]
#     -------------------
#     ["MMM","PGM","GP"]
    
#     dict = {
#         M:4
#         P:2
#         G:2
#     }
    
#     lastappeared = {
#         M:1
#         P:2
#         G:2 (house 2)  
#     } 
    
#     travel = [3,10]
#     -> cumulatedtime = [0, 3, 13]
    
#     traveltime = cumulatedtime[1] + cumulatedtime[2] + cumulatedtime[2]
#                 =  3 + 13 + 13 
#                 = 29
            
#     pickuptime = 4 + 2 + 2
#                 = 8
        
#     ans = 37

       
            
        
    
    