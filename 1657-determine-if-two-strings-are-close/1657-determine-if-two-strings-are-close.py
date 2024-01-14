class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)
    
        # print((set(dict1.keys()), set(dict2.keys())))
        # print((set(dict1.keys()) == set(dict2.keys())))
        # print(sorted(list(dict1.values())), sorted(list(dict2.values())))
        # print(sorted(list(dict1.values()))==sorted(list(dict2.values())))
        
        return ((set(dict1.keys()) == set(dict2.keys())) and (sorted(list(dict1.values())) == sorted(list(dict2.values()))))
        

        
#         "abbzzca"
#         "babzzcz"
#         ------ 
#         "abbzzcz"
#         ""