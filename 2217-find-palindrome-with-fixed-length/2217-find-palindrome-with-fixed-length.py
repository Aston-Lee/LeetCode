class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        l = intLength
        base = 10 ** math.floor((l - 1) / 2)
        res = [q - 1 + base for q in queries]
        print(res)
        for i, s in enumerate(res):
            a = str(s) + str(s)[0:l//2][::-1]
            res[i] = int(a) if len(a) == intLength else -1
        
        return res
            
        