class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
                   
            
#         #1 always comes first, and we fill in all the ones that exist,
#         #if it gets greater than n, then we finish
        ans = []
        
        def recursive(value):
            if len(ans) >= n:
                return
            ans.append(value)
            if (value * 10) <= n:
                recursive(value * 10)
            if value + 1 <= n and value%10 < 9:
                recursive(value + 1)
        recursive(1)

        return ans