class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        onemap = defaultdict(int)
        
        def getone(n):
            cnt = 0 
            while n:
                if n & 1 :
                    cnt+=1
                n>>=1
            return cnt 
        
        for n in arr:
            onemap[n]= getone(n)
        
        def mergesort(array):
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left = mergesort(array[:mid])
            right = mergesort(array[mid:])
            return merge(left, right)
        
        def merge(arr1, arr2):
            l, r = 0, 0
            tmparr = []
            while l<len(arr1) and r<len(arr2):
                if onemap[arr1[l]] < onemap[arr2[r]]:
                    tmparr.append(arr1[l])
                    l += 1
                elif onemap[arr1[l]] > onemap[arr2[r]]:
                    tmparr.append(arr2[r])
                    r += 1
                else:
                    if arr1[l] < arr2[r]:
                        tmparr.append(arr1[l])
                        l += 1
                    else:
                        tmparr.append(arr2[r])
                        r += 1
                    
            tmparr += arr1[l:] + arr2[r:]
            return tmparr  
            
        return mergesort(arr) 
            
            
            
        