class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)
    
        # return ((set(dict1.keys()) == set(dict2.keys())) and (sorted(list(dict1.values())) == sorted(list(dict2.values()))))
        return dict1.keys() == dict2.keys() and sorted(dict1.values()) == sorted(dict2.values())
