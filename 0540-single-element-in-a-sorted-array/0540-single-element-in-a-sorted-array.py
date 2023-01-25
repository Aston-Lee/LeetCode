class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) ==1:
            return nums[0]
        
        l, r = 0 ,len(nums)-1
        
        while l<r:
            if r-l == 2:
                tmpdict = defaultdict(int)
                for i in range(l, r+1):
                    tmpdict[nums[i]] += 1
                for key in tmpdict:
                    if tmpdict[key] == 1:
                        return key
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m]!=nums[m+1]:
                return nums[m]
            elif nums[m] == nums[m-1]:
                if (r-m)%2 == 0:
                    r = m
                else:
                    l = m-1
            elif nums[m] == nums[m+1]:
                if (r-m+1)%2 == 0:
                    r = m+1
                else:
                    l = m
            else:
                print("how")
                
        return r