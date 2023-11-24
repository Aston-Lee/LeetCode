class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        
        n = len(sentence)
        mem = {}
        
        # @lru_cache(None)
        def dp(i):  # return (nextIdx, times) when the i_th word is at the beginning of the row.
            og_i = i
            c = 0
            times = 0
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    times += 1
                    i = 0
            mem[og_i] =  (i, times) ## store it in memoize
            return i, times

        ans = 0
        wordIdx = 0
        for _ in range(rows):
            if wordIdx in mem:
                ans += mem[wordIdx][1]
                wordIdx = mem[wordIdx][0]
            else:
                ans += dp(wordIdx)[1]
                wordIdx = dp(wordIdx)[0]
        return ans
        
        
        
        
#         '''
#         ["i","had","apple","pie"]
#         i-had
#         apple
#         pie-i
#         had--
        
#         pattern {
#             i-had : 0 0
#             apple : 1 0
#             pie-i : 2 1
#             had-- : 3 1
#             apple : 4 1
#             pie-i : 5 2
#             had-- : 6 2
#             apple : 7 2
#             pie-i : 8 3
#             had-- : 9 3
#             apple : 10 3
#             pie-i : 11 4
#         }
        
#         8 5 -> 8-2 = ceil(6/3
#         9 5 -> 9-2 = 7/3
#         10 5 _> 10-2 = 8/3
#         11 -> 11-2 = 9/3
        
        
#         new_cols -= base
        

#         '''
#         i = 0
#         curr = -1
#         tmp = ""
#         output = []
#         cycle = 0
#         pattern = {}
#         base = 0
#         MOD = 0
        
#         while len(output) != rows:
#             # print(i, curr, tmp, output, cycle)
        
#             if curr + len(sentence[i]) < cols:
#                 tmp += sentence[i]
#                 curr += len(sentence[i])
#                 i += 1
#                 if curr+1 < cols:
#                     curr+=1
#                     tmp+='-'
#             else:
#                 while curr != cols-1:
#                     tmp += '-'
#                     curr += 1
                

#             if curr == cols-1:
#                 if tmp not in pattern:
#                     pattern[tmp] = len(output)
#                 else:
#                     MOD = len(output) - pattern[tmp]
#                     cycle = math.ceil((rows - base) / MOD) +1
#                     return cycle
#                 output.append(tmp)
#                 tmp = ""
#                 curr = -1
                
#             if i == len(sentence):
#                 if base == 0:
#                     base = len(output)
#                 cycle += 1
#                 i = 0   
        
#         return cycle