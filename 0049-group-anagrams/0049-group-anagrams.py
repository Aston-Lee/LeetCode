class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         mymap = {}
#         freq = Counter("eat")
#         mymap[str(freq)] = ["eat","ate"]
#         print(mymap)
        
        mymap = defaultdict(list)
        for string in strs:
            freq = Counter(string)
            sorted_freq = sorted(freq.items(), key=lambda x: x[0])
            mymap[tuple(sorted_freq)].append(string)
        
        res = []
        for key in mymap:
            res.append(mymap[key])
        return res
    
#         res = defaultdict(list)
#             for word in strs:
#                 count = [0]*26
#                 for char in word:
#                     count[ord(char) - ord('a')] += 1
#                 res[tuple(count)].append(word)

#             return res.values()
        