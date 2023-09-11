class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
 
        # mydict = {
        # 1: [1],
        # 2: [0, 5],
        # 3: [2, 3, 4],
        # }
        mydict = defaultdict(list)
        for i, val in enumerate(groupSizes):
            mydict[val].append(i)
    
        ans = []
        for size, lists in mydict.items():
            while lists:
                tmp = lists[:size]
                lists = lists[size:]
                ans.append(tmp)
            # print(size, lists)
        
        return ans
            
            
            
        