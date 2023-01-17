class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # BT(partition , tmpRes , remain) -> bool
        # s = aab
        #     BT(a, [a], ab)
        #         BT(a, [a,a], b)
        #             BT(b, [a,a,b], "")
        #         BT(ab, [a, ab], "")
        #     BT(aa, [aa], b)
        #         BT(b, [aa,b], "")
        #     BT(aab, [abb], "")
        
        Res = []
        
        def is_palindrome(s):
            n = len(s)
            for i in range(len(s)//2):
                if s[i] != s[n-i-1]:
                    return False
            return True
        
        def backtrack(partition, tmpRes, remain):
            if not is_palindrome(partition):
                return
            
            tmpStr = ""
            if remain == "":
                Res.append(tmpRes[:])
            for i, char in enumerate(remain):
                tmpStr += char
                tmpRes.append(tmpStr)
                backtrack(tmpStr, tmpRes, remain[i+1:])
                tmpRes.pop()
                
        backtrack("", [], s)
        return Res