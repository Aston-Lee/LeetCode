class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
#         map 
        
#         BT(tmpRes, remaindigits)
        
#         BT("", 23)
#             BT(a, 3)
#                 BT(ad, "")
#                 BT(ae)
#                 BT(af)
#             BT(b, 3)
#                 BT(bd)
#             BT(c, 3)
        
        charmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"  
        }
        
        Res = []
        if digits == "":
            return Res
        def backtrack(tmpRes, remaindigits):
            if remaindigits == "":
                Res.append(tmpRes)
                return 
            backup = tmpRes
            for char in charmap[remaindigits[0]]:
                tmpRes += char
                backtrack(tmpRes, remaindigits[1:])                
                tmpRes = backup
        backtrack("", digits)
        return Res
        
        
        
        
        
        
        
        
#         charmap = {
#             "2" : "abc",
#             "3" : "def",
#             "4" : "ghi",
#             "5" : "jkl",
#             "6" : "mno",
#             "7" : "pqrs",
#             "8" : "tuv",
#             "9" : "wxyz"  
#         }

#         res = []
#         n = len(digits)
#         def backtrack(prev, remain):
#             tmp_prev = prev
#             for char in charmap[remain[0]]:
#                 prev += char
#                 if len(prev) == n:
#                     res.append(prev)
#                     prev = tmp_prev
#                 else:
#                     backtrack(prev, remain[1:] )
#                     prev = tmp_prev
#             return

#         if not digits:
#             return []

#         backtrack("", digits)
#         return res
        
