class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        '''
        "practice"
        "leetcode"
        Counter({ 'd': 1})
        Counter({ 'p': 1, 'r': 1, 'a': 1, 'i': 1})
        toswap = 4
        changed = 1
        d : 1
        d : None
        '''

        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        # print(dict1)
        # print(dict2)
        toswap, changed = 0, 0
        for key, val in dict1.items():
            if key not in dict2:
                toswap += val
            else:
                if val < dict2[key]:
                    toswap -= val
                    changed += val
                else:
                    toswap += val - dict2[key]
            # print(key, dict1[key], dict2[key], toswap)
        
        return toswap + changed