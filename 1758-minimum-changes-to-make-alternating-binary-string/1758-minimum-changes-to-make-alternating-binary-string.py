class Solution:
    def minOperations(self, s: str) -> int:

        # either starts from 1 or starts from 0
        # calculate 2 result and return min
        
        def check(f):
            tmp = 0
            flag = f
            for c in s:
                if c!=flag:
                    tmp += 1
                flag = '0' if flag == '1' else '1'
            return tmp
        
        return min(check('1'), check('0'))