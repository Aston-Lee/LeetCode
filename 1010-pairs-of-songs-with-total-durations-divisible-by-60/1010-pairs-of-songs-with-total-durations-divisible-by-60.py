class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
#         ## brute force O(n^2) / O(1)
#         if len(time) == 1:
#             return 0
        
#         count = 0
#         for i in range(len(time)-1):
#             for j in range(i+1,len(time)):
#                 if (time[i]+time[j]) % 60 == 0:
#                     count += 1
#         return count

        remainder = defaultdict(int)
        count = 0
        
        for t in time:
            if t%60 == 0:
                count += remainder[0]
            else:
                count += remainder[60-t%60]
            remainder[t%60] += 1
        
        return count
        