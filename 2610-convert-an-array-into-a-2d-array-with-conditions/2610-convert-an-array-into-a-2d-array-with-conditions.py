# from sortedcontainers import SortedDict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        '''
        The 2D array should contain only the elements of the array nums.
        Each row in the 2D array contains distinct integers.
        The number of rows in the 2D array should be minimal.
        
        
        [1,3,4,1,2,3,1]
        
        1: 3
        2: 1
        3: 2
        4: 1
        [1,2,3,4], [1,3], [1]
        '''
        # NumFreq = SortedDict()
        NumFreq = collections.Counter(nums)
        NumFreq = {k: v for k, v in sorted(NumFreq.items(), key=lambda item: item[1], reverse = True)}
        
        maxFreq = list(NumFreq.items())[0][1]
        ans = []
        for _ in range(maxFreq):
            ans.append(list())
        
        for key, val in NumFreq.items():
            for i in range(val):
                ans[i].append(key)
                
        return ans