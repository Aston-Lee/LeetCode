class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
#         c = a^b;
#         You can get a or b back if you have the other value available:

#         a = c^b; // or b^c (order is not important)
#         b = c^a; // or a^c

        mem = [pref[0]]
    
        for i in range(1, len(pref)):
            mem.append(pref[i-1]^pref[i])

        return mem