class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
#         brute force 
        
#         [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
        
#         0,2 -> [4,6,5]   4 5 6
#         0,3 -> [4,6,5,9] 4 5 6 9
#         2,5 -> [5,9,3,7] 3 5 7 9

        def check(start, end):
            arr = nums[start: end+1].copy()
            arr.sort()
            gx = arr[1]-arr[0]
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] != gx:
                    return False
            return True
                
            
        res = []
        for i in range(len(l)):
            res.append(check(l[i], r[i]))
            
        return res
            
            
        